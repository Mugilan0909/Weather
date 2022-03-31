from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

def create_app():
    app=Flask(__name__,instance_relative_config=False)
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://hmtcfsrutytyyl:b4bcc6057aa825f8a3af87f898935f99c2315f0e882f66cfafa78bf45de8f3a3@ec2-54-157-79-121.compute-1.amazonaws.com:5432/d8c32okij0b31u'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    db.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()
        app.register_blueprint(routes.post_bp1)

        from .weather import routs

        app.register_blueprint(routs.weather_bp)

        return app

app=create_app()

if __name__=='__main__':
    app.run(debug=False)