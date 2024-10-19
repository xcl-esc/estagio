numFornecido = int(input('Digite um número:\n'))

termoSequencia = 3
num1 = 0
num2 = 1
print(f'\n{num1}\n{num2}')


while termoSequencia<= numFornecido:
    num3 = num1 + num2
    print(num3)
    termoSequencia += 1
    num1 = num2
    num2 = num3
   
listaFin = [num3]
if numFornecido in listaFin:
        print('Faz parte da sequencia de fin')