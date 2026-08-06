# Hacer un programa en Python que utilizando y listas y otras estructuras de programación permite
# simular los procesos de un banco relacionado con las cuentas de ahorro. La aplicación debe
# permitir lo siguiente:
# a. Crear una cuenta de ahorros. Las cuentas de ahorro tienen el siguiente código:
# año-consecutivo.
# Ejemplo: 2026-1, la siguiente sería 2026-2, 2026-3 y así sucesivamente. El año se tiene
# que obtener de la fecha actual.
# b. Agregar los datos del cliente dueño de una cuenta de ahorros con los siguientes datos:
# identificación, nombre completo y correo electrónico.
# c. De las cuentas de ahorro se requieren conocer los siguientes datos: código de la cuenta,
# fecha de creación saldo.
# d. Consignar a una determinada cuenta
# e. Retirar a una determinada cuenta.
# La solución debe presentar un menú de opciones así:
# MENÚ BANCO ADSO 3229426
# 1. Crear Cuenta
# 2. Consignar Cuenta
# 3. Retirar Cuenta
# 4. Consultar Cuenta Por Código
# 5. Consultar Cuenta por Identificación Cliente
# 6. Listar Cuentas
# 7. Salir
# Ingrese Opción (1-7):


from datetime import datetime
import os
from platform import system
cuentas = []
clientes = []
def crearCliente():
    os.system("cls")
    identificacion = input("Ingrese la identificación del cliente: ")
    existeCliente = False
    for cliente in clientes:
        if cliente["identificacion"] == identificacion:
            existeCliente = True
            
            break
    if existeCliente == False:

        nombre = input("Ingrese el nombre completo del cliente: ")
        correo = input("Ingrese el correo electrónico del cliente: ")
        cliente = {
            "identificacion": identificacion,
            "nombre": nombre,
            "correo": correo
        }
        clientes.append(cliente) #agregando cliente a la lista de clientes
        return identificacion
    else:
        print("El cliente ya existe.")
        return identificacion
def crearCuenta():
    os.system("cls")
    print("\t \tCREACION DE CUENTA")
    identificacionCliente = crearCliente()
    fechadehoy = datetime.now()
    yearNow = datetime.now().year
    consecutivo = len(cuentas) + 1
    codigoCuenta = f"{yearNow}-{consecutivo}"
    saldo = float(input("Ingrese el saldo inicial de la cuenta: "))
    cuenta = {
        "codigo": codigoCuenta,
        "fecha_creacion": fechadehoy,
        "saldo": saldo,
        "identificacion_cliente": identificacionCliente
    }
    cuentas.append(cuenta)
def consignarCuenta():
    os.system("cls")
    print("\t \tCONSIGNAR A CUENTA")
def retirarCuenta():
    pass
def consultarCuentaPorCodigo():
    pass
def consultarCuentaPorIdentificacionCliente():
    pass
def listarCuentas():
    os.system("cls")
    print("\t \tLISTADO DE CUENTAS")
    for cuenta in cuentas:
        print(f" Código: {cuenta['codigo']}, Fecha de Creación: {cuenta['fecha_creacion']}, Saldo: {cuenta['saldo']}")

def menu():
    
    print("\t \tMENÚ BANCO ADSO 3229426")
    opcion = 0
    while opcion != 7: 
        os.system("cls")
        print("\t1. Crear Cuenta")
        print("\t2. Consignar Cuenta")
        print("\t3. Retirar Cuenta")
        print("\t4. Consultar Cuenta Por Código")
        print("\t5. Consultar Cuenta por Identificación Cliente")
        print("\t6. Listar Cuentas")
        print("\t7. Salir")
        opcion = int(input("Ingrese Opción (1-7): "))
        match opcion:
            case 1:
                crearCuenta()
            case 2:
                consignarCuenta()
            case 3:
                retirarCuenta()
            case 4:
                consultarCuentaPorCodigo()
            case 5:
                consultarCuentaPorIdentificacionCliente()
            case 6:
                listarCuentas()
            case 7:
                print("Saliendo del programa...")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")
        input("Presione Enter para continuar...")

menu()
