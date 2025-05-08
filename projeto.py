from bs4 import BeautifulSoup
import requests
import json

url = 'https://infosimples.com/vagas/desafio/commercia/product.html'

resposta = {}

response = requests.get(url)

parsed_html = BeautifulSoup(response.content, 'html.parser')
resposta['title'] = parsed_html.select_one('h2#product_title').get_text()
resposta['brand'] = parsed_html.select_one('div.brand').get_text()

lista = []
'''
resposta['categories'] = parsed_html.select_one('nav.current-category').get_text()
for item in resposta['categories']:
    lista.append(item)
'''

'''
for item in parsed_html.select_one('nav.current-category a'):
   lista.append(item.get_text())

print(lista)
'''

resposta['categories'] = parsed_html.select_one('nav.current-category').get_text()
print(resposta['categories'(1)])





json_resposta_final = json.dumps(resposta)

with open('teste.json', 'w') as arquivo_json:
 arquivo_json.write(json_resposta_final)

