#  Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input(' Primeiro numero: '))
b = int(input(' Segundo valor: '))
c = int(input(' terceiro valor: '))
   # Verificando o menor!
if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<a and a<b:
    menor = c
print(' O menor valor foi: {}' .format(menor))
    # verificando o maior!
if a>b and a>c:
        maior = a
if b>a and b>c:
        maior = b
if c>a and c>b:
        maior = c
print(' O maior valor foi : {}' .format(maior))