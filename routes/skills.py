from flask import Blueprint, render_template
import os
import json

skills_bp = Blueprint('skills', __name__)

@skills_bp.route('/skills/')
def show_skills():
    skills_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'skills.json'))
    with open(skills_path, 'r', encoding='utf-8') as f:
        skills = json.load(f)
    return render_template('skills.html', skills=skills)
