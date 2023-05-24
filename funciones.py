#1.Declaracion de un metodo
#2.Declaracion de un metodo con parametros
def restar(n1,n2):
    restar=n1-n2
    print(f"la resta entre {n1} y {n2} es {restar}")
#2.Declaracion de un metodo con valor de retorno
def multiplicar(n1,n2):
    #cuerpo del metodo
    multiplicar=n1*n2
    #retorno de dato
    return multiplicar

def sumar(n1,n2):
    #cuerpo del metodo
    sumar=n1+n2
    #retorno de dato
    return sumar
   
    
#Llamado o invocación de metodo
print("Menu opciones")
num1=int(input("Ingrese el primer numero"))
num2=int(input("Ingrese el segundo numero"))
op=input("Ingrese la opcion segun la operacion a realizar \n UNO suma, DOS resta, TRES Multiplicar, CUATRO Dividir, CINCO promedio")

#argumentos 

if op==1:
    #Invocar metodo suma
    sumar(num1,num2)
    op=input("Infresa nueva suma")
 

elif op==2:
    #Invocar metodo con parametros
    restar(num1,num2)
elif op==3:
    #Invocer metodo con valor de retorno
    #multiplicar(num1,num2)
    
    #Directamente en una impresion
    
    print(f"la multiplicacion en te {num1} y {num2} es {multiplicar(num1,num2)}")  
    
    producto=multiplicar(num1,num2)
    if producto<50:
        print("El producto es menor que 50")
    else:
        print("El producto es menor que 50")
#parametros
