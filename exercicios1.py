import math
#1 - Imprima a frase: Python na Escola de Programação da Alura.
print('Python na Escola de Programação da Alura')

#2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
nome = 'Pedro Henrique'
idade = 26

print(f'Meu nome é {nome} e tenho {idade} anos')

#3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:
c = 'Alura'

for i in c:
    print(i)
    

#4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:
print(round(math.pi, 5))








#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
numero = int(input('Digite um numero: '))

resultado = numero % 2

if resultado == 0:
    print(f'O numero {numero} é par!!!!')

else:
    print(f'O numero {numero} é impar!!!!3')


#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

idade = int(input('Digite sua idade: '))

if idade <= 12:
    print('Criança')
elif idade >=13 and idade <= 18:
    print('Adolescente')
else:
        print('Adulto')