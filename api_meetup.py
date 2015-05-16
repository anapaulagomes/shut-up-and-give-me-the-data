
import requests

API_KEY = "65317b2e34322116b10b7946284e1f"

params = {'apikey': PUBLIC_KEY,'ts': ts, 'hash': m, 'limit': 100, 'offset': n}
r = requests.get('http://api.yelp.com/v2/search', params=params)
print r.url

#membros
https://api.meetup.com/2/members?&sign=true&photo-host=public&group_urlname=gdg-bh&page=20
https://secure.meetup.com/meetup_api/console/?path=/2/profiles


https://api.meetup.com/2/profiles?offset=0&format=json&group_urlname=gdg-bh&photo-host=public&page=20&order=visited&sig_id=135268292&sig=cb441d404c7427c81aec85b35395aecb5612e968

#