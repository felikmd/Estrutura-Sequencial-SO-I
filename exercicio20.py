import math

a=float
b=float
c=float
delta=float
x1=float
x2=float

a=float(input("Digite o valor A: "))
b=float(input("Digite o valor B: "))
c=float(input("Digite o valor C: "))
delta = ((b * b) - 4 * a * c )
if (delta > 0):
    x1 = ((-b) + (math.sqrt(delta)) / (2*a))
    x2 = ((-b) - (math.sqrt(delta)) / (2*a))
    print ("A primeira raiz é: ",x1)
    print ("A segunda raiz é: ",x2)
else:
        print ("Não tem raizes reais.")