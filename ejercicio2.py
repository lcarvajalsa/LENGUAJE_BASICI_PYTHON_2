# carisellazo
def lanzarMoneda(jugar, eleccion, valor):

    from random import randint, random
    jugar = randint(1, 2)

    if jugar == 1 and eleccion == 1:
        valor = valor+valor
        print(" Salio cara, usted eliguio cara Ganaste....", valor)

    elif jugar == 1 and eleccion == 2:
        valor = valor-valor
        print(" Salio cara, usted eliguio sello Perdiste....", valor)
    elif jugar == 2 and eleccion == 2:
        valor = valor+valor
        print(" Salio sello, usted eliguio sello Ganaste....", valor)
    elif jugar == 2 and eleccion == 1:
        valor = valor-valor
        print(" Salio sello, usted eliguio cara perdiste....", valor)
    elif eleccion != 1 or eleccion != 2:
        print("Digitaste una opcion incorrecta")
    else:
        print("sigue intentando")


print("A jugar")
valor = (int(input("Ingrese el valor a jugador")))
nom = (input("Ingrese el nombre del jugador"))
jugar = (int(input("UNO para cara, DOS para sello")))
aceptar = (int(input("UNO para jugar")))
while aceptar == 1:
    total = lanzarMoneda(nom, jugar, valor)
    repetir = (int(input("deceas jugar nuevamente uno para si dos para no")))
    if repetir==1 and valor>0:
        doblar=(int(input("UNO para doblar, DOS para no")))
        if doblar==1:
            valor=valor*2
            jugar=(int(input("UNO para cara, DOS para sello")))
            total=lanzarMoneda(nom,jugar,valor)
        else:
            print("sinsaldo")
            break
    


