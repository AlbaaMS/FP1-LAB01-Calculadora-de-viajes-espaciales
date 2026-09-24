edad = int(input("Dime la edad"))
nivel_fisico = int(input("Dime el nivel físico"))
while nivel_fisico < 0 or nivel_fisico > 10:
    nivel_fisico = int(input(("Vuelve a darme el nivel físico en el rango específico")))
                       
if edad < 18:
    print("Debes ser mayor de edad")
elif nivel_fisico < 5: 
    print ("Debes estar en mejor forma")
else: 
    print("¡Listo para despegar!")