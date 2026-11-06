import math
nome_completo = (input('Digite seu nome completo: '))
sobrenome = (input('Digite seu sobrenome: '))

pos = nome_completo.find(sobrenome)

if pos != -1:
    print("Seu nome começa na posição: ", pos )
else:
    print("Sobrenome não encontrado!")

n = float (input('Informe um número: '))
print('{n:.8f}'.format(n=n))

print ('---')


n = float (input('informe um numero: '))
x = n * math.pi
print('x = n * pi = ', n)
print('Teto de X =', math.ceil(x))
print('Piso de X =', math.floor(x))
print ('Log de X na base 10=', math.log(x,10))
print('Raiz de X =', math.sqrt (x))
