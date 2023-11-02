'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
1. o produto do dobro do primeiro com metade do segundo .
2 .a soma do triplo do primeiro com o terceiro.
3. o terceiro elevado ao cubo.
'''
numero1=int(input("Informe o primeiro número inteiro"))

numero2 =int(input("Informe o segundo número inteiro"))

numeroReal =float (input("Informe o número real"))

a = (2*numero1) - (numero2/2)

b  = 3*numero1+numeroReal

c = numeroReal**3

print(f"A é igual {a}")
print(f"B é igual {b}")
print(f"C é igual {c}")


