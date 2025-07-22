# desafio de pintura de parede
# Sabendo que 1 litro  de tinta pinta 2m²,quantos vou precisar?
l = float(input(" Digite a largura da parede: "))
a = float(input("Digite a altura da parede: "))
print(" A sua parede tem a dimensão de {}X{} e sua área é de {:.2f}m²".format(l, a, (l*a)))
print(" Para pintar essa parede voce precisara de {}litros de tinta" .format((l*a)/2))