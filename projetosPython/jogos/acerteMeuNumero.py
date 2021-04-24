
# programa para adivinhar o número que o usuario pensar com as informações
# esta muito alto (h) ou esta muito baixo (l)

print('\nOlá pense em um número de 1 a 100 que eu irei adivinhar\n')

# vars que contabilizam qual o menor e qual o maior range do numero 
menor = 0
maior = 100

while True:
	print('Eu pensei no número {} está certo ? '.format((menor + maior)	/ 2))
	entrada = input('Digite "h" muito alto, "l" para muito baixo e "c" para correto : ')
	if entrada == 'l': # se o número for muito baixo será acrescentado a metade so número a var menor
		menor += ((maior + menor) / 2) / 2
	elif entrada == 'h': # se o número estiver muito alto 
		maior -= ((maior + menor) /2 ) /2 # vai ser subtraido a metade do número estipulado pelo algoritimo
	elif entrada == 'c':
		print('\nO número {} que eu pensei está correto.'.format((maior+menor) /2))
		print('\nFim de codigo\n')
	else:
		print('\nOpção invalida\n')

	
	
