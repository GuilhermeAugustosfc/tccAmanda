from django.db import models
import requests
from bs4 import BeautifulSoup

class Produto(models.Model):

    def __init__(self):
        self.search = ""
    def buscaProduto(self, dados):
        sites_de_busca = ["https://www.americanas.com.br/busca/","https://buscas2.casasbahia.com.br/busca?q=","https://search3.pontofrio.com.br/busca?q=","https://www.submarino.com.br/busca/"]
        for sites in sites_de_busca:
            url = sites + dados['search']
            response = requests.get(url=url)
            content = response.content
            self.scrapping_page(content)
    def scrapping_page(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        produtos = soup.find_all(".product-grid-item")
        a = "nada"





# Create your models here.
