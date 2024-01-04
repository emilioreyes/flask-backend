from flask import Flask
from config import config

#routes
from routes import Producto


app = Flask(__name__)

def page_not_found(error):
    return '<h1>pagina no entrada</h1>',404

if __name__== '__main__':
    #app.config.from_object(config['development'])
    #blueprints
    app.register_blueprint(Producto.main,url_prefix="/api/productos")
    #handler errors
    app.register_error_handler(404,page_not_found)
    #app.run(port=5001)
    app.run(host='0.0.0.0',port=8000,debug=True)