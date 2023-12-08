#Making "website" folder a python package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

data_base = SQLAlchemy()
DB_NAME = "database.db"

#Create flask app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'qwertyasdfgh'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    data_base.init_app(app)
    
    #Import blueprints
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note
    
    with app.app_context():
        data_base.create_all()
        
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app