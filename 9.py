'''
Faça um Programa que peça a temperatura em graus Fahrenheit, 
transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
'''

temperaturaFahrenheit = float(input("Informe a temperatura em Fahrenheit: "))

temperaturaCelsius = 5 * ((temperaturaFahrenheit-32) / 9)


print(temperaturaFahrenheit," em celsius é ", temperaturaCelsius," graus")