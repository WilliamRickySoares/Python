# Desafio 026
# Faça um programa que leia uma frase pelo teclado e mostre:
# a. Quantas vezes aparece a letra "A";
# b. Em que posição ela aparece a primeira vez;
# c. Em que posição ela aparece a última vez;

frase = str(input('Escreva uma frase: ')).strip()
fraseLower = frase.lower()
print('A letra "A" aparece {} vezes'.format(fraseLower.count('a')))
print('A primeira letra "a" aparece na posição {}'.format(fraseLower.find('a')+1))
print('A última vez que a letra "a" aparece é na posição {}'.format(fraseLower.rfind('a')+1))
