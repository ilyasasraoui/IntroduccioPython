# Programa que pregunta dos números a l'usuari i calcula la seva suma.

num1 = float(input("Ingresa el primer número: "))

num2 = float(input("Ingresa el segundo número: "))

suma = num1 + num2

print(f"La suma de {num1} y {num2} es: {suma}")23



# Programa que pregunta un número i retorna el seu quadrat.

numero = float(input("Ingresa un número: "))

cuadrado = numero ** 2

print(f"El cuadrado de {numero} es: {cuadrado}")



# Programa que pregunta el nom a l'usuari i retorna el text: "Hola Ilyas" és el nom de l'usuari.


nombre = input("Ingresa tu nombre: ")

saludo = "Hola Ilyas"

print(saludo)



# Programa que demana un pes en kg a l'usuari i retorna el mateix pes convertit en lliures.

peso_kg = float(input("Ingresa el peso en kilogramos: "))

peso_lbs = peso_kg * 2.20462

print(f"El peso de {peso_kg} kilogramos es equivalente a {peso_lbs} libras.")



# Programa que demana una temperatura en graus Celsius a l'usuari i retorna la temperatura en graus Fahrenheit.
temperatura_celsius = float(input("Ingresa la temperatura en grados Celsius: "))

temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

print(f"La temperatura de {temperatura_celsius} grados Celsius es equivalente a {temperatura_fahrenheit} grados Fahrenheit.")
