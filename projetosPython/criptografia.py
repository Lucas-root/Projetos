
from sys import argv

alfabeto = [
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
	'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
	'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4',
	'5', '6', '7', '8', '9',
]

def criptografa(palavra, descriptografa=False, com_seed=False, SEED=1):
	'''
	criptografa uma palavra com a tecnica letra>>
	ex: l = m 
	se for passado True para o seu parametro, ele decriptografa
	se com_seed for True ele criptografa apartir da seed
	'''
	resultado = ''
	
	for letra in palavra:

		adicionar = ''

		if letra == ' ':
			adicionar = ' '
		elif letra not in alfabeto:
			adicionar = letra
		else:
			index = alfabeto.index(letra)
			

			if descriptografa:
				adicionar = alfabeto[index-SEED]

			else:
				# IMPORTANTE! não confundir o SEED com posicao num array
				# o SEED se refere a casas 
				# caso index se refira a ultima letra adicionar recebe a
				
				if index == len(alfabeto)-1:
					adicionar = alfabeto[SEED-1]
				else:
					#SEED-(len(alfabeto)-1)-1
					adicionar = alfabeto[(SEED-1)-((len(alfabeto)-1)-index)]
					'''
					if index+SEED > len(alfabeto)-1:
						#(len(alfabeto)-1)-index
						adicionar = alfabeto[SEED]
					else:
						adicionar = alfabeto[index + SEED]
					'''
		
		resultado += adicionar
	
	return resultado

def criptografa_documento(path_original, path_final, descriptografa=False, com_seed=False, SEED=1):

	arquivo = open(path_original, 'r')	

	lista_palavras = []
	palavras_criptografadas = []

	for linha in arquivo:
		lista_palavras.append(linha)

	for p in lista_palavras:
		palavras_criptografadas.append(criptografa(p, descriptografa, com_seed, SEED))

	arquivo.close()
	arquivo = open(path_final, 'w')

	for p in palavras_criptografadas:
		arquivo.write(p)

def verifica_arquivos(arquivo):
	try:
		open(arquivo)
		return 0
	except:
		return 1

def pega_arquivo_original():
	while True:
		arquivo_original = input('\nDigite o path do arquivo_original: ')
		if verifica_arquivos(arquivo_original) == 0:
			print('\nEste arquivo não exite! Digite novamente!')
		else:
			return arquivo_original 

def pega_arquivo_final():
	while True:
		arquivo_final = input('\nDigite o path do arquivo_final: ')
		if arquivo_final not in ('', ' '):
			return arquivo_final
		else:
			print('\nDigite um valor valido!')
		

def colhe_informacoes():
	"""
	Pega os parametros passados ao executar o arquivo
	"""
	# caso não seja passados parametros

	if len(argv) > 3:
		print('Foram passados argumentos de mais!')	
		while True:
			opcao = input(f'\nVocê deseja ultilizar {argv[1]} como arquivo_original? ("SIM"/"não"): ').lower()
			if opcao in (' ', '', 'sim', 's'):
				arquivo_original = argv[1]
				break
			elif opcao in ('n', 'não', 'nao'):
				arquivo_original = pega_arquivo_original
				break
			else:
				print('\nNão entendi! Tente novamente!')
		while True:
			opcao = input(f'\nVocê deseja ultilizar {argv[2]} como arquivo_final? ("SIM","não"): ').lower()
			if opcao in ('s', 'sim', '', ' '):
				arquivo_final = argv[2]
				break
			elif opcao in ('n', 'não'):
				arquivo_final = pega_arquivo_final()
				break
			else:
				print('\nNão entendi! Tente novamente!')

	elif len(argv) > 1:
		if verifica_arquivos(argv[1]) == 1:
			print(f'\nO arquivo {argv[1]} não existe!')
			arquivo_original = pega_arquivo_original()
		else:
			arquivo_original = argv[1]

	elif len(argv) == 1:
		arquivo_original = pega_arquivo_original()
	
	if len(argv) == 3:
		arquivo_final = argv[2]
	elif len(argv) < 3:
		arquivo_final = pega_arquivo_final()
	
	return arquivo_original, arquivo_final

def main():
	
	arquivo_original, arquivo_final = colhe_informacoes()

	while True:
		print('\nVocê deseja criptografar ou descriptografar o documento?')
		print('Digite (1) para criptografar')
		print('Digite (2) para descriptografar')
		opcao = input('Digite uma opção: ')

		if opcao == '1':
			descriptografar = False
			break
		elif opcao == '2':
			descriptografar = True
			break
		else:
			print('\nDigite uma opção valida!')
	
	com_seed = False
	while True:
		if descriptografar:
			opcao = input('\nDeseja descriptografar apartir de uma SEED? ("sim/NÃO"): ').lower()
		else:
			opcao = input('\nDeseja criptografar apartir de uma SEED? ("sim/NÃO"): ').lower()
		if opcao not in ('sim', 's', 'nao', 'não', 'n', '', ' '):
			print('\nDigite um valor valido!')
			continue
		break

	if opcao in ('sim', 's'):
		com_seed = True
		while True:
			SEED = input('\nDigite uma SEED: ')
			if not SEED.isnumeric():
				print('\nDigite apenas números!')	
			else:
				SEED = int(SEED)

				print('SEED antes =', SEED)
				while SEED > len(alfabeto):
					SEED -= len(alfabeto)
				print('SEED depois: ',SEED)
				break
	else:
		SEED = 1
	
	while True:
		# somente para não precisar copiar e colar o bloco duas vezes
		if descriptografar:
			operacao = 'descriptografar'
		else:
			operacao = 'criptografar'

		print(f'\nVocê tem certeza que deseja {operacao} o documento {arquivo_original}')
		print(f'E salvar as alterações em {arquivo_final}?')
		opcao = input('Digite "sim" para continuar ou "Não" para cancelar (padrão:Não): ').lower()
		if opcao in ('não', 'n', 'nao', '', ' '):
			print('\nOperação cancelada.')
			return 1
		elif opcao in ('s', 'sim'):
			break
		else:
			print('\nNão entendi! Tente novamente')
	# caso seja passado True para descriptografar ele reverte
	criptografa_documento(arquivo_original, arquivo_final, descriptografar, com_seed, SEED)
	print(f'\nSucesso! Operação {operacao} realizada em ({arquivo_original}) e gravada em ({arquivo_final}).')	

if __name__ == '__main__':
	main()


