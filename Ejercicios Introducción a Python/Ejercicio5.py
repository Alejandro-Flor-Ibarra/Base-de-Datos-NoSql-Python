# Hacer un programa que permita crear una lista de palabras y que, a continuación, pida una
# palabra y diga cuántas veces aparece esa palabra en la lista
palabras = ["gato", "perro", "ratón", "gato", "pez", "gato", "perro", "conejo", "gato", "loro", "hipopotamo", "jirafa", "caballo", "raton"]
contador = 0

palabra_unica = []
print(f"-------LISTADO DE PALABRAS-------")
for palabra in palabras:
    if palabra not in palabra_unica:
        palabra_unica.append(palabra)
for palabra in palabra_unica:
    
    print(f"--{palabra}")

palabra_buscada = input("Ingrese la palabra que desea buscar: ")

for palabra in palabras:
    if palabra == palabra_buscada:
        contador += 1

print(f"La palabra '{palabra_buscada}' aparece {contador} veces en la lista.")