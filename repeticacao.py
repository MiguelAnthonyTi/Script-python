print ('Fluxo de Repetição.')

atual = 0
n = int (input('Digite aqui um numero: '))
while (atual < n):
    print (atual)
    atual += 2 


print ('------------------')

soma = 0 
for cont in range (3):
    n = float(input('Digite um número: '))
    soma += n

print(soma)