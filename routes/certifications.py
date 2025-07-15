from flask import Blueprint,render_template
import os
import json

certifications_bp=Blueprint("certifications",__name__)
@certifications_bp.route('/certifications/')
def show_certifications():
    cert_path=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','data','certifications.json'))
    with open(cert_path,'r',encoding='utf-8')as f:
        certifications=json.load(f)
    return render_template('certifications.html',certifications=certifications)