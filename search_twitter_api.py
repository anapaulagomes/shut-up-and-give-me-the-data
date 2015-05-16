from TwitterAPI import TwitterAPI
import simplejson as json

"""
Acesso a REST API do Twitter (search)
https://dev.twitter.com/rest/public
"""

twitter_api = TwitterAPI(consumer_key='XXXX',
                      consumer_secret='XXXX',
                      access_token_key='XXXX',
                      access_token_secret='XXXX')

resultado = twitter_api.request('search/tweets', {'q': '#python', 'lang': 'en', 'count': '10'})

for linha in resultado:
	tweet = json.dumps(linha)
	print json.loads(tweet)['text']
