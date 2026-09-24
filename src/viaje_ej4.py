distancia = 225000000
for i in range(10000,60000,10000):
    tiempo= (distancia/ i)
    dias= tiempo/24
    print((f"VELOCIDAD {i} --> TIEMPO {dias}"))