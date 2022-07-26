import math
x=int(input(""))
y=int(input(""))
mayor=int
d=int
 
while((x<1 or y<1)or (x>6 or y>6)):
    if x<1 or x>6:
        print("")
        x
    if y<1 or y>6:
        print("")
        y
 
if y<=x:
    mayor=x
else:
    mayor=y
 
 
d=7-mayor
a = math.gcd(d,6)
 
print(str(int(d/a)),"/",str(int(6/a)),sep='')
