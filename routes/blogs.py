from flask import Blueprint, render_template, jsonify
import os
import json

blogs_bp = Blueprint('blogs', __name__)

@blogs_bp.route('/api/blogs')
def get_blogs():
    blogs_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'blogs.json')
    with open(blogs_path, 'r') as f:
        blogs = json.load(f)
    return jsonify(blogs)
