from flask import jsonify
from database.db import get_conection
from flask_jwt_extended import create_access_token

#entities
from models.entities.Usuario import Usuario

class UsuarioModel():
    @classmethod
    def login(self,credentials:Usuario):
        try:
            cnn=get_conection()
            with cnn.cursor() as cursor:
                cursor.execute("select username from users where username=%s and password=%s",(credentials.username,credentials.password))
                row = cursor.fetchone()
                print(row)
                if row==None:
                    return None
                else:
                    access_token = create_access_token(identity=row[0])
                    return access_token
        except Exception as ex:
            raise Exception(ex)