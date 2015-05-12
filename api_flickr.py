import flickrapi
import simplejson as json
import sys

"""
Script para coletar fotos do Flickr. Utilizamos a API FlickrAPI.
Eh necessario criar um app na plataforma do Flickr para obter as chaves de acesso.
Voce pode criar em: https://www.flickr.com/services/apps/create/

"""

chave = "4f35fb147cdbb468994415064c16a5fa"
segredo = "15ec63a9edec6623"

"""
Com as suas chaves de acesso, faz a autenticacao na API, passando tambem o formato de retorno das requisicoes.
"""
def autenticacao(chave, segredo):
	return flickrapi.FlickrAPI(chave, segredo, format='json')

"""
Este metodo busca as fotos baseado nas coordenadas e nas imagens que contem dados geograficos.
Os demais metodos da API podem ser consultados aqui: https://www.flickr.com/services/api/
"""
def busca_fotos(coordenadas, pagina, flickr):
	fotos = flickr.photos.search(bbox=coordenadas,has_geo=1, page=pagina)#date_upload=data
	return fotos

"""
Carrega o retorno da API em um formato JSON que possa ser manipulado no codigo.
Aqui voce pode criar estruturas para buscar varias fotos, incrementando numeros das paginas.
"""
def coleta(coordenadas, flickr):
	fotos = busca_fotos(coordenadas, 1, flickr)
	fotos_json = json.loads(fotos)#primeira pagina - necessaria para consultar tambem quantas estao disponiveis - 250 fotos por pagina

	#print fotos_json['photos']# todas as informacoes
	paginas = fotos_json['photos']['pages']#numero de paginas
	numero_fotos = fotos_json['photos']['total']#numero total de fotos
	print numero_fotos, "fotos em", paginas, "paginas."

def main():
	flickr = autenticacao(chave, segredo)
	coordenadas = "-44.1308,-20.1243,-43.7475,-19.7659"
	coleta(coordenadas, flickr)
	
if __name__ == '__main__':
	main()