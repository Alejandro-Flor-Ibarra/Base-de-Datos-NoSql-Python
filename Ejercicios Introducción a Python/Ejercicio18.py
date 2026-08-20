from carro import Carro

# creando un objeto de la clase Carro
unCarro = Carro("ABC123", "Toyota", 2020, "Rojo")

print(type(unCarro))

unCarro.girarDerecha()
unCarro.girarIzquierda()
print(f"El carro es de color {unCarro.color.upper()} y su placa es {unCarro.placa}")
# modificando atributo color del objeto unCarro
unCarro.color = "Azul"
print(f"El carro es de color {unCarro.color.upper()} y su placa es {unCarro.placa}")

otroCarro = Carro("XYZ789", "Honda", 2021, "Negro")
print(f"El otro carro es de color {otroCarro.color.upper()} y su placa es {otroCarro.placa}")

unCarro.Acelerar(20)
unCarro.Acelerar(30)
