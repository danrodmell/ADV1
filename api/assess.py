"""
api/assess.py - Vercel Serverless Function
Uses Open Router API (Llama 2 70B) for cost-effective assessment
"""
import json
import os
from datetime import datetime
from typing import Dict
import urllib.request
import urllib.error
from http.server import BaseHTTPRequestHandler

ASSESSMENTS_FILE = "/tmp/assessments.json"

def load_assessments() -> list:
    """Load existing assessments log"""
    if os.path.exists(ASSESSMENTS_FILE):
        try:
            with open(ASSESSMENTS_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_assessments(data: list):
    """Save assessments log"""
    try:
        with open(ASSESSMENTS_FILE, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"[WARNING] Could not save assessments: {str(e)}")

def calculate_score(answers: Dict[str, int]) -> int:
    """Calculate AI Readiness score (0-100)"""
    total = sum(answers.values())
    # 10 questions × 3 max = 30 total
    return int((total / 30) * 100)

def categorize_maturity(score: int) -> str:
    """Categorize maturity level"""
    if score < 25:
        return "Emergente"
    elif score < 50:
        return "Inicial"
    elif score < 75:
        return "Intermedia"
    else:
        return "Avanzada"

def call_openai(prompt: str, api_key: str) -> str:
    """Call OpenAI Chat Completions API"""
    
    url = "https://api.openai.com/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "gpt-5-mini",
        "messages": [
            {
                "role": "system",
                "content": "Eres un experto en transformación digital y adopción de AI en organizaciones. Responde en español, de manera profesional pero conversacional. Sé conciso y directo, sin fluff."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "max_completion_tokens": 500,
        "top_p": 0.9
    }
    
    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode('utf-8'),
            headers=headers,
            method='POST'
        )
        
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode('utf-8'))
            content = None
            def extract_text(value):
                if isinstance(value, str):
                    return value.strip() or None
                if isinstance(value, dict):
                    for key in ("text", "content", "value"):
                        text = extract_text(value.get(key))
                        if text:
                            return text
                    for key in ("message", "delta"):
                        text = extract_text(value.get(key))
                        if text:
                            return text
                    return None
                if isinstance(value, list):
                    for item in value:
                        text = extract_text(item)
                        if text:
                            return text
                return None
            if isinstance(result, dict):
                choices = result.get("choices")
                if isinstance(choices, list) and choices:
                    first = choices[0] if isinstance(choices[0], dict) else None
                    if isinstance(first, dict):
                        content = extract_text(first)
                if content is None:
                    content = extract_text(result.get("output_text"))
            if content:
                return content
            raise ValueError(f"Unexpected API response format: keys={list(result.keys()) if isinstance(result, dict) else type(result)}")
    
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        print(f"[ERROR] OpenAI HTTP Error: {e.code}")
        print(f"[ERROR] Response: {error_body}")
        raise Exception(f"OpenAI API error: {e.code}")
    except urllib.error.URLError as e:
        print(f"[ERROR] OpenAI URL Error: {str(e)}")
        raise Exception(f"Network error: {str(e)}")
    except Exception as e:
        print(f"[ERROR] OpenAI call failed: {str(e)}")
        raise

class handler(BaseHTTPRequestHandler):
    """
    POST /api/assess
    Body: {
        contact: { fullname, email, company, role },
        answers: { q1: int, q2: int, ..., q10: int }
    }
    
    Returns: {
        score: int,
        diagnosis: str,
        maturity: str
    }
    """

    def _send_json(self, status_code: int, payload: dict):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.end_headers()

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(length).decode("utf-8") if length else "{}"
            data = json.loads(body)
            contact = data.get("contact", {})
            answers = data.get("answers", {})
            
            # Validate answers
            if not all(f"q{i}" in answers for i in range(1, 11)):
                self._send_json(400, {"error": "Missing questions in answers"})
                return
            
            score = calculate_score(answers)
            maturity = categorize_maturity(score)
            
            # Get API key
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("OPENAI_API_KEY not set")
            
            # Build prompt
            prompt = f"""Tu organización tiene un score de AI Readiness de {score}/100 ({maturity}).

Respuestas del assessment (escala 1-3, donde 3 es más maduro):
1. Estrategia de Datos: {answers.get('q1', 1)}
2. Skills de AI en la org: {answers.get('q2', 1)}
3. Infraestructura Cloud: {answers.get('q3', 1)}
4. Gobernanza/Privacidad: {answers.get('q4', 1)}
5. Use Cases Identificados: {answers.get('q5', 1)}
6. Presupuesto AI: {answers.get('q6', 1)}
7. Talento ML/AI: {answers.get('q7', 1)}
8. Change Management: {answers.get('q8', 1)}
9. Data Pipeline/MLOps: {answers.get('q9', 1)}
10. Deployment en Producción: {answers.get('q10', 1)}

Proporciona un diagnóstico ejecutivo en formato:
1. DIAGNÓSTICO (2-3 párrafos sobre el estado actual - sé específico basado en los scores)
2. TOP 3 RECOMENDACIONES (numeradas y prioritizadas)
3. RUTA 6-12 MESES (2-3 hitos clave)

Total máximo 350 palabras. Tono: profesional, director-friendly, directo."""

            # Call OpenAI
            diagnosis = call_openai(prompt, api_key)
            
            # Save to log
            assessment_record = {
                "id": datetime.now().isoformat(),
                "timestamp": datetime.now().isoformat(),
                "type": "assessment",
                "contact": contact,
                "answers": answers,
                "score": score,
                "maturity": maturity,
                "diagnosis_snippet": diagnosis[:200]
            }
            
            assessments = load_assessments()
            assessments.append(assessment_record)
            save_assessments(assessments)
            
            print(f"[ASSESSMENT] {contact.get('email')} from {contact.get('company')} - Score: {score}")
            
            self._send_json(200, {
                "score": score,
                "maturity": maturity,
                "diagnosis": diagnosis
            })
        
        except ValueError as ve:
            print(f"[ERROR] Configuration: {str(ve)}")
            self._send_json(500, {"error": "API key not configured"})
        except json.JSONDecodeError:
            self._send_json(400, {"error": "Invalid JSON"})
        except Exception as e:
            print(f"[ERROR] Assessment handler: {str(e)}")
            self._send_json(500, {"error": "Error processing assessment"})
