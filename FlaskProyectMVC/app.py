
from flask import Flask
from flask_mysqldb import MySQL
from config import Config


mysql= MySQL()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mysql.init_app(app)
    
    from controllers.albumController import albumsBP
    app.register_blueprint(albumsBP)
    
    return app

   
if __name__ == '__main__':
    app=create_app()
    app.run(port=3000, debug=True)