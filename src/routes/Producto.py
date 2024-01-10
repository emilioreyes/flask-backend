from flask import Blueprint,jsonify,request
from flask_jwt_extended import jwt_required
#entities
from models.entities.Producto import Producto

#models
from models.ProductoModel import ProductoModel
main=Blueprint("productos_blueprint ",__name__)

@main.route("/")
@jwt_required()
def get_productos():
    try:
        productos=ProductoModel.get_Productos()
        return jsonify(productos)
    except Exception as ex:
        return jsonify({"message":str(ex)}),500
    

@main.route("/<id>")
@jwt_required()
def getProducto(id):
    try:
        producto=ProductoModel.get_Producto(id)
        if producto != None:
            return jsonify(producto)
        else:
            return jsonify({}),404
    except Exception as ex:
        return jsonify({"message":str(ex)}),500
    
@main.route("/add",methods=["POST"])
def save_Producto():
    try:
        nombre=request.json["nombre"]
        precio=request.json["precio"]
        producto=Producto(0,nombre,precio)
        affected_rows=ProductoModel.save_Producto(producto)
        if affected_rows!=0:
            return jsonify({"message":"save correcto"}),202
        else:
            return jsonify({"message":"not save"}),404
    except Exception as ex:
        return jsonify({"message":str(ex)}),500

