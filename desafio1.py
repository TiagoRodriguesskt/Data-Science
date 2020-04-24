#!/usr/bin/env python

#DESAFIO PYTHON
#Tendo como dados de entrada a altura de uma pessoa.
#Construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
#Essa formula (72.7 * altura) - 58 eh para calculo mausculino


sexo = int(input('Escolha: 1-Masculino  2-Feminino: '))
h = float(input('Altura:'))
peso = float(input('Peso:'))

peso_ideal = (72.7*h) - 58 if sexo == 1 else (62.1*h) - 44.7

if peso < peso_ideal:
        print('Abaixo do peso ideal!')
elif peso == peso_ideal:
        print('Dentro do peso ideal!')
else:
        print('Acima do peso ideal!')
print ('Peso: %.2f / Peso ideal: %.2f' %(peso, peso_ideal))


