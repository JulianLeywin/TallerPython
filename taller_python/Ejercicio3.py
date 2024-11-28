#Ejercicios de Refuerzo

##Crear un ciclo que escriba python 5 veces en la consola
for i in range(5):
    print("Taller Python")
print()

##Crear un ciclo para que te genere los numeros del 1 a un valor ingresado por teclado
limite = int(input("Escribe un número límite: "))
for i in range(1, limite + 1):
    print(i)
print()

##Crear un ciclo que ingrese los numeros pares ingresados desde 0 hasta un valor que se ingrese por teclado
limite = int(input("Escribe un número límite para los pares: "))
for i in range(0, limite + 1, 2):
    print(i)