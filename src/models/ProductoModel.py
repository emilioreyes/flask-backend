from database.db import get_conection
from .entities.Producto import Producto
class ProductoModel():

    @classmethod
    def get_Productos(self): 
        try:
            
            conexion=get_conection()
            data=[] 
            try:
                with conexion.cursor() as cursor:
                    sql="select * from productos order by nombre asc"
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    print(result)
                    for row in result:
                        producto=Producto(row[0],row[1],row[2])
                        data.append(producto.to_JSON())
                conexion.close()
            except Exception as e:
                raise Exception(e)
            return data
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_Producto(self,id): 
        try:
            
            conexion=get_conection()
            try:
                with conexion.cursor() as cursor:
                    
                    cursor.execute("select * from productos where id=%s",(id))
                    row = cursor.fetchone()
                    producto=None
                    if row!=None:
                        producto=Producto(row[0],row[1],row[2])
                        producto=producto.to_JSON()
                conexion.close()
            except Exception as e:
                raise Exception(e)
            return producto
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def save_Producto(self,producto): 
        try:   
            conexion=get_conection()
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("""insert into productos (nombre,precio) 
                                   values (%s, %s )""",(producto.nombre, producto.precio))
                    affected_rows=cursor.rowcount
                    conexion.commit()
              
                return affected_rows
            except Exception as e:
                raise Exception(e)
        except Exception as ex:
            raise Exception(ex)