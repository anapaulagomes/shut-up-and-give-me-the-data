import requests
import time
import hashlib
import simplejson as json

"""
Script para coletar todos os personagens disponiveis na API da Marvel
"""

"""
Para coletar da API da Marvel voce deve se cadastrar e obter uma chave em: http://developer.marvel.com/documentation/getting_started
Com as chaves publica e privada voce deve gerar um hash a partir do horario atual.

Mais detalhes sobre o processo de autenticacao: http://developer.marvel.com/documentation/authorization
Mais detalhes sobre retornos da API: http://developer.marvel.com/documentation/apiresults
"""

PUBLIC_KEY = '2124cb975af929a3d80d511bc07dac69'
PRIVATE_KEY = '19d2d72ced9cdfcadcf1347626acfba120fc7bad'

timestamp = int(time.time())#horario atual

hash_ = hashlib.md5(str(timestamp)+PRIVATE_KEY+PUBLIC_KEY).hexdigest()

"""
Sabendo que existem ate 1500 personagens e eh possivel coletar 100 por pagina, fazemos um for para coletar todos os personagens.
"""
for n in range(0,1500,100):
	print '#',n #pagina
	parametros = {'apikey': PUBLIC_KEY,'ts': timestamp, 'hash': hash_, 'limit': 100, 'offset': n}
	r = requests.get('http://gateway.marvel.com/v1/public/characters', params=parametros)#requisicao com a autenticacao de acordo com o padrao da API
	#print r.url
	for j in json.loads(r.text)['data']['results']:
		print j['name']
