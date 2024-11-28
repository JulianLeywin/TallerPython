#Ejercicos de Refuerzo 2

##Crear una condicion que permita verificar si un valor ingresado es par o impar
edad = int(input("Escribe la edad: "))
if edad % 2 == 0:
    print("La edad es par.")
else:
    print("La edad es impar.")
print()

##crea una condicion que te permita verificar si un valor es mayor o menor a 20
edad = int(input("Escribe la edad: "))
if edad > 20:
    print("Tiene mas de 20.")
elif edad < 20:
    print("Es menor de 20.")
else:
    print("Tiene 20.")
print()


##crear una condicion que evalue mas de 2 posibilidades
numero = int(input("Escribe un número: "))
if numero > 0:
    print("Es un número positivo.")
elif numero < 0:
    print("Es un número negativo.")
else:
    print("El número es cero.")
