"""
api/contact.py - Vercel Serverless Function
Saves contact info
"""
import json
import os
from datetime import datetime
from http.server import BaseHTTPRequestHandler

ASSESSMENTS_FILE = "/tmp/assessments.json"

def load_assessments() -> list:
    if os.path.exists(ASSESSMENTS_FILE):
        try:
            with open(ASSESSMENTS_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_assessments(data: list):
    try:
        with open(ASSESSMENTS_FILE, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"[WARNING] Could not save assessments: {str(e)}")

class handler(BaseHTTPRequestHandler):
    """
    POST /api/contact
    Body: { fullname, email, company, role }
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
            
            required = ["fullname", "email", "company"]
            for field in required:
                if not data.get(field):
                    self._send_json(400, {"error": f"Missing field: {field}"})
                    return
            
            contact_id = datetime.now().isoformat()
            contact_record = {
                "id": contact_id,
                "timestamp": contact_id,
                "type": "contact",
                "fullname": data.get("fullname"),
                "email": data.get("email"),
                "company": data.get("company"),
                "role": data.get("role", "")
            }
            
            assessments = load_assessments()
            assessments.append(contact_record)
            save_assessments(assessments)
            
            print(f"[CONTACT] {data.get('email')} from {data.get('company')}")
            
            self._send_json(200, {"success": True, "id": contact_id})
        
        except json.JSONDecodeError:
            self._send_json(400, {"error": "Invalid JSON"})
        except Exception as e:
            print(f"[ERROR] Contact handler: {str(e)}")
            self._send_json(500, {"error": "Internal server error"})
