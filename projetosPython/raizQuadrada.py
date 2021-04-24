'''
	Este programa lê um número e diz a sua raiz quadrada que ele conseguiu calcular
	se as variaveis maior e menor guardam os valores relativos a maior e a menor possibilidade das raizes
	a variavel guess guarda o metade da soma da var maior com a var menor / 2 
	se guess ** 2 for maior que o numero digitado pelo usuario (entrada) a var maior recebe este guess
	se guess ** 2 for menor que a entrada digitada inicialmente pelo usuario menor recebe guess
	o while quebra quando a raiz aprocimada tiver uma taxa de erro igual ou inferior a 0.001
'''

numero = float(input('Digite um número para descobrir a sua raiz quadrada : '))
maior = 9
menor = 0
guess = 9

while abs((guess ** 2) - numero) >= 0.001:
	if guess ** 2 < numero:
		menor = guess
	elif guess ** 2 > numero:
		maior = guess

	guess = (maior + menor) / 2
raiz = (maior + menor) / 2

print('A raiz quadrada de {} é {:.5f}'.format(numero, raiz))
