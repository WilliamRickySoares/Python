# Desafio 026
# Faça um programa que leia uma frase pelo teclado e mostre:
# a. Quantas vezes aparece a letra "A";
# b. Em que posição ela aparece a primeira vez;
# c. Em que posição ela aparece a última vez;

frase = input('Escreva uma frase: ').strip()
frase = frase.lower()
print('A letra "A" aparece {} vezes'.format(frase.count('a')))
print('A primeira letra "a" aparece na posição {}'.format(frase.find('a')))
print('A última vez que a letra "a" aparece é na posição {}'.format(frase.rfind('a')))
