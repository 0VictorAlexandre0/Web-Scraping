from bs4 import BeautifulSoup
import requests
import json

url = 'https://infosimples.com/vagas/desafio/commercia/product.html'

resposta = {}
response = requests.get(url)
parsed_html = BeautifulSoup(response.content, 'html.parser')


resposta['title'] = parsed_html.select_one('h2#product_title').get_text(strip=True)

resposta['brand'] = parsed_html.select_one('div.brand').get_text(strip=True)

resposta['categories'] = [a.get_text(strip=True) 
    for a in parsed_html.select('nav.current-category a')]

resposta['description'] = [p.get_text(strip=True) 
    for p in parsed_html.select('div.proddet p')]

resposta['skus'] = [name.get_text(strip=True)
    for name in parsed_html.select('div.prod-nome')], [current_price.get_text(strip=True)
        for current_price in parsed_html.select('div.prod-pnow')], [old_price.get_text(strip=True)
            for old_price in parsed_html.select('div.prod-pold')], [i.get_text(strip=True)
                for i in parsed_html.select('div.card-container i')]

resposta['properties'] = [td.get_text(strip=True)
    for td in parsed_html.select('table.pure-table td')]


json_resposta_final = json.dumps(resposta)


with open('produto.json', 'w') as arquivo_json:
    json.dump(resposta, arquivo_json, ensure_ascii=False, indent=2)

