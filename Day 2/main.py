nombre = int(input("Saisissez un nombre: "))

if nombre == 0:
    print("Le nombre est nul")
elif nombre > 0:
    print("Le nombre est positif")
else:
    print("Le nombre est négatif")

if nombre >= 0:
    for i in range(0, nombre + 1):
        print(i)
else:
    for i in range(0, nombre - 1, -1):
        print(i)