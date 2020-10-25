#2) Implemente um programa que receba um produto como parâmetro e liste o nome e o preço de 
# todos esses produtos no mercado livre, com paginação incluída. Busque uma forma de passar
# um parâmetro para o seu programa. 

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import json

def finds(browser, by, expression):
    try:
        return browser.find_elements(by, expression)
    except NoSuchElementException as nse:
        return None

def find(browser, by, expression):
    try:
        return browser.find_element(by, expression)
    except NoSuchElementException as nse:
        return None

output  = open('output.json', 'w', encoding='utf-8')
driver = webdriver.Firefox()
produto = input("Qual é o produto que deseja consultar ? ")
driverTexto = "https://lista.mercadolivre.com.br/"+produto+"#D[A:"+produto+"]"
driver.get(driverTexto)

items = finds(driver, By.CLASS_NAME, 'ui-search-result__content-wrapper')

for item in items:
        
    titulo = find(item, By.CLASS_NAME, 'ui-search-item__title').get_property("textContent")
    preco = find(item, By.CLASS_NAME, 'price-tag').get_property("textContent")
    print(titulo)
    print(preco)
