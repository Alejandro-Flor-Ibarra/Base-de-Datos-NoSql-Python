# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y
# quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El
# programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el
# cliente es menor de 5 años puede entrar gratis, si tiene entre 5 y 18 años debe pagar 5 mil pesos
# y si es mayor de 18 años debe pagar 10 mil pesos.

edad = int(input("Ingrese su edad "))
if edad < 5 :
    cobro = "Usted entra gratis"
elif edad > 5 and edad < 18 :
    cobro = "Usted debe pagar $5.000"
else:
    cobro = "Usted debe pagar $10.000 C.O.P"

print(f"Su edad es {edad}")
print(cobro)