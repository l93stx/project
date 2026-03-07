from api_proxy import get_top_headlines
import pprint

if __name__ == '__main__':
    result = get_top_headlines(q = 'apple', api_key = 'dd9406fad0c041b58c2b4f05d744a7e0')
    pprint.pprint(result)