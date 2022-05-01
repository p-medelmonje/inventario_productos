"""

### Descripción general del programa

- Utilizar Programación Orientada a Objetos (?)
- Incluir sqlite3.
- Interfaz en consola. Posteriormente en una interfaz gráfica (para empezar, TkInter. Más adelante en PyQt5).
- (Opcional) guardar información en archivo csv o Excel.

- Agradecimientos al canal Dimas y su video de [cómo usar SQLite 3 en Python](https://www.youtube.com/watch?v=uB0928SOTEQ), que me sirvió como refresca memoria.


### Lo que debería hacer el programa

- Crear una tabla de productos en la base de datos y una tabla de usuarios, si no existieren.
- Dar la opción al usuario de añadir, modificar o eliminar productos.
- Dar la opción al usuario de consultar los productos guardados, en general o por categoría.
- Dar la opción de crear tipos de producto, que serán guardados en un diccionario o lista, y ayudarán al usuario a utilizar tipos recurrentes, para que no exista el problema de crear, por ejemplo, una categoría "Deportes" y una categoría "deportivos".
- Campos (inicialmente): Cantidad, Nombre, Tipo, Fecha y hora de ingreso, Usuario.
    - Los datos deben ser obligatorios.

#### Función de añadir productos

[ ] Se solicita al usuario que ingrese el nombre del producto, luego la categoría y al final la cantidad.  
[ ] **(Opcional)** Al momento de ingresar la categoría, se despliega una lista con las categorías utilizadas anteriormente, para facilitar al usuario el uso de las mismas categorías.  
[ ] Al ingresar los datos requeridos, se dará al usuario la opción de ingresar otro producto.  
[ ] Una vez ingresados los productos deseados, el programa confirmará el ingreso con un mensaje en pantalla.  
[ ] **(Opcional)** Dejar una tecla para interrumpir un ingreso.


#### Función de eliminar un producto

[ ] Elegida la opción, se mostrará una advertencia de que al elegir el producto, el programa  lo eliminará sin consultar si está seguro(a).  
[ ] El programa solicitará al usuario escribir el nombre del producto, y luego mostrará una consulta con los productos que tienen nombre semejante.  
[ ] Luego, el programa solicitará al usuario el id del producto que quiere eliminar.  
"""

import sqlite3 as sql
import os
import getpass

from clases import *
from comandos import *

lproductos = []


# La función intro() crea una base de datos si no existe

def intro():
    print("=================================")
    print("Gestor de inventario de productos")
    print("=================================\n")
    


passconfirmar = "guruguru"

# Comienzo de la ejecución del programa

intro()
crearBD()
crearTablas()

# Comienzo de bucle infinito del programa

while True:
    print("\nSelecciona operación:\n1- Añadir producto(s) \n2- Eliminar producto \n3- Consultar base de datos")
    opcion = input("> ")

    while not opcion in "123":
        print("Selecciona operación:\n1- Añadir producto \n2- Eliminar producto \n3- Consultar base de datos")
        opcion = input("> ")
        
        
# Opción 1: Añadir producto(s)

    if opcion == "1":
        print("\nElegida opción de añadir producto(s)")

        while True:

            try:

                nombre = input("Ingrese nombre de producto: ")
                categoria = input("Ingrese categoría de producto: ")
                cantidad = int(input("Ingrese cantidad: "))

            except:
                print("\nError: Uno o más datos inválido(s)\n")

            else:           

                lproductos.append((cantidad, nombre, categoria))    

                reingresar = input("¿Ingresar otro producto? (s) para sí o cualquier otra tecla para no: ").upper()

                if reingresar == "S":
                    print("\n")
                else:
                    insertarFilas(lproductos)
                    break


    # Opción 2: Modificar producto(s)

    elif opcion == "2":
        print("\nElegida opción de modificar producto")
        print("\n1-Eliminar por id\n2-Eliminar todo")
        eliminar = input("> ")
        
        if eliminar == "2":
            while True:
                print("\n¿Está seguro(a) de querer eliminar todos los registros? (s/n)")
                confirmar = input("> ").lower()
                
                while not confirmar in "sn":
                    print("\nOpción no válida. 's' para sí y 'n' para no.")
                    confirmar = input("> ").lower()
                    
                if confirmar == "n":
                    print("Operación cancelada")
                    break
                else: 
                    try:
                        p = getpass.getpass(prompt="Ingresa contraseña: ")
                    except Exception as error:
                        print('ERROR', error)
                    else:
                        print('Password entered:', p)
                        eliminarTodo()
                        break


    # Opción 3: Consultar inventario

    elif opcion == "3":
        print("\n1- Para consultar por todos los productos, \n2- Para consultar por uno específico")
        consulta = input("> ")
        if consulta == "1":
            print("\nMostrando productos ordenados por Nombre, Tipo y Cantidad:\n")
            leerFilas()
        elif consulta == "2":
            busqueda = input("""Buscar por palabras clave, utilizando % como comodín.\nEjemplo: ampolleta% si consulta por ampolletas: """)
            buscar(busqueda)
        else:
            print("Opción inválida")


    else:
        print("Opción inválida")    
    



# In[ ]:




