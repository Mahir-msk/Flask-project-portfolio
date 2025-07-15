from flask import Blueprint, render_template, send_from_directory
import os

resume_bp = Blueprint('resume', __name__)

@resume_bp.route('/resume/')
def show_resume():
    return render_template('resume.html')

@resume_bp.route('/resume-file')
def resume_file():
    resume_path = os.path.join('static', 'resume')
    return send_from_directory(resume_path, 'Mahir_Resume.pdf')  # Make sure the filename matches
