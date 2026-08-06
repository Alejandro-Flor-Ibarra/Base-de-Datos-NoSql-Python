# Ejercicio 4: Convertir un número decimal a binario
def decimal_a_binario(numero):
    respuesta=""
    resultado=numero
    while(True):
        valorInicial = resultado
        residuo = valorInicial % 2
        respuesta += str(residuo)
        resultado = valorInicial // 2
        if resultado == 1:
            respuesta += str(resultado)
            break
    respuesta = "".join(reversed(respuesta))
    return respuesta

numeroEntrada = int(input("Ingrese numero entero para convertir a binario: "))
binario = decimal_a_binario(numeroEntrada)
print(f"El número decimal {numeroEntrada} en binario es: {binario}")