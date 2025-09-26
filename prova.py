
"""
hola = ord("B")
print(hola)

adeu = chr(hola)
print(adeu)
"""
options = input("Vols codificar o descodificar? ")

pw = input("Escriu una contrasenya: ")

key = [ord(c) for c in pw]

print(key)