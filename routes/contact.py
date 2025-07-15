from flask import Blueprint, request, jsonify,render_template
import os
import json
from datetime import datetime

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact/')
def contact():
    return render_template('contact.html')

@contact_bp.route('/contact/submit', methods=['POST'])
def submit_contact():
    try:
        data = request.form
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        # Create contact entry
        contact_entry = {
            "name": name,
            "email": email,
            "message": message,
            "timestamp": datetime.now().isoformat()
        }

        # Save to JSON file
        contacts_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'contacts.json')
        if os.path.exists(contacts_path):
            with open(contacts_path, 'r') as f:
                contacts = json.load(f)
        else:
            contacts = []

        contacts.append(contact_entry)

        with open(contacts_path, 'w') as f:
            json.dump(contacts, f, indent=2)

        return jsonify({"success": True})
    
    except Exception as e:
        print("Error saving contact form:", e)
        return jsonify({"success": False, "error": str(e)})
