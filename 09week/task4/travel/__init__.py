from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create_app():
    app=Flask(__name__)

    #we use this utility module to display forms quickly
    bootstrap = Bootstrap(app)

    #A secret key for the session object
    app.secret_key='somerandomvalue'

    #config upload folder
    UPLOAD_FOLDER = '/static/image'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    #Configue and initialise DB
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///travel123.sqlite'
    db.init_app(app)
    
    #add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)
    from . import destinations
    app.register_blueprint(destinations.bp)
    from . import auth
    app.register_blueprint(auth.bp)

    return app

