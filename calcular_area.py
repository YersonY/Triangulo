from triangle import calcular_area

base = float(input("Ingrese la longitud de la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

area = calcular_area(base, altura)
print("El área del triángulo es:", area)
