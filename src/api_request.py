import requests


def api_req(url):
    response = requests.get(url)
    result = response.json()
    data = result['results']
    
    for item in data:
        print(item['name'])
    

if __name__ == '__main__':
    api_req('https://pokeapi.co/api/v2/pokemon?limit=150')