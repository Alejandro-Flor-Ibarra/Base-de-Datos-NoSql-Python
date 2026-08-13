# La pizzería Napolitana de la Ciudad de Neiva ofrece pizzas vegetarianas y no vegetarianas a
# sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación:
# • Ingredientes vegetarianos: Pimiento y tofu.
# • Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función
# de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se
# puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los
# ingredientes que lleva.
import os 
from platform import system
ingredientes_vegetarianos = ["Pimiento", "Tofu"]
ingredientes_no_vegetarianos = ["Peperoni", "Jamón", "Salmón"]
ingredientes_todos = ["Mozzarella", "Tomate"]
def vegetarianos():
    os.system("cls" if system() == "Windows" else "clear")
    opcion = ""

    while opcion != "1" and opcion != "2" and opcion != "3":
        print("\nIngredientes vegetarianos disponibles:\n")

        for i in range(len(ingredientes_vegetarianos)):
            print(f"{i + 1}. {ingredientes_vegetarianos[i]}")

        print("3. Ambos ingredientes\n")

        opcion = input("Seleccione un ingrediente (1, 2 o 3): ")

        if opcion == "1" or opcion == "2":
            os.system("cls" if system() == "Windows" else "clear")
            ingrediente_elegido = ingredientes_vegetarianos[int(opcion) - 1]
            ingredientes_todos.append(ingrediente_elegido)

            print(
                f"""
╔══════════════════════════════════════════════╗
║              🍕🍕🍕🍕🍕🍕                    ║
║                                              ║
║        SU PIZZA VEGETARIANA LLEVA           
║                                              ║
║              🍕🍕🍕🍕🍕🍕                    ║
╠══════════════════════════════════════════════╣
║                                              ║
║          🍅  {', '.join(ingredientes_todos)}  🧀          
║                                              ║
╠══════════════════════════════════════════════╣
║                                              ║
║          ¡Gracias por su compra! 🍕          ║
║                                              ║
╚══════════════════════════════════════════════╝
"""
            )

        elif opcion == "3":
            os.system("cls" if system() == "Windows" else "clear")
            ingredientes_todos.extend(ingredientes_vegetarianos)

            print(
                f"""
╔══════════════════════════════════════════════╗
║              🍕🍕🍕🍕🍕🍕                    ║
║                                              ║
║        SU PIZZA VEGETARIANA LLEVA           ║
║                                              ║
║              🍕🍕🍕🍕🍕🍕                    ║
╠══════════════════════════════════════════════╣
║                                              ║
║          🍅  {', '.join(ingredientes_todos)}  🧀          
║                                              ║
╠══════════════════════════════════════════════╣
║                                              ║
║          ¡Gracias por su compra! 🍕          ║
║                                              ║
╚══════════════════════════════════════════════╝
"""
            )

        else:
            print("\nOpción incorrecta. Intenta de nuevo.")

def no_vegetarianos():
    os.system("cls" if system() == "Windows" else "clear")
    opcion = ""
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
        print("\nIngredientes no vegetarianos disponibles:\n")
        for i in range(len(ingredientes_no_vegetarianos)):
            print(f"{i + 1}. {ingredientes_no_vegetarianos[i]}")
        print("4. Todos los ingredientes\n")
        opcion = input("Seleccione un ingrediente (1, 2, 3 o 4): ")
        if opcion == "1" or opcion == "2" or opcion == "3":
            os.system("cls" if system() == "Windows" else "clear")
            ingrediente_elegido = ingredientes_no_vegetarianos[int(opcion) - 1]
            ingredientes_todos.append(ingrediente_elegido)
            print(
f"""
╔══════════════════════════════════════════════╗
║              🍕🍕🍕🍕🍕🍕                    ║
║                                              ║
║        SU PIZZA NO VEGETARIANA LLEVA         ║
║                                              ║
║              🍕🍕🍕🍕🍕🍕                    ║
╠══════════════════════════════════════════════╣
║                                              ║
║          🍅  {', '.join(ingredientes_todos)}  🧀          
║                                              ║
╠══════════════════════════════════════════════╣
║                                              ║
║          ¡Gracias por su compra! 🍕          ║
║                                              ║
╚══════════════════════════════════════════════╝
"""
            )
        elif opcion == "4":
            os.system("cls" if system() == "Windows" else "clear")
            ingredientes_todos.extend(ingredientes_no_vegetarianos)
            print(
f"""
╔══════════════════════════════════════════════╗
║              🍕🍕🍕🍕🍕🍕                    ║
║                                              ║
║        SU PIZZA NO VEGETARIANA LLEVA         ║
║                                              ║
║              🍕🍕🍕🍕🍕🍕                    ║
╠══════════════════════════════════════════════╣
║                                              ║
║          🍅  {', '.join(ingredientes_todos)}  🧀          
║                                              ║
╠══════════════════════════════════════════════╣
║                                              ║
║          ¡Gracias por su compra! 🍕          ║
║                                              ║
╚══════════════════════════════════════════════╝
"""
            )
        else:
            print("\nOpción incorrecta. Intenta de nuevo.")

def menu():
    opcion = ""
    while opcion != "1" and opcion != "2":
        os.system("cls" if system() == "Windows" else "clear")
        print("---Bienvenido a la pizzería Napolitana de Neiva ---\n")
        print("\t\t 🍕🍕    ")
        print("\nSeleccione una opción válida:\n")
        print("1. Ingredientes vegetarianos")
        print("2. Ingredientes no vegetarianos")
        print("3. Salir\n")
        opcion = input("Ingrese su opción (1, 2 o 3): ")
        match opcion:
            case "1":
                vegetarianos()
            case "2":
                no_vegetarianos()
            case "3":
                print("Gracias por visitar la pizzería Napolitana de Neiva.")
                break
            case _:
                print("Opción inválida. Por favor, seleccione 1 o 2.")
menu()