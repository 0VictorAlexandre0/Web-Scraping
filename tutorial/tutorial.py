# Bibliotecas que nós instalamos manualmente
from bs4 import BeautifulSoup
import requests
# Bibliotecas nativas do Python
import json
# URL do site
url = 'https://infosimples.com/vagas/desafio/commercia/product.html'
# Objeto contendo a resposta final
resposta_final = {}
# Faz o request
response = requests.get(url)
# Parse do responses
parsed_html = BeautifulSoup(response.content, 'html.parser')
# Vamos pegar o título do produto, na tag H2, com ID "product_title"
resposta_final['title'] = parsed_html.select_one('h2#product_title').get_text()
# Aqui você adiciona os outros campos...

# Gera string JSON com a resposta final
json_resposta_final = json.dumps(resposta_final)
# Salva o arquivo JSON com a resposta final
with open('produto.json', 'w') as arquivo_json:
 arquivo_json.write(json_resposta_final)
