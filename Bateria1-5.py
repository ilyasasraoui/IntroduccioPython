# Programa que demana una temperatura en graus Celsius a l'usuari i retorna la temperatura en graus Fahrenheit.
temperatura_celsius = float(input("Ingresa la temperatura en grados Celsius: "))

temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

print(f"La temperatura de {temperatura_celsius} grados Celsius es equivalente a {temperatura_fahrenheit} grados Fahrenheit.")
