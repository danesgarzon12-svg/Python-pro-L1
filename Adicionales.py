#1
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))

edad_el_proximo_ano = edad + 1

print("Hola, ", nombre, "¡en un año tendrás ", edad_el_proximo_ano, " años!")
#2

palabra = input("Escribe una palabra: ")

vocales = 0

for letra in palabra:
    if letra in "aeiouAEIOU":
        vocales = vocales + 1

print("Número de vocales:", vocales)
#3
x = 5
x = x + 2
x *= 3
print(x)
