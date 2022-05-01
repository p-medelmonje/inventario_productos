class Producto:
    def __init__(self, ident, tipo, nombre, precio, cantidad):
        self.ident = ident
        self.tipo = tipo.capitalize()
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad   
        
class Usuario:
    def __init__(self, nombre, usuario, passwd):
        self.nombre = nombre
        self.usuario = usuario
        self.passwd = passwd
        
class Admin(Usuario):
    def ingresoAdmin(self):
        print(f"Ingreso de Administrador")
        
        
