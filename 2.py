nota1=float(input("ingrese la primera nota"))
n1=(nota1*0.1)
nota2=float(input("ingrese la segunda nota"))
n2=(nota2*0.15)
nota3=float(input("ingrese la tercera nota"))
n3=(nota3*0.25)
nota4=float(input("ingrese la cuarta nota"))
n4=(nota4*0.15)
nota5=float(input("ingrese la quinta nota"))
n5=(nota5*0.35)

nf=(n1+n2+n3+n4+n5)

if nf >=3.0:
	if nf>4.5:
		print("felicidades su nota es superior y es:  " , nf)
	else:
		print("aprobo mi materia pero puede mejorar y su nota es:  " , nf)

else:
	if nf <2.0:
		print("no puede habilitat mi mayeria y su nota es: ", nf)
	else:
			print("no aprobo y debe habiliyar esta materia y su nota es: " , nf)
