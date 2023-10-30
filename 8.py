'''
Faça um Programa que pergunte quanto você ganha por hora 
e o número de horas trabalhadas no mês. Calcule e mostre 
o total do seu salário no referido mês.
'''
salarioHora = float(input("Valor recebido por hora: "))

horasTrabalhadas = int(input("Quantidade de horas trabalhadas: "))

salario = salarioHora*horasTrabalhadas

print("O salário referente a esse mês tem que ser de : R$",salario)