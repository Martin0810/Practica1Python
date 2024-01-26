edad= int(input("Ingrese la edad del cliente: "))

if edad<4:
    print("El cliente puede entrar gratis")
elif edad>=4 and edad<=18:
    print("El cliente debe pagar $5")
elif edad>18:
    print("El cliente debe pagar $10")