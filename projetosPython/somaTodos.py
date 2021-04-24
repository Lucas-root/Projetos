# algoritimo para ler um número e imprimir a soma de todos os numeros
#que o compoem ex : entrada 6 
#o algoritimo cai somar os números de 1 ate 6 (1+2+3+4+5+6)
#saida >>> 21

controle = 0
while controle == 0:
	numero = float(input('Digite o número a ser verificado : '))
	porcento = (numero / 2) + 0.5
	print('\nA soma de todos os algarismos deste número é : \n')
	print(numero * porcento)
	print()

	novamente = input('Deseja tentar com outro ? (S/n)')
	if novamente.lower() == 's' or novamente == '':
		continue
	elif novamente.lower() == 'n':
		print('\nFim do código\n')
		controle += 1
	else:
		print('Digite algo valido')

