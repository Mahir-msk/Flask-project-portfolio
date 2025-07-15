from flask import Blueprint, render_template
import os, json

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    blogs_path = os.path.join(base, 'data', 'blogs.json')
    tech_news_path = os.path.join(base, 'data', 'tech_news.json')

    with open(blogs_path, 'r', encoding='utf-8') as f:
        blogs = json.load(f)

    with open(tech_news_path, 'r', encoding='utf-8') as f:
        news = json.load(f)

    return render_template('home.html', blogs=blogs, news=news)
