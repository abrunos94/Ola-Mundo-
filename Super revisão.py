# SUPER REVISÃO - PYTHON MUNDO 1

# Neste projeto será demonstrado e explicado as principais funções.
# Serão mostradas linhas de código (basta remover o "#" dos comentários para executar)

# ---------------------------------------------------------
# MÓDULO 1 - Entrada e saída de variáveis:
# ---------------------------------------------------------

nome =  input('Qual seu nome? ')
#idade = input('Quantos anos você tem? ')

# Duas formas de formatar strings:
# print('Olá {}! Você tem {} anos!'.format(nome, idade))
# print(f'Olá {nome}! Você tem {idade} anos!')

# EXEMPLO:
# Entrada: nome = Alex, idade = 30
# Saída: Olá Alex! Você tem 30 anos!

# ---------------------------------------------------------
# MÓDULO 2 - Tipos Primitivos e Conversão de Tipos
# ---------------------------------------------------------
# Tipos primitivos, segue abaixo alguns exemplos de primitivos:
# int: numeros inteiros ( 10, -4);
# float: numeros com casas decimais (3.14, 9.8888....)
# str : texto ou caracteres ("texto")
# boll : valores boleanos ( logico), (True, False)
# Exemplo:
idade = int(input(' Quantos anos voce tem? ')) # int mostra que o numero é inteiro.
altura = float(input(' Qual sua altura? ')) # float aqui pede numeres decimais
str(print(' Seu nome é {}, voce tem {}, e sua altura é {}.' .format(nome, idade, altura)))
str(print(f'Seu nome é {nome}, voce tem {idade} e sua altura é {altura}'))
