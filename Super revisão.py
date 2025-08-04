# SUPER REVISÃO - PYTHON MUNDO 1


# Neste projeto será demonstrado e explicado as principais funções.
# Serão mostradas linhas de código (basta remover o "#" dos comentários para executar)

# ---------------------------------------------------------
# MÓDULO 1 - Entrada e saída de variáveis:
# ---------------------------------------------------------

#nome =  input('Qual seu nome? ')
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
#idade = int(input(' Quantos anos voce tem? ')) # int mostra que o numero é inteiro.
#altura = float(input(' Qual sua altura? ')) # float aqui pede numeres decimais
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
#a = float(input('Digite um numero: '))
#b = float(input(' Digite um numero: '))
#s = a + b
#sub = a - b
#mult = a * b
#div = a / b
#divinteira = a // b
#restodadiv = a % b
#pote = a ** b
#print(' Olá {} ja sabemos que sua idade é {} e que sua altura é {}!' .format(nome, idade, altura))
#print(f'Agora vamos ver seu conhecimento em matematica!')
#print(f'Voce digitou o numero {a} e {b}, vamos ver agora suas operaçoes matematicas!.')
#print('Voce digitou o numero {} e {}, vamos ver agora suas operaçoes matematicas!.'.format(a, b))
#print(' A soma é {}, \n Subtração {}, \n Multiplicação {}, \n Divisão real {}, \n Divisão inteira {}, \n Resto da divisão {}, \n Potencia é {}.'
 #     .format(s, sub, mult, div, divinteira, restodadiv, pote ))

# ---------------------------------------------------------
# Módulo 4 — Manipulando Textos (Strings)
# ---------------------------------------------------------
# Modulo importante para entender como se formata textos, colocar en maisculo ou minusculo alem de pode contar letras procurar palavras e dividir strings.

#| Método               | Função                                                          |
#| -------------------- | --------------------------------------------------------------- |
#| `len()`              | Conta o número total de caracteres da string                    |
#| `count()`            | Conta quantas vezes um caractere/aparece                        |
#| `find()`             | Informa a posição de uma substring (ou -1 se não existir)       |
#| `'palavra' in frase` | Retorna `True` ou `False` se a palavra existir ou não na string |
#| `upper()`            | Converte para MAIÚSCULAS                                        |
#| `lower()`            | Converte para minúsculas                                        |
#| `capitalize()`       | Só a primeira letra da string em maiúscula                      |
#| `title()`            | Primeira letra de cada palavra em maiúscula                     |
#| `strip()`            | Remove espaços em branco do começo e do fim                     |
#| `split()`            | Divide a string em partes (gera uma lista)                      |
#| `' - '.join()`       | Junta elementos de uma lista com o separador que você quiser    |



# Vamos praticar com uma frase simples
frase = 'Curso em Vídeo Python'

# Tamanho da frase
#print(f"Tamanho da frase: {len(frase)} caracteres")

# Quantas vezes aparece a letra 'o'
#print(f"Quantidade de letras 'o': {frase.count('o')}")

# Posição onde começa a palavra 'Vídeo'
#print(f"Posição da palavra 'Vídeo': {frase.find('Vídeo')}")

# A palavra 'Android' existe?
#print(f"A palavra 'Android' está na frase? {'Android' in frase}")

# Transformações:
#print(f"Maiúsculas: {frase.upper()}")
#print(f"Minúsculas: {frase.lower()}")
#print(f"Primeira letra de cada palavra: {frase.title()}")
#print(f"Só a primeira letra da frase: {frase.capitalize()}")

# Removendo espaços das pontas
#espacada = '   Olá mundo   '
#print(f"Sem espaços nas pontas: '{espacada.strip()}'")

# Dividindo a frase em palavras
#print(f"Dividida em lista: {frase.split()}")

# Juntando com hífen
#print(f"Juntando com hífen: {'-'.join(frase.split())}")

# Exemplo
nome = input(' Digite seu nome completo: ')
print(f' Seu  nome completo é {nome}.')
print(' Prazer {}!' .format(nome))
print('Seu nome tem {} letras!' .format(len(nome) - 4) )
print(f'Seu nome tem {(len(nome) - 4)} letras!')
print(f' Seu nome todo embletra maiscula fica assim {nome.upper()}!')
print(' Seu nome todo embletra maiscula fica assim {}!' .format(nome.upper()))
primeiro_nome = nome.split()[0]
print(f'Seu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras.')

# ---------------------------------------------------------
# Módulo Módulo 5 — Listas (Variáveis Compostas)
# ---------------------------------------------------------
