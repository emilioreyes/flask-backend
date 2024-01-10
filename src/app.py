from flask import Flask
from flask_cors import CORS,cross_origin
from config import config

#routes
from routes import Producto
from routes import Login

from flask_jwt_extended import JWTManager

app = Flask(__name__)

CORS(app)
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

def page_not_found(error):
    return '<h1>pagina no entrada</h1>',404

if __name__== '__main__':
    #app.config.from_object(config['development'])

    app.register_blueprint(Producto.main,url_prefix="/api/productos")
    app.register_blueprint(Login.main,url_prefix="/api/login")

    #handler errors
    app.register_error_handler(404,page_not_found)

    app.run(host='0.0.0.0',port=8000,debug=True)