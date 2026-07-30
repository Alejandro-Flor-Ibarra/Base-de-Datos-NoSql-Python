# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un
# nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario
# su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input("Ingrese su nombre: ")
primera_letra = nombre[0].upper() 
sexo = input("Ingrese su sexo (M/F): ")
sexo = sexo.upper()  

if sexo == "F" and primera_letra < "M":
    grupo = "A"
elif sexo == "M" and primera_letra > "N":
    grupo = "A"
else:
    grupo = "B"

print(f"Usted pertenece al grupo {grupo}")