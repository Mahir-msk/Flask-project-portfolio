from flask import Blueprint, jsonify
import os, json

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/tech-news')
def get_tech_news():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'tech_news.json'))
    with open(path, 'r', encoding='utf-8') as f:
        news = json.load(f)
    return jsonify(news)
