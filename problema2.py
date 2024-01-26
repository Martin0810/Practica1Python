consumo = float(input("Estimado cliente, ¿Cuanto fue el monto total de su consumo? "))
porce_propina = int(input("¿Y cuánto porcentaje del consumo total gustaria dejar como propina? "))

propina= consumo*porce_propina/100

print(f"La propina que debe dejar es de: S/{propina}")