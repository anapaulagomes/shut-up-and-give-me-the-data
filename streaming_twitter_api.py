import simplejson as json
from TwitterAPI import TwitterAPI

"""
Para utilizar a biblioteca TwitterAPI voce instalar atraves do comando: pip install TwitterAPI
ou pode fazer o clone pelo GitHub https://github.com/geduldig/TwitterAPI

Para criar uma aplicacao do Twitter eh  necessario ter uma conta no Twitter com um numero de telefone cadastrado.
Depois de logado na conta, criar uma aplicacao em https://apps.twitter.com > Create New App

Apos criar o app, na tela de detalhes da aplicacao, para acessar as chaves voce deve clicar
em Keys and Access Token. Para gerar o token, nesta mesma aba clique em Create Access Token.
"""
twitter_api = TwitterAPI(consumer_key='XXXX',
                      consumer_secret='XXXX',
                      access_token_key='XXXX',
                      access_token_secret='XXXX')

"""
Os tweets podem ser trazidos de acordo com parametros escolhidos pelo usuario.
Exemplo: localizacao, termos, linguagem.
https://dev.twitter.com/streaming/overview/request-parameters
"""
parametros = {'track':'pizza'}

"""
stream.status_code indica o codigo da conexao.
Os codigos podem ser visto aqui: https://dev.twitter.com/overview/api/response-codes
"""
print stream.status_code #status da conexao

for item in twitter_api.request('statuses/filter', parametros):
    print item['text']#imprime o texto do tweet