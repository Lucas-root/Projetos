from time import sleep

path = input('Digite o path do usuario: ')

conteudo = []

while True:

	usuario = open(path, 'r')
	alteracao = usuario.readlines()

	if len(conteudo) < len(alteracao):
		for m in alteracao[len(conteudo):]:
			print(m)
		conteudo = alteracao
		alteracao = []
		sleep(0.5)

