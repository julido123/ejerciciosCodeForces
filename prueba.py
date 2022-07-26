import math
""" dato = input("Ingrese dato: ")

num = None
for conv in (int, float, complex):
    try:
        num = conv(dato)
        break
    except ValueError:
        pass

if num is None:
    print("Error de entrada")
else:
    var=type(num).__name__
    print(var)
    print(f"dato={num} (tipo: {type(num).__name__})") """
numero=math.sqrt(pow(0-9,2)+pow(0-15,2))
if numero%1==0:
    print("Es entero")
else:
    print("Nu")