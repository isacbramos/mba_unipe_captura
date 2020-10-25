#1) Implemente um programa que entre no site do UOL e imprima apenas a seguinte mensagem: 
# A cotação atual do dólar é: <cotação>, onde <cotação> vai ser o valor capturado do site 
# no momento. Procure uma forma de omitir as mensagens de log na execução do seu programa 
# para aparecer apenas essa mensagem como saída. 

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
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
driver.get("https://www.uol.com.br/")
# elem = driver.find_element_by_tag_name("body")
# elem.send_keys(Keys.END)
# elem.send_keys(Keys.END)
# elem.send_keys(Keys.END)
items = finds(driver, By.CLASS_NAME, 'HU_currency__quote')
dolar = items[0].get_property("textContent").strip()
print("A  cotação  atual  do  dólar  é: "+dolar)
