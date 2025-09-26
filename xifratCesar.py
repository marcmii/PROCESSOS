frase = input("Escriu una frase: ")

xifrar = input("Vols xifrar o desxifrar: ")

resultat = ""

if xifrar == "xifrar":
    for i in frase:
        resultat += chr(ord(i) + 1)
    print(resultat)
elif xifrar == "desxifrar":
    for i in frase:
        resultat += chr(ord(i) - 1)
    print(resultat)