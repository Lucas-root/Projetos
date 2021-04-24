'''
	By lucasedux0@gmail.com
'''
# Este jogo é um Jogo da forca de terminal que escolhe uma palavra de um 
# arquivo txt

# importa a biblioteca choice (ultilizada para escolher um item de uma lista)
# depois le o txt salva as suas palvras em uma lista e a variavel palavra recebe
# um choice da lista de palavras
from random import choice

arquivo = open('words.txt', 'r')
lista_palavras = arquivo.read()
lista_palavras = lista_palavras.split()
arquivo.close()

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
disponiveis = alfabeto
palavra = choice(lista_palavras) 
letras_disponiveis = palavra # armazena as letras da palavra que estão disponiveis
tentativas = 8
foram = [] # armazena as letras que o usuario já digitou tanto as corretas como as não
complemento = '' # armazena a string com a formatação correta de foram

# esta variavel armazena no formato {0:['letra_da_pavalra':'_']}
# a estrutura da forca sendo a key do dict um numero que vai de 0 até o 
# tamanho da palavra no valor a primeira letra é a letra que ele faz referencia
# e a segunda str começa com um '_' mas quando o úsuario acerta a letra ele muda
# para a letra
estrutura = {}
conta = 0

# cria a estrutura da forma que será ultilizada
for letra in palavra:
	estrutura[conta] = [letra, '_']
	conta += 1

def imprime():
	'''
	imprime corretamente a variavel estrura
	'''
	string = ''
	for item in estrutura:
		string += estrutura[item][1]
	return string
		
while True:
	
	if tentativas == 0:
		print('\nQue pena! suas tentativas acabaram')
		print('A parlavra era : {}\n'.format(palavra))
		break
	elif letras_disponiveis == '':
		print('\nParabéns! você finalizou o jogo!')
		print('A palavra completa ficou {}\n'.format(imprime()))
		break
	# se foram não estiver vazia complemento recebe as letras que o usuario já 
	# tentou no formato 'a-b-c-d'...
	if foram != []:
		complemento = ''
		for letra in foram:
			complemento += str(letra)+'-'
		if complemento[-1] == '-':
			complemento = complemento[:(len(complemento)-1)]
	print('\n'+'-='*20)
	print('Tentativas :',str(tentativas)+'\t\tjá foram : '+complemento)
	print('Tente acertar a palavra :',imprime())
	print('\n'+'-='*20)

	letra = input('Digite uma letra : ')

	# true se oque o usuario digitar não for uma letra (por exemplo um simbolo)
	# obs : ele verifica as letras da variavel (alfabeto) que não é alterada
	if not letra in alfabeto:
		print('\nDigite Somente letras!\n')
		continue
	elif letra in foram:
		print('\nEsta letra já foi TENTE OUTRA!')
	elif not letra in palavra:
		print('\nEstá palavra não contem está letra')
		foram.append(letra)
		tentativas -= 1
	
	# se letra estiver em letras disponiveis ele remove a letra da variavel
	# letras disponiveis, remove 1 de tentativas, adiciona a letra que o úsuario
	# acabou de digitar a lista foram, e altera o '_' do estrutura[item][1] para 
	# a letra que o usuario digitou assim na hora que for ser impresso a estrutura
	# com a função imprime a letra que o úsuario digitou não será mais um traço
	elif letra in letras_disponiveis:
		letras_disponiveis = letras_disponiveis.replace(letra, '')
		foram.append(letra)
		disponiveis = disponiveis.replace(letra, '')
		for item in estrutura:
			if estrutura[item][0] == letra:
				estrutura[item][1] = letra

				
				
		

	
	
