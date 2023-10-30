#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

i=0
somaNotas=0
while i<4:
    nota= float(input("Informe a nota: "))
    somaNotas+=nota
    i+=1

somaNotas= somaNotas/4

print("A media de notas eh: ",somaNotas)


