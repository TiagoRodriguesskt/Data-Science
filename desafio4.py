# DESAFIO CONDICIONAIS
# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

#!/usr/bin/env python
nome = str(input('Qual seu nome? '))

turno = str(input('Em qual turno que você estuda? M=manha, T=tarde ou N-noite: ').upper())

if turno == 'M':
    print('Bom dia,', nome,'!')

elif turno == 'T':
    print('Boa tarde,', nome,'!')

elif turno == 'N':
    print('Boa noite,', nome,"!")

else:
    print('Valor inválido!')

