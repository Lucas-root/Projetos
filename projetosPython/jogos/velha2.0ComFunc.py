# Esta é a tentativa de rescrever o programa do jogo da velha antigo mas 
# Agora ultilizando funções, listas, tuplas e dicionários

from random import choice
from time import sleep

tabuleiro = {
	1:' ', 2:' ', 3:' ',
	4:' ', 5:' ', 6:' ',
	7:' ', 8:' ', 9:' ',
}
disponiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
possibilidades_ganhar = (
	(1, 2, 3),
	(4, 5, 6),
	(7, 8, 9),
	(1, 4, 7),
	(2, 5, 8),
	(3, 6, 9),
	(3, 5, 7),
	(1, 5, 9),
)

def escolheSimbolo():
	'''
	pergunta ao jogador qual simbolo ele irá querer "X" ou "O" e atribui o simbolo
	escolhido a jogado e outro simbolo restante a computador
	'''

	global simbolo_jogador
	global simbolo_computador

	while True:
		escolha = input('\nQual simbolo vocẽ irá querer ? (X/O) : ').lower()
		if escolha in ['x', 'o']:
			if escolha == 'x':
				simbolo_jogador = 'X'
				simbolo_computador = 'O'
				print('Ok, quem começa é você')
			else:
				simbolo_jogador = 'O'
				simbolo_computador = 'X'
				print('Você escolheu a "O" então eu começo')
			break
		else:
			print('\nSimbolo invalido! Digite apenas "X" ou "O"')
			continue
	# return de quem irá começar o jogo
	if simbolo_jogador == 'X':
		return 'jogador'
	else:
		return 'computador'

def imprime():
	'''
	Função para imprimir o tabuleiro 
	'''
	
	print(f'\t {tabuleiro[1]} | {tabuleiro[2]} | {tabuleiro[3]} ')
	print('\t-----------')
	print(f'\t {tabuleiro[4]} | {tabuleiro[5]} | {tabuleiro[6]} ')
	print('\t-----------')
	print(f'\t {tabuleiro[7]} | {tabuleiro[8]} | {tabuleiro[9]} ')

def jogadorEscolhe(simbolo):
	'''
	pergunta ao jogador qual casa ele irá jogar e altera o tabuleiro para esta 
	casa
	'''
	global disponiveis
	global tabuleiro
	while True:
		try:
			imprime()
			numero = int(input('Digite o número da casa a ser jogada : '))
			if not numero in tabuleiro:
				print('\nO tabuleiro não possui está posição! Tente novamente\n')
				continue
			elif tabuleiro[numero] != ' ':
				print('\nEstá casa já está ocupada tente outra!\n')
				continue
			else:
				try:
					tabuleiro[int(numero)] = simbolo
					disponiveis.remove(numero)
					imprime()
					break
				except:
					print(f'Algum erro ocorreu ao atribuir o "{simbolo}" a tabuleiro[{numero}]')
		except ValueError:
			print('\nDigite apenas números! Tente novamente\n')

def computadorEscolhe(simbolo_computador):
	'''
	função para o computador escolher uma casa para ele jogar
	'''
	global disponiveis
	global tabuleiro

	escolheu = choice(disponiveis)
	disponiveis.remove(escolheu)

	tabuleiro[escolheu] = simbolo_computador
	print(f'\nJoguei na casa {escolheu}\n')

def verificaGanhador():
	'''
	função para verificar se alguem ganhou o jogo
	'''
	for t in possibilidades_ganhar:
		if tabuleiro[t[0]] == ' ' or tabuleiro[t[1]] == ' ' or tabuleiro[t[2]] == ' ':
			continue	
		else:
			if tabuleiro[t[0]] == tabuleiro[t[1]] == tabuleiro[t[2]]:
				if tabuleiro[t[0]] == simbolo_jogador:
					return 'jogador'
				else:
					return 'computador'
	return 'ninguem'

def main():

	print('\n'+'-+'*20)
	print('\tJOGO DA VELHA!')
	print('-+'*20)
	print()

	print('O tabuleiro está enumerado por indices então a primeira casa \nrecebe o indice 1 e assim por diante.')
	
	comeca = escolheSimbolo()	
	vez = comeca	

	for i in range(1, 9+1):
		if vez == 'jogador':
			vez = 'computador'
			jogadorEscolhe(simbolo_jogador)
		elif vez == 'computador':
			print('\nMinha vez...')
			sleep(0.5)
			vez = 'jogador'
			computadorEscolhe(simbolo_computador)
		# obs : ele só começa avaliar apartir da 5º jogada (pois somente apartir
		# da 5º que alguem tera preenchido uma linha
		if i >= 5:
			if verificaGanhador() == 'jogador':
				print('\nPARABÉNS! você venceu!\n')
				print('Fim de jogo\n')
				break
			elif verificaGanhador() == 'computador':
				imprime()
				print('\nHEHE! Eu venci!')
				print('\nFim de jogo\n')
				break
		
	
main()	



