continuar = ""
def viaje ():
    distancia = float(input("dime la distancia"))
    velocidad = float(input("dime la velocidad"))
    tiempo_horas = distancia / velocidad
    tiempo_dias = tiempo_horas / 24
    print(f"Tardarías {tiempo_dias} días en llegar.")
    continuar = input("¿Quieres hacer otra simulación? (s/n)")
    return viaje()
viaje ()
while continuar == "s":
    if continuar != "s":
        break
    else:
        viaje()