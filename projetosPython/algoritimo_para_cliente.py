
alunos = []
posicao = 1

while True:

	print(f'\ndigite o nome do {posicao}º aluno a ser adicionado, ou digite "sair" para sair.\n')
	adicionar = str(input('aluno: '))

	if adicionar in ('sair', 'exit'):
		break

	elif adicionar in alunos:
		print('\nEste aluno ja foi adicionado! se quiser adionar outra pessoa\ncom um mesmo nome, complemente com o seu sobrenome')

	elif adicionar == '':
		print('\nPor favor digite algo')

	else:
		alunos.append(adicionar)
		posicao += 1
	


duplas = []
nao_foram = alunos[:]
atual = 0

dic_alunos = {}

while atual < len(alunos):
	nao_foram = nao_foram[1:]
	dic_alunos[alunos[atual]] = []

	for aluno in nao_foram:
		dic_alunos[alunos[atual]].append(aluno)
		duplas.append((alunos[atual], aluno))
	atual += 1

print(duplas)
print()
print(dic_alunos)

rodadas = []

for ix in range(1, 15+1):
	rodadas[str(ix)] = []

	for d in duplas:
		if d[0] or d[1] not in rodadas[]










