fila=input("") #Se ingresa el número de filas y columnas
matriz=[]
mal=""
i=0

if len(fila)==3:
    while i<int(fila[0]):
        colores=input("")
        matriz.append(colores)
        i+=1
    
if len(fila)==4:
    fil=int(fila[0:2])
    while i<int(fil):
        colores=input("")
        matriz.append(colores)
        i+=1

if len(str(fila))==5:
    if fila[1]==" ":
        fil=fila[0]
    else:
        fil=fila[0:3]
    while i<int(fil):
        colores=input("")
        matriz.append(colores)
        i+=1

if len(fila)==6:
    fil=int(fila[0:3])
    while i<int(fil):
        colores=input("")
        matriz.append(colores)
        i+=1

if len(fila)==7:
    fil=int(fila[0:4])
    while i<int(fil):
        colores=input("")
        matriz.append(colores)
        i+=1


for x in matriz:
    confirmacion=""
    for j in range(len(x)):
        if x[j]==x[j-1]:
            confirmacion+="1"
    if len(confirmacion)!=len(x):
        mal="1"

for u in range(len(matriz)-1):
    if matriz[u]==matriz[u+1]:
        mal="1"

if mal=="1":
    print("NO")
else:
    print("YES")
