def verifica_formato(cpf_):
	"""
	verifica o formato do cfp caso ele verifique que o cpf está em um formato
	invalido como ---2342..23 por exemplo ele retorna False
	o primeiro if ele verifica se existe um '-' no cpf se tem
	ele verifica se o '-' esta na unica posição que ele pode ficar o cpf[::-3]
	o segundo if verifica se existe algum '.' no cpf se True 
	ele verifica se este '.' esta na 3 ou na 7 posição se não estiver em uma das duas 
	posições ele retorna False
	"""
	if '-' in cpf_:
		if not cpf_.count('-') == 1:
			print('Este CPF possui muitos "-"')
			return False
		elif cpf_[-3] != '-':
			print('CPF fora dos formatos permitidos')
			return False
	if '.' in cpf_:
		if not cpf_.count('.') in (2, 1):
			print('Este cfp possui muitos "."')
			return False	
		elif cpf_.count('.') == 1:
			if not (cpf_[3] == '.' or cpf_[7] == '.'):
				print('Este CPF esta fora de formato')
				return False
			elif not (cpf_[3] == '.' and cpf_[7] == '.'):
				print('Este cpf está fora de formato')
				return False
				
	return True

def verifica_quantidade(cpf_):
	"""
	formata o cpf. Ele retira os '.' e '-' e verifica se a quantidade de números 
	é == 11 se for retorna 11 se não False
	"""
	global final
	final = cpf_
	if '-' in final:
		final = final.replace('-', '')
	if '.' in final:
		final = final.replace('.', '')
	if not len(final) == 11:
		print('Este cpf possui mais ou menos que 11 números')
		return False
	return True

def verifica_digitos(cpf_):
	"""
	verifica se não foi digitado nenhuma letra ou 
	caractere especial invalido
	caso ele encontre algun caractere invalido ele retorna False
	se ele não encontrar caracteres invalidos ele retorna True
	esta função tambem chama a função verifica_formato() que verifica o formato d0 cfp
	"""
	alfabeto = 'abcdefghijklmnopqrstuvwxyz'
	especiais = '1234567890.-'

	for al in alfabeto:
		for dig in cpf_:
			if al == dig:
				print('letras não são permitidas')
				return False
	for carc in cpf_:
		if not carc in especiais:
			return False
	if not verifica_formato(cpf_):
		return False
	if not verifica_quantidade(cpf_): 
		return False
	# só vai retornar True se passar pelos outros passos
	return True

while True:

	cpf = input('Digite o seu CPF : ').lower().strip()

	# variavel de controle ultilizada pelas ultimas linhas
	fcon = 0
	# se verifica digitos retornar False
	if not verifica_digitos(cpf):
		print('Caracter invalido')
		print('Apenas números, "." e "-" são permitidos')
		print('Tente com outro cpf')
		continue
	sem_digito = final[0:9] 
	primeira_conta = 0
	contr = 11
	for i in sem_digito:
		contr -= 1
		primeira_conta += int(i)*contr
	digito_1 = (primeira_conta * 10)%11
	if digito_1 == 10:
		digito_1 = 0

	contr = 12
	segunda_conta = 0
	com_digito = final[0:9]+str(digito_1)
	for a in com_digito:
		contr -= 1
		segunda_conta += int(a)*contr
	digito_2 = (segunda_conta * 10) % 11
	
	cpf_final = final[0:9] + str(digito_1) + str(digito_2)
	
	print()

	if final == cpf_final:
		print('Este é um cpf valido.\n')
	else:
		print('Este cpf NÃO é valido.')
	
	while True:
		print('\nDigite "S" ou "N"\n')
		novamente = input('Você deseja tentar com outro cpf ? ').strip().lower()
		if novamente == 's':
			break
		elif novamente == 'n':
			fcon = 1
			break
		else:
			print('Digito inválido!')
	if fcon == 1:
		break
print('Fim do código\n')

		
	
