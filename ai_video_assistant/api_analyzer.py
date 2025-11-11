"""
API-based content analysis module for the AI-Powered Video Lecture Assistant.
Uses cloud LLM APIs (OpenAI, Groq, etc.) as an alternative to local Ollama.
"""

import json
import logging
from typing import Dict
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class APIContentAnalyzer:
    """Analyzes lecture transcriptions using cloud LLM APIs."""
    
    # System instruction for the AI model
    SYSTEM_INSTRUCTION = """You are an expert educational assistant and curriculum designer. Your task is to analyze a provided lecture transcription and generate a structured set of learning aids. The output must be in a single, valid JSON object.

Rules:

Summary: The summary must be a single, concise paragraph (4-6 sentences) capturing the main argument and topics of the lecture.

Insights: The insights must be a list of 5-7 distinct, important facts, definitions, or concepts from the text. Each insight should be a single, clear sentence.

Quiz: The quiz must contain exactly 5 multiple-choice questions.

Quiz Structure: Each question must have:
  - A question text.
  - A list of 4 options (as a dictionary with keys A, B, C, D).
  - The correct_answer (which must be a letter: A, B, C, or D).

Relevance: All summaries, insights, and questions must be 100% derived from the provided transcription. Do not introduce external information."""
    
    def __init__(self, api_key: str, provider: str = "openai", model: str = None, timeout: int = 60):
        """
        Initialize the APIContentAnalyzer.
        
        Args:
            api_key: API key for the LLM provider
            provider: API provider ('openai', 'groq', 'anthropic')
            model: Model name (if None, uses provider default)
            timeout: Request timeout in seconds (default: 60)
        """
        self.api_key = api_key
        self.provider = provider.lower()
        self.timeout = timeout
        
        # Set default models and endpoints based on provider
        if self.provider == "openai":
            self.model = model or "gpt-3.5-turbo"
            self.api_url = "https://api.openai.com/v1/chat/completions"
            self.headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }
        elif self.provider == "groq":
            self.model = model or "llama-3.1-8b-instant"
            self.api_url = "https://api.groq.com/openai/v1/chat/completions"
            self.headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }
        elif self.provider == "anthropic":
            self.model = model or "claude-3-haiku-20240307"
            self.api_url = "https://api.anthropic.com/v1/messages"
            self.headers = {
                "Content-Type": "application/json",
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01"
            }
        elif self.provider == "xai":
            self.model = model or "grok-beta"
            self.api_url = "https://api.x.ai/v1/chat/completions"
            self.headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }
        elif self.provider == "google":
            self.model = model or "gemini-2.5-flash"
            # Use v1 API (stable)
            self.api_url = f"https://generativelanguage.googleapis.com/v1/models/{self.model}:generateContent"
            self.api_key = api_key  # Google uses query param, not header
            self.headers = {
                "Content-Type": "application/json"
            }
        else:
            raise ValueError(f"Unsupported provider: {provider}. Use 'openai', 'groq', 'anthropic', 'xai', or 'google'")
        
        logger.info(f"✅ API Analyzer initialized with {self.provider.upper()} ({self.model})")
    
    def _create_user_prompt(self, transcription: str) -> str:
        """Create the user prompt for the LLM."""
        return f"""Here is the transcription from an educational lecture. Please analyze it and provide the summary, key insights, and a 5-question multiple-choice quiz based on the rules.

Transcription:

{transcription}


Output Format:

Provide your response as a single, valid JSON object using this exact schema:

{{
  "summary": "A single-paragraph summary of the lecture content...",
  "insights": [
    "The first key insight or definition.",
    "The second key insight or fact.",
    "..."
  ],
  "quiz": [
    {{
      "question": "What is the first question?",
      "options": {{
        "A": "First option",
        "B": "Second option",
        "C": "Third option",
        "D": "Fourth option"
      }},
      "correct_answer": "B"
    }}
  ]
}}

IMPORTANT: Return ONLY the JSON object, nothing else."""
    
    def _call_api(self, prompt: str) -> str:
        """Call the LLM API to generate content."""
        try:
            logger.info(f"🌐 Calling {self.provider.upper()} API with model: {self.model}")
            
            if self.provider in ["openai", "groq", "xai"]:
                # OpenAI-compatible API format (OpenAI, Groq, xAI)
                payload = {
                    "model": self.model,
                    "messages": [
                        {"role": "system", "content": self.SYSTEM_INSTRUCTION},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.3,
                    "max_tokens": 4096
                }
                
                response = requests.post(
                    self.api_url,
                    headers=self.headers,
                    json=payload,
                    timeout=self.timeout
                )
                response.raise_for_status()
                result = response.json()
                return result['choices'][0]['message']['content']
            
            elif self.provider == "anthropic":
                # Anthropic Claude API format
                payload = {
                    "model": self.model,
                    "max_tokens": 4096,
                    "system": self.SYSTEM_INSTRUCTION,
                    "messages": [
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.3
                }
                
                response = requests.post(
                    self.api_url,
                    headers=self.headers,
                    json=payload,
                    timeout=self.timeout
                )
                response.raise_for_status()
                result = response.json()
                return result['content'][0]['text']
            
            elif self.provider == "google":
                # Google Gemini API format
                full_prompt = f"{self.SYSTEM_INSTRUCTION}\n\n{prompt}"
                payload = {
                    "contents": [{
                        "parts": [{
                            "text": full_prompt
                        }]
                    }],
                    "generationConfig": {
                        "temperature": 0.3,
                        "maxOutputTokens": 4096
                    }
                }
                
                response = requests.post(
                    f"{self.api_url}?key={self.api_key}",
                    headers=self.headers,
                    json=payload,
                    timeout=self.timeout
                )
                response.raise_for_status()
                result = response.json()
                return result['candidates'][0]['content']['parts'][0]['text']
        
        except requests.exceptions.Timeout:
            raise Exception(f"{self.provider.upper()} API request timed out after {self.timeout}s")
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise Exception(f"Invalid API key for {self.provider.upper()}. Please check your API key.")
            elif e.response.status_code == 429:
                raise Exception(f"{self.provider.upper()} API rate limit exceeded. Try again later.")
            else:
                raise Exception(f"{self.provider.upper()} API error: {e.response.status_code} - {e.response.text}")
        except Exception as e:
            raise Exception(f"{self.provider.upper()} API error: {str(e)}")
    
    def analyze(self, transcription: str) -> Dict:
        """
        Analyze a lecture transcription and generate learning aids using API.
        
        Args:
            transcription: The full text transcription of the lecture
        
        Returns:
            Dictionary containing:
                - summary: Concise paragraph summary
                - insights: List of key takeaways (5-7 items)
                - quiz: List of 5 multiple-choice questions
        """
        if not transcription or len(transcription.strip()) < 50:
            raise ValueError("Transcription is too short or empty for meaningful analysis")
        
        word_count = len(transcription.split())
        char_count = len(transcription)
        
        logger.info(f"Analyzing transcription ({char_count:,} characters, ~{word_count:,} words)...")
        
        try:
            # Create the prompt
            prompt = self._create_user_prompt(transcription)
            
            # Generate content via API
            response_text = self._call_api(prompt)
            
            # Extract JSON from response
            response_text = response_text.strip()
            
            # Sometimes the model might wrap JSON in markdown code blocks
            if "```json" in response_text:
                response_text = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                response_text = response_text.split("```")[1].split("```")[0].strip()
            
            # Find the first { and last } to extract JSON
            start_idx = response_text.find("{")
            end_idx = response_text.rfind("}") + 1
            
            if start_idx != -1 and end_idx > start_idx:
                response_text = response_text[start_idx:end_idx]
            
            # Parse JSON
            result = json.loads(response_text)
            
            # Validate the structure
            self._validate_result(result)
            
            logger.info("✅ Analysis completed successfully")
            return result
        
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON response: {str(e)}")
            logger.error(f"Response text: {response_text[:500]}...")
            raise Exception(f"Invalid JSON response from API: {str(e)}")
        
        except Exception as e:
            logger.error(f"Error during analysis: {str(e)}")
            raise
    
    def _validate_result(self, result: Dict):
        """Validate that the result has the expected structure."""
        required_keys = ["summary", "insights", "quiz"]
        for key in required_keys:
            if key not in result:
                raise ValueError(f"Missing required key in response: {key}")
        
        if not isinstance(result["summary"], str):
            raise ValueError("Summary must be a string")
        
        if not isinstance(result["insights"], list) or len(result["insights"]) < 5:
            raise ValueError("Insights must be a list with at least 5 items")
        
        if not isinstance(result["quiz"], list) or len(result["quiz"]) != 5:
            raise ValueError("Quiz must contain exactly 5 questions")
        
        # Validate quiz structure
        for i, question in enumerate(result["quiz"]):
            if "question" not in question or "options" not in question or "correct_answer" not in question:
                raise ValueError(f"Quiz question {i+1} is missing required fields")
            
            options = question["options"]
            if isinstance(options, list):
                # Convert list to dict
                option_dict = {chr(65 + idx): opt for idx, opt in enumerate(options)}
                question["options"] = option_dict
                options = option_dict
            
            if not isinstance(options, dict) or len(options) != 4:
                raise ValueError(f"Quiz question {i+1} must have exactly 4 options as a dictionary")
            
            # Normalize correct_answer to just be the key
            correct_answer = question["correct_answer"]
            if len(correct_answer) == 1 and correct_answer.upper() in options:
                question["correct_answer"] = correct_answer.upper()
            elif correct_answer in options.values():
                # Find the key for this value
                for key, value in options.items():
                    if value == correct_answer:
                        question["correct_answer"] = key
                        break


if __name__ == "__main__":
    # Example usage
    import os
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Set OPENAI_API_KEY environment variable to test")
        exit(1)
    
    analyzer = APIContentAnalyzer(api_key=api_key, provider="openai")
    
    sample_text = """
    Today we're going to discuss machine learning fundamentals.
    Machine learning is a subset of AI that allows computers to learn from data.
    """
    
    try:
        result = analyzer.analyze(sample_text)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error: {e}")
