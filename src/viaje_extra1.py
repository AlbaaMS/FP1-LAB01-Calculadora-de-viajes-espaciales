distancia = int(input("Dame la distancia"))
total_parada = 0
for i in range( 150000, distancia , 150000 ):
    print ((f"Parada en el km {i}"))
    total_parada += 1
print((f"Total de paradas a repostar:{total_parada}"))