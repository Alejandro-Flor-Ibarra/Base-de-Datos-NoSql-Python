import pymysql as mysql
import os
from dotenv import load_dotenv
#crear variables para conexion a base de datos
load_dotenv()


user= os.getenv("user")
password=os.getenv("password")
database= os.getenv("baseDatos")
host= os.getenv("host")

#se crea un objeto de topo conexion

miConexion=mysql.connect(
    host=host, 
    user=user, 
    database=database, 
    password=password)
print(miConexion)
print(type(miConexion))

#crear objeto de tipo cursor necesario
cursor = miConexion.cursor()
def agregar():
    try:
        #producto a agregar con codido nombre precio y categoria
        producto = ("5", "sombrero", 28000, "ropa")
        consulta = "insert into productos values(null, %s, %s, %s, %s)"
        cursor.execute(consulta,producto)
        miConexion.commit()
        if(cursor.rowcount==1):
            print("Producto agregado correctamente")

    except mysql.Error as e:
        miConexion.rollback()
        print(str(e))


def listar():
    try:
        consulta = "SELECT * FROM productos"
        cursor.execute(consulta)
        productos = cursor.fetchall()

        if productos:
            print("\n" + "=" * 90)
            print(
                f"{'ID':<6}"
                f"{'CODIGO':<15}"
                f"{'NOMBRE':<25}"
                f"{'PRECIO':<15}"
                f"{'CATEGORIA':<20}"
            )
            print("=" * 90)

            for producto in productos:
                print(
                    f"{producto[0]:<6}"
                    f"{producto[1]:<15}"
                    f"{producto[2]:<25}"
                    f"${producto[3]:<14.2f}"
                    f"{producto[4]:<20}"
                )

            print("=" * 90)
            print(f"Total de productos: {len(productos)}")

        else:
            print("No hay productos registrados")

    except mysql.Error as e:
        print(str(e))

def consultarPorCodigo():
    try:
        codigo = input("Ingrese código de producto a consultar: ")
        codigoAConsultar=(codigo,)
        consulta ="select * from productos where proCodigo=%s"
        cursor.execute(consulta,codigoAConsultar)
        producto=cursor.fetchone()
        if producto:
            print(f"Id: {producto[0]}")
            print(f"codigo: {producto[1]}")
            print(f"Nombre: {producto[2]}")
            print(f"Precio: {producto[3]}")
            print(f"Categoria: {producto[4]}")
        else:
            print("No existe producto con ese codigo")

    except mysql.Error as e:
        print(str(e))

def actualizar():
    try:
        datosActualizar=("Botines",1)
        consulta = "update productos set proNombre=%s where idProducto=%s"
        cursor.execute(consulta, datosActualizar)
        miConexion.commit()
        if cursor.rowcount ==1:
            print("producto actualizado")
        else: 
            print("No existe producto con ese Id")
    
    except mysql.Error as e:
        miConexion.rollback()
        print(str(e))
def eliminar():
    try:
        productoEliminar = (1,)
        consulta = "delete from productos where idProducto=%s"
        cursor.execute(consulta, productoEliminar)
        miConexion.commit()
        if cursor.rowcount ==1:
            print("producto eliminado")
        else: 
            print("No existe producto con ese Id")
    
    except mysql.Error as e:
        miConexion.rollback()
        print(str(e))

def agregarVarios():
    try:
        productos = [
            ("18", "zapatillas", 12000, "calzado"),
            ("19", "pantalones", 30000, "ropa"),
            ("20", "pantalon de cuero", 45000, "ropa")
        ]

        consulta = "INSERT INTO productos VALUES(NULL, %s, %s, %s, %s)"

        cursor.executemany(consulta, productos)
        miConexion.commit()

        if cursor.rowcount == len(productos):
            print("Productos agregados correctamente")

    except mysql.Error as e:
        miConexion.rollback()
        print(str(e))
def revisarCategoria():
    try:
        categoria = input("Ingrese la categoria a consultar: ")
        categoriaAConsultar = (categoria,)

        consulta = "SELECT * FROM productos WHERE proCatergoria = %s"

        cursor.execute(consulta, categoriaAConsultar)
        productos = cursor.fetchall()

        if productos:
            print("\n" + "=" * 75)
            print(f"{'ID':<5} {'CODIGO':<15} {'NOMBRE':<25} {'PRECIO':<15} {'CATEGORIA':<15}")
            print("=" * 75)

            for producto in productos:
                print(f"{producto[0]:<5} {producto[1]:<15} {producto[2]:<25} {producto[3]:<15.2f} {producto[4]:<15}")

            print("=" * 75)

        else:
            print("No existe producto con esa categoria")

    except mysql.Error as e:
        miConexion.rollback()
        print(str(e))
#revisarCategoria()
listar()
#agregar()
#consultarPorCodigo()
#actualizar()
#eliminar()
#agregarVarios()