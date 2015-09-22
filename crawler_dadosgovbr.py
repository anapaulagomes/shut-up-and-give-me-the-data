from pyquery import PyQuery as pq
import urllib
import csv

url_base = 'http://dados.gov.br'
url_procons = 'http://dados.gov.br/dataset/cadastro-nacional-de-reclamacoes-fundamentadas-procons-sindec'
url_reclamacoes_consumidor_gov = 'http://dados.gov.br/dataset/reclamacoes-do-consumidor-gov-br'
url_unidades = 'http://dados.gov.br/dataset/unidades-dos-procons'

def parse_pagina_html(url):
    return urllib.urlopen(url).read()

def coleta_links_fontes(url):
    pagina = pq(parse_pagina_html(url))
    lista_links = pagina('li.resource-item a.heading')
    links = [url_base + a.attrib['href'] for a in lista_links]

    return links

def coleta_url_dados(url):
    pagina = pq(parse_pagina_html(url))
    link_dado = pagina('p.ellipsis a').attr('href')
    return link_dado

def salva_arquivo(url):
    nome_arquivo = url[url.rfind('/')+1:]
    try:
        urllib.urlretrieve (url, nome_arquivo)
        return True
    except:
        print 'erro: ', url, sys.exc_info()[0]
        return False

if __name__ == '__main__':
    urls = coleta_links_fontes(url_procons) + coleta_links_fontes(url_reclamacoes_consumidor_gov) + coleta_links_fontes(url_unidades)
    for url in urls:
        url_dado = coleta_url_dados(url)
        salva_arquivo(url_dado)
