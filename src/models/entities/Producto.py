class Producto():
    def __init__(self,id:int,nombre:str,precio:float) -> None:
        self.id=id
        self.nombre=nombre
        self.precio=precio
    
    def to_JSON(self):
        return {
            "id":self.id,
            "nombre":self.nombre,    
            "precio":self.precio   
        }