"""
api/contact.py - Vercel Serverless Function
Saves contact info
"""
import json
import os
from datetime import datetime

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

def handler(request):
    """
    POST /api/contact
    Body: { fullname, email, company, role }
    """
    if request.method != "POST":
        return {
            "statusCode": 405,
            "body": json.dumps({"error": "Method not allowed"})
        }

    try:
        data = json.loads(request.body)
        
        required = ["fullname", "email", "company"]
        for field in required:
            if not data.get(field):
                return {
                    "statusCode": 400,
                    "body": json.dumps({"error": f"Missing field: {field}"})
                }
        
        contact_id = datetime.now().isoformat()
        contact_record = {
            "id": contact_id,
            "timestamp": contact_id,
            "type": "contact",
            "fullname": data.get("fullname"),
            "email": data.get("email"),
            "company": data.get("company"),
            "role": data.get("role", ""),
        }
        
        assessments = load_assessments()
        assessments.append(contact_record)
        save_assessments(assessments)
        
        print(f"[CONTACT] {contact_record['email']} from {contact_record['company']}")
        
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "success": True,
                "id": contact_id
            })
        }
    
    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid JSON"})
        }
    except Exception as e:
        print(f"[ERROR] Contact handler: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal server error"})
        }
