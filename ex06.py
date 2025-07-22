# Mostre para mim o antecessor e o sucessor de um numero.
n = int(input("Digite um numero:"))
Antecessor = n - 1
Sucessor = n + 2
print("O antecessor de {} é {} e seu sucessor é {}" .format(n, Antecessor, Sucessor))
print("O antecessor de {} é {} e seu sucessor é {}" .format(n,(n-1), (n+2)))
# Nesse ultimo print podemos notar que no .format  somente identifiquei o n.