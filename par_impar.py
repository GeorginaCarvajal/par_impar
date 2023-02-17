#programa para verificar números par e impar

print("-----------------------")
print("------par o impar------")
print("-----------------------")

#input
x = int(input ("digite un numero: "))

#procesing
r=x%2
if x==0:
    msj= "Par"
else:
    msj="impar"

print(" el numero" +str(r) + "es" + msj)

