n=int(input("ingrese el numero a estudio"))
if ((n>0 and n%7!=0) and (n%2==0 and n%9!=0)) or (n%2!=0 and (n>100 and n<5000)) and (n%7!=0 or n%5==0):
    print("el numero es chevere")
else:
    print("el numero no es chevere")
