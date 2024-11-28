edad = int(input("¿Cuántos años tienes? "))

if edad < 18:
    print("Eres menor de edad, no puedes votar aún.")
elif edad >= 18 and edad < 21:
    print("Tienes la edad para votar, pero aún eres joven para otros derechos.")
else:
    print("Eres mayor de 21 años, puedes votar y disfrutar de todos los derechos para adultos.")
