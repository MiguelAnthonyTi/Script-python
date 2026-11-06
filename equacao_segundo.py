import math
print ( 'Equção de Segundo Grau ')

a = float (input('DIgite aqui o valor de A: '))
b = float (input('DIgite aqui o valor de B: '))
c = float (input('DIgite aqui o valor de C: '))

if a == 0 :
    print ('Não é uma equação de Segundo Grau. Pois A tem que ser exatamente diferente de 0')
else:
    delta = b**2 - 4 * (a * c)
    if (delta < 0):
        print('A equação não tem Raizes')
    elif (delta == 0):
        x1= b * (-1)/2 *a 
        print ('Equação possui raiz: ', x1, '')
    else:
        raiz_delta = math.sqrt(delta)
        x1 =(b * (-1) + raiz_delta)/2*a
        x2 =(b * (-1) - raiz_delta)/2*a

        print('A equação possuiu raizes: ')
        print('x1 =', x1)
        print('x2 =', x2)