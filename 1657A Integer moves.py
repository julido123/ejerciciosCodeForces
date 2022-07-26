import math

cantidadOperaciones=int(input())
contador=0
listaOperaciones=[]

while contador<cantidadOperaciones:
    operacion=input()
    listaOperaciones.append(operacion)
    contador+=1

for elemento in listaOperaciones:

    if len(elemento)==3:
        x=int(elemento[0])
        y=int(elemento[2])
        numero=math.sqrt(pow(0-x,2)+pow(0-y,2))
        if x==0 and y==0:
            print(0)
        elif numero%1==0:
            print(1)
        else:
            print(2)
    if len(elemento)==4:
        x=int(elemento[0:2])
        y=int(elemento[2]+elemento[3])
        numero=math.sqrt(pow(0-x,2)+pow(0-y,2))
        if numero%1==0:
            print(1)
        else:
            print(2)
        
    if len(elemento)==5:
        x=int(elemento[0:2])
        y=int(elemento[3]+elemento[4])
        numero=math.sqrt(pow(0-x,2)+pow(0-y,2))
        if numero%1==0:
            print(1)
        else:
            print(2)