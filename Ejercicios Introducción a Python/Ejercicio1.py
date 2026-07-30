# ---- Calculadora de impuestos para la nueva reforma tributaria en Colombia ----

# La nueva reforma tributaria en Colombia propone recaudar un impuesto a los salarios de todos
# los colombianos de acuerdo a la siguiente tabla:

# Salario Tasa de Impuesto
# Entre 12 Millon hasta 15 millones ------------ 3%
# Más de 15 Millones hasta 20 Millones --------- 5%
# Más de 20 millones hasta 30 millones --------- 8%
# Más de 30 millones --------------------------  10%

# Escribir un programa en Python que pregunte su salario mensual y muestre por pantalla el
# impuesto que debe pagar.

salario = float(input("Ingrese su salario mensual: "))
impuesto = 0

if salario <= 12000000:
    impuesto = 0
elif salario <= 15000000:
    impuesto = salario * 0.03
elif salario <= 20000000:
    impuesto = salario * 0.05
elif salario <= 30000000:
    impuesto = salario * 0.08
else:
    impuesto = salario * 0.10

print("Su salario es:", salario)
print("El impuesto que debe pagar es:", impuesto)
print("Su salario después del impuesto es:", salario - impuesto)
