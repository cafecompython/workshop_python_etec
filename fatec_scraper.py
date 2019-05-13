# carregar as bibliotecas
import lxml.html
import requests
from urllib.parse import urljoin



url = 'https://www.vestibularfatec.com.br/unidades-cursos/' # link base
resposta = requests.get(url) # resposta da solicitação ao site (binário)

doc = lxml.html.fromstring(resposta.content) # transforma o conteúdo da resposta em html 

cursos = doc.xpath('//div[@id="cursos"]/ul/li/a/text()') # usa xpath para coletar os títulos de cada curso
links = doc.xpath('//div[@id="cursos"]/ul/li/a/@href') # usa xpath para coletar os links relativos de cada curso

links_cursos = [] # cria uma lista vazia para guardar os links tratados

# trata os links
for link in links:
    link_unido = urljoin(url, link) # une o link base 
    links_cursos.append(link_unido) # guarda o link tratado na lista links_cursos

resultados = list(zip(cursos, links_cursos)) # cria uma lista de tuplas combinando (cursos, links_cursos)

# escreve os resultados em um arquivo de texto
with open('cursos_fatec.txt', 'a') as f:
    for resultado in resultados:
        f.write('%s: %s \n' % resultado) # transforma cada tupla em uma string e escreve no arquivo 