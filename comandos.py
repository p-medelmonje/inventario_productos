import sqlite3 as sql
import os

def crearBD():
    if os.path.isfile("BDproductos.db"):
        print("Base de datos encontrada y operativa.")
    
    else:
        conn = sql.connect("BDproductos.db")
        conn.commit()
        conn.close()
        print("Base de datos no encontrada. Se ha creado una nueva base de datos.")

    
def crearTablas():
    conn = sql.connect("BDproductos.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE if not exists productos(
            idProd INTEGER PRIMARY KEY AUTOINCREMENT,
            Cantidad INTEGER NOT NULL,
            Nombre TEXT NOT NULL,
            Categoría TEXT NOT NULL            
        )"""
    )
#     cursor.execute(
#         """CREATE TABLE if not exists usuarios(
#             idUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
#             Nombre TEXT NOT NULL,
#             Contraseña CHAR(10) NOT NULL,
#             Admin BOOL,
#
#         )
#         """
#     )
    conn.commit()
    conn.close()
    
    
def insertarFila(nombre, tipo, cantidad):
    conn = sql.connect("BDproductos.db")
    cursor = conn.cursor()    
    instruccion = f"INSERT INTO productos VALUES({cantidad}, '{nombre}', '{categoria}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    
    
def leerFilas():
    conn = sql.connect("BDproductos.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM productos"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print("Mostrando productos ordenados por \nid, Cant., Nombre, Categoría\n")
    for linea in datos:
        print(linea)
    
    
def insertarFilas(lproductos):
    conn = sql.connect("BDproductos.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO productos VALUES(null,?,?,?)"
    cursor.executemany(instruccion, lproductos)
    conn.commit()
    conn.close()
    print("\nProductos ingresados correctamente")
    
    
def leerOrdenado(campo):
    conn = sql.connect("BDproductos.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM productos ORDER BY {campo}"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)
    
def buscar(busqueda):
    conn = sql.connect("BDproductos.db")
    cursor = conn.cursor()
    # buscar con exactitud
    #instruccion = f"SELECT * FROM productos WHERE nombre = 'Monociclo'"
    # buscar nombres parecidos utilizando % como comodín
    instruccion = f"SELECT * FROM productos WHERE nombre like {busqueda}"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    for d in datos:
        print(d)
    
def actualizarCampos():
    conn = sql.connect("BDproductos.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE productos SET cantidad = 5 WHERE nombre like 'anillo%'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    
def eliminarFila():
    conn = sql.connect("BDproductos.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM productos WHERE nombre like 'anillo%'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    
def eliminarTodo():
    conn = sql.connect("BDproductos.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM productos"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    print(f"{cursor.rowcount} registro(s) eliminado(s)")
    
    
if __name__ == "__main__":
    #crearBD()
    #crearTabla()
    #insertarFila("Anillo de plata", "Anillo", 3)
    #insertarFila("Aros de madera", "Aros", 1)
    #leerFilas()    
    #insertarFilas(productos)
    #leerOrdenado("tipo")
    #buscar()
    #actualizarCampos()
    #eliminarFila()
    pass