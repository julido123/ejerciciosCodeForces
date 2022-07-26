s=input("")#Primera plabra
t=input("")#Segunda plabra
posiblesCambios=int(input())
listaPosibilidades=[]
i=0
precio=0
while i<posiblesCambios:
    opcion=input("")
    listaPosibilidades.append(opcion)
    i+=1

listaS=list(s)
listaT=list(t)

resultado="-1"

if s==t:
    print("0")
    print(t)
elif len(s)!=len(t):
    print(resultado)
else:
    for x in range(len(listaS)):
        if listaS[x]!=listaT[x]:        
            for i in listaPosibilidades:
                    suma=0
                    """for u in listaPosibilidades:
                        if i[0:3]==u[0:3]:
                            f"""
                    #if listaS[x]==i[0] and listaT[x]==i[0]
                    if listaS[x]==i[0]:        
                        if i[2]==listaT[x]: 
                            listaS[x]=listaT[x]
                            if len(i)==5:
                                suma=int(i[4])
                            if len(i)==6:
                                suma=int(str(i[4])+str(i[5]))
                            if len(i)==7:
                                suma=int(str(i[4])+str(i[5])+str(i[6])) 
                    if listaT[x]==i[0]:
                        if i[2]==listaS[x]:
                            listaT[x]=listaS[x]
                            if len(i)==5:
                                suma=int(i[4])
                            if len(i)==6:
                                suma=int(str(i[4])+str(i[5]))
                            if len(i)==7:
                                suma=int(str(i[4])+str(i[5])+str(i[6])) 
                    precio+=int(suma)
    if listaS==listaT:
        resultado=""
        for x in listaS:
            resultado+=x
        
        print(str(precio))
        print(resultado)  
    else:
        print(resultado)        



