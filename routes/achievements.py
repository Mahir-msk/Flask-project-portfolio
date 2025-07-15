from flask import Blueprint, render_template
import os
import json

achievements_bp = Blueprint('achievements', __name__)

@achievements_bp.route('/achievements/')
def show_achievements():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'achievements.json'))
    with open(path, 'r', encoding='utf-8') as f:
        achievements = json.load(f)
    return render_template('achievements.html', achievements=achievements)
