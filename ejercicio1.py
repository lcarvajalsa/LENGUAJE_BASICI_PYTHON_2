sumar_1=[]

def sumar(n1,n2):
    #cuerpo del metodo
    sumar=n1+n2
    #retorno de dato
    return sumar

print("Menu suma")
suma=int(input("Ingrese  UNO para sumar, "))
while suma==1:
    num1=int(input("Ingrese el primer numero"))
    num2=int(input("Ingrese el segundo numero"))
    if suma==1:
        #Invocar metodo suma
        sumar(num1,num2)
        suma_r=sumar(num1,num2)
        sumar_1.append(suma_r)
        suma=int(input("UNO para siguiente suma, DOS para salir"))
    else:
        break    
for i,e in enumerate(sumar_1):
    print(i,e)
#falta sumar y dividir por la cantidad de veses 
        
        
 