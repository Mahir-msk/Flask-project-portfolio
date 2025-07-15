from flask import Blueprint, render_template, current_app
import os
import json

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/projects/')
def show_projects():
    data_path = os.path.join(current_app.root_path, 'data', 'projects.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        projects = json.load(f)
    return render_template('projects.html', projects=projects)
