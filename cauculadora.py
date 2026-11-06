# Exemplo 1 
print ("Calcularoda simples")
ni = 10 // 3
print('10 // 3 =', ni)
ni = 10 % 3
print ('10 % 3 =', ni)
nr = 2.34 * 3.58
print('2.34 * 3.58 =', nr)
nr = 2.99 / 4.1
print ('2.99 / 4.1 = ', nr)

print ('-------------')

# Exemplo 2
n1 = int(input('Digite um numero:= '))
n2  = int (input ('Digite um segundo numero:='))

n3 = n1 + n2
print ('A soma dos numero que você escolheu é = ', n1,'+',n2,'=',n3)

n4 = n1 - n2 
print ('A diferença dos numero que você escolheu é = ', n1,'-',n2,'=',n4)

n5 = n1 * n2
print ('A multiplicação dos numero que você escolheu é = ', n1,'*',n2,'=',n5)

n6 = n1 / n2 
print ('A divisão dos numero que você escolheu é = ', n1,'/',n2 ,'=',n6)

n7 = n1 % n2
print ('O resto da divisão dos numero que você escolheu é = ', n1,'/',n2 ,'=',n7)

n8 = n1 ** n2 
print ('o valor da potencia dos numero que você escolheu é = ', n1,'^',n2 ,'=',n8)

n9 = n1 // n2
print ('A dvisão inteira dos numero que você escolheu é = ', n1,'/',n2 ,'=',n9)


# Exemplo 3 

n1 = int(input("\nInforme um número: "))
n2 = int (input("Informe outro número: "))

p = (n1 > n2)
q = (n1 != n2)

r = not (p or q ) and (not p)

print('p =', p )
print('q =', q )
print('r =', r )