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
#str(print(' Seu nome é {}, voce tem {}, e sua altura é {}.' .format(nome, idade, altura)))
#str(print(f'Seu nome é {nome}, voce tem {idade} e sua altura é {altura}'))

# ---------------------------------------------------------
# Módulo 3 — Operadores Aritméticos
# ---------------------------------------------------------
#Aprederemos agora como funciona os operadores aritmetico e como ele spodem nos ajudar!
#| Operador | Função           | Exemplo  | Resultado |
#| -------- | ---------------- | -------- | --------- |
#| `+`      | Adição           | `2 + 3`  | `5`       |
#| `-`      | Subtração        | `5 - 2`  | `3`       |
#| `*`      | Multiplicação    | `4 * 2`  | `8`       |
#| `/`      | Divisão real     | `7 / 2`  | `3.5`     | A divisão / sempre retorna float (número com ponto).
#| `//`     | Divisão inteira  | `7 // 2` | `3`       | O operador // ignora as casas decimais (divisão inteira).
#| `%`      | Resto da divisão | `7 % 2`  | `1`       | O operador % é usado para verificar divisibilidade, paridade, etc.
#| `**`     | Potência         | `2 ** 3` | `8`       | A potência ** também pode ser usada para raízes
# segue abaixo exemplo:
a = float(input('Digite um numero: '))
b = float(input(' Digite um numero: '))
s = a + b
sub = a - b
mult = a * b
div = a / b
divinteira = a // b
restodadiv = a % b
pote = a ** b
print(' Olá {} ja sabemos que sua idade é {} e que sua altura é {}!' .format(nome, idade, altura))
print(f'Agora vamos ver seu conhecimento em matematica!')
print(f'Voce digitou o numero {a} e {b}, vamos ver agora suas operaçoes matematicas!.')
print('Voce digitou o numero {} e {}, vamos ver agora suas operaçoes matematicas!.'.format(a, b))
print(' A soma é {}, \n Subtração {}, \n Multiplicação {}, \n Divisão real {}, \n Divisão inteira {}, \n Resto da divisão {}, \n Potencia é {}.'
      .format(s, sub, mult, div, divinteira, restodadiv, pote ))

# ---------------------------------------------------------
# Módulo 3 —  Módulo 4 — Manipulando Textos (Strings)
# ---------------------------------------------------------
