hora_actual = input("Ingrese la hora en formato de 24 horas (HH:MM): ")
hora, minutos = map(int, hora_actual.split(':'))

if 7 <= hora < 8:
    print("Es hora de desayunar.")
elif 12 <= hora < 13:
     print("Es hora de almorzar.")
elif 18 <= hora < 19:
    print("Es hora de cenar.")
else:
    pass