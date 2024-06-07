'''
Main entry point of the FreshFarmers application.
'''
from flask import Flask
from flask_session import Session
from models import db
from routes import main_blueprint
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///freshfarmers.db'
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SESSION_TYPE'] = 'filesystem'
    db.init_app(app)
    Session(app)
    app.register_blueprint(main_blueprint)
    return app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)