nota = int(input ('Digite a nota tirada neste semestre: '))
if (nota >= 60):
    print("APROVADO")
else:
    print ('REPROVADO')

print ('----------------------------')

nota1 = int (input('Digite aqui sua nota neste 2° Semestre:'))

if (nota1 >= 60):
    print('APROVADO')
elif(nota1 < 60 and nota1 >= 40):
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')