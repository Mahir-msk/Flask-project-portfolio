from flask import Flask
from routes.home import home_bp
from routes.api import api_bp
from routes.projects import projects_bp
from routes.skills import skills_bp
from routes.certifications import certifications_bp
from routes.achievements import achievements_bp
from routes.contact import contact_bp
from routes.resume import resume_bp
from routes.blogs import blogs_bp

def create_app():
    app=Flask(__name__)

    app.register_blueprint(home_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(skills_bp)
    app.register_blueprint(certifications_bp)
    app.register_blueprint(achievements_bp )
    app.register_blueprint(contact_bp)
    app.register_blueprint(resume_bp)
    app.register_blueprint(blogs_bp)

    return app

if __name__=='__main__':
    app=create_app()
    app.run(host='0.0.0.0',debug=True)
