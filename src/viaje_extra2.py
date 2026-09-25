#2
distancia_km = 384400  # distancia Tierra - Luna
velocidad_kmh = 5000
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
semanas = tiempo_dias // 7
dias_restantes = tiempo_dias % 7
print(f"Tardarías {semanas} semanas y {dias_restantes} días en llegar.")

#4 
distancia = 225000000
for i in range(10000,60000,10000):
    tiempo= (distancia/ i)
    dias= tiempo/24
    semanas = dias // 7
    dias_restantes = dias % 7
    print((f"VELOCIDAD {i} --> TIEMPO {semanas} semanas y {dias_restantes} días"))