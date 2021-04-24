# author : lucasedux0@gmail.com

comandos = {
	'help':'exibe todos os comandos disponiveis',
}

estoque = {
	'doces':{
		'bolachas':{
			'bel-vita':4.99,
		},
		'chocolates':{
			'barras':{
				'diamante-negro':{
					'50g':3.00,
					'100g':5.49,
				},
			},
		},
	},
	'bebidas':{
		'vinhos':{
			'vinho-branco':20.99,
		},
	},
	'laticinios':{
		'leites':{
			'terra-viva':3.49,
			'piracanjuba':4.50,
		},
		'queijos':{
			'brancos':{
				'seara':{
					'100g':5.00,
				},
			},
		},	
	},
}

print()
	
def impressao(dicionario):
	for chave in dicionario:
		if type(dicionario[chave]) == dict:
			print(chave)
			impressao(dicionario[chave])
		else:
			print('\t',chave,':',dicionario[chave])

impressao(estoque)
