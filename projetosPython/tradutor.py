traducoes = {
	'melon':'melão'
}

def traduzir(palavra):
	formatado = palavra.lower()
	verifica = formatado in traducoes
	if verifica:
		print('\nA tradução de {} é : \n'.format(palavra))
		print(traducoes[formatado])
		print()
	elif verifica == False:
		print('\nEu não possuo está palavra em meu banco de dados\n')
	else:
		print('Algum erro ocorreu!')


controle = 0

while controle == 0:
	entrada = input('Digite a palavra a ser traduzida : ')
	traduzir(entrada)

	while True:	
		novamente = input('Deseja traduzir outra palavra ? (S/n)')
		if novamente == 'n':
			controle += 1
			break 
		elif novamente == 's' or novamente == '':
			break
		else:
			print('Digite uma resposta valida')


