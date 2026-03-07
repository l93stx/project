import requests as r
import pprint
result = r.get('https://api.github.com/events')
pprint.pprint(result.json())