'''By <lucasedux0@gmail.com> este programa precisa ser melhorado muito ainda !
'''

alfabeto = 'abcdefghijklmnopqrstuvwxyz' # o alfabeto completo serve para a função gerador() ultilizala

#recebe a palavra e a formata (retira os possiveis espaços nos lados e joga ela para lower)
palavra = input('Digite uma palavra para ver qual \né a sua maior precedencia  alfabetica : ')
palavra = palavra.lower()
palavra = palavra.strip()

def gerador(alterar): # está função recebe uma palavra e retorna uma lista de todas as suas possibi-
	tamanho = len(alterar) #...-lidades de ordem alfabetica

	ultimo = len(alterar)-1 

	possiveis = [] # variavel onde será armazenada localmente todas as possibilidades
	letra = 0
	inicial = 2 
	loop = 0

	while loop <= ultimo:
		
		loop += 1
		for i in range(tamanho): # algoritimo para gerar as possibilidades e armazenar na lista
			if i == 0: # se for a primeira execução do for ele reseta a v controle
				controle = inicial
				possiveis.append(alterar[letra])
			if controle <= tamanho:
				possiveis.append(alterar[letra:controle])
				controle += 1
		inicial += 1
		letra += 1
	return possiveis	

alpha_possi = gerador(alfabeto)
palavra_possi = gerador(palavra)

len_palavra = len(palavra_possi)
conta = 0

maior = 0
qual = '' 

for i in range(len_palavra): # verifica qual precedencia na lista de precedencias alfabeticas é maior
	if palavra_possi[i] in alpha_possi:
		if len(palavra_possi[i]) > maior:
			maior = len(palavra_possi[i])	
			qual = palavra_possi[i] # a palavra que for maior é gravada na variavel (qual)

print('A maior precedencia alfabetica desta palavra é {}'.format(qual))


			
