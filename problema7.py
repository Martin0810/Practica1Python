n1= int(input("Ingrese el primer numero: "))
n2= int(input("Ingrese el segundo numero: "))

print("Seleccione una opción:")
print("1. Mostrar la suma de los dos números.") 
print("2. Mostrar la resta (primer número menos segundo número).")
print("3. Mostrar la multiplicación de los dos números.")

opcion=int(input("Ingrese la opcion deseada: "))

if opcion == 1:
    resultado = n1 + n2
    print(f"La suma de {n1} y {n2} es: {resultado}")
elif opcion == 2:
    resultado = n1 - n2
    print(f"La resta de {n1} menos {n2} es: {resultado}")
elif opcion == 3:
    resultado = n1 * n2
    print(f"La multiplicación de {n1} y {n2} es: {resultado}")
else:
    print("Opción no válida.")