'''
Tendo como dado de entrada a altura (h) de uma pessoa,
 construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''

sexo = input("Informe seu gênero(M ou F): ")

altura = float(input("Informe sua altura: "))


if sexo == 'M':
    pesoIdeal = (72.7*altura) - 58
else:
    pesoIdeal = (62.1*altura) - 44.7


print(f"Seu peso ideal é de {pesoIdeal:.2f}")