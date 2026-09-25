
def viaje():
    distancia = float(input("Dime la distancia: "))
    velocidad = float(input("Dime la velocidad: "))
    tiempo_horas = distancia / velocidad
    tiempo_dias = tiempo_horas / 24
    print(f"Tardarías {tiempo_dias:.2f} días en llegar.\n")

continuar = "s"

while continuar == "s":
    viaje()
    continuar = input("¿Quieres hacer otra simulación? (s/n): ")

print("¡Gracias por usar el simulador!")