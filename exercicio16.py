#declaraçao de varivel
horastra=float
valorhora=float
valordesc=float
numerodep=float
salario=float
salarioliq=float

#inicio
horastra=float(input("digite o numero de horas trabalhadas: "))
valorhora=float(input("digite o valor do salario a hora: "))
valordesc=float(input("digite o valor de desconto: "))
numerodep=float(input("digite o numero de dependentes: "))
salario=(horastra*valorhora)
salarioliq=(salario-valordesc) + (numerodep * 100)
print ("esse é o seu salario desse mes: ", salarioliq)
#fim