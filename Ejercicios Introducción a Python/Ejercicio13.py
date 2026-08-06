# Hacer un programa en Python que implemente una función que reciba como parámetro una lista
# con números enteros y como resultado debe devolver la suma de los números.
def suma_lista(listaNumeros):
    suma = 0
    for numero in listaNumeros:
        suma += numero
    return suma

numeros = [1, 2, 3, 4, 5]
resultado = suma_lista(numeros)
print(f"La lista de números es: {numeros}")
print(f"La suma de la lista es: {resultado}")