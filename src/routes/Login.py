from flask import Blueprint,jsonify,request
#entities
from models.entities.Usuario import Usuario

#models
from models.UsuarioModel import UsuarioModel

from flask_cors import cross_origin

main=Blueprint("login_blueprint",__name__)

@main.route("/",methods=["POST"])
def login():
    try:
        username=request.json["username"]
        password=request.json["password"]
        credentials=Usuario(username,password)
        jwt=UsuarioModel.login(credentials)
        if jwt!=None:
            return jsonify({"token":jwt}),202
        else:
            return jsonify({"message":"Bad Credentials"}),401

    except Exception as ex:
        return jsonify({"message":str(ex)}),500