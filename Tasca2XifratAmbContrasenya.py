options = input("Vols codificar o descodificar? ")

if options == "c":
    nFile = input("Entra el nom del arxiu: ")
    pw = input("Entra la contrasenya: ")
    key = bytearray(pw.encode("utf-8"))
    f = open(nFile, "rb")
    dades = bytearray(f.read())
    f.close()
    for i in range(len(dades)):
        dades[i] = (dades[i] + key[i % len(key)]) % 256
    f = open("COD_" + nFile, "wb")
    f.write(dades)
    f.close()

if options == "d":
    nFile = input("Entra el nom del arxiu: ")
    pw = input("Entra la contrasenya: ")
    key = bytearray(pw.encode("utf-8"))
    f = open(nFile, "rb")
    dades = bytearray(f.read())
    f.close()
    for i in range(len(dades)):
        dades[i] = (dades[i] - key[i % len(key)]) % 256
    nou_nom = "DEC_" + nFile.replace("COD_", "")
    f = open(nou_nom, "wb")
    f.write(dades)
    f.close()