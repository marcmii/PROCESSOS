options = input("Vols codificar o descodificar? ")

if options == "c":
    nFile = input("Entra el nom del arxiu: ")
    f = open(nFile, "rb")
    contingutLlegit = f.read()
    f.close()
    contingutEncriptat = bytearray(contingutLlegit)
    for i in range(len(contingutLlegit)):
        contingutEncriptat[i] = (contingutEncriptat[i] + 1) % 256
    f = open("COD_" + nFile, "wb")
    f.write(contingutEncriptat)
    f.close()

if options == "d":
    nFile = input("Entra el nom del arxiu: ")
    f = open(nFile, "rb")
    contingutLlegit = f.read()
    f.close()
    contingutEncriptat = bytearray(contingutLlegit)
    for i in range(len(contingutLlegit)):
        contingutEncriptat[i] = (contingutEncriptat[i] - 1) % 256
    f = open("DEC_" + nFile, "wb")
    f.write(contingutEncriptat)
    f.close()