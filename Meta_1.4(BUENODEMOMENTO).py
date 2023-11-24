"""
Alumno: Aguilar Covarrubias Oscar Ulises
Fecha: 10/09/2023

Programa:
         Modificar la función de la Meta 1.3 para que ademas de recibir el nombre del producto, reciba el numero de
         productos (ó paginas) en Amazon, ademas de automatizar la busqueda del producto, debe extraer el nombre del
         producto, rating, precio, fecha de entrega. La función debe de retornar un dataframe y crear un archivo csv con la
         información recabada.
"""

import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

response = requests.get("https://www.amazon.com.mx/ref=nav_logo")
print(response.status_code)

s = Service(ChromeDriverManager().install())
opc = Options()
opc.add_argument("--window-size=1020,1200")

navegador = webdriver.Chrome(service=s, options=opc)
navegador.get("https://www.amazon.com.mx/ref=nav_logo")

product = input("¿Qué producto desea buscar? ")
num = int(input("¿Cuántos productos desea analizar? "))

searchBox = navegador.find_element(By.NAME, "field-keywords")
searchBox.send_keys(product)
searchBox.submit()

# Esperar a que la página de resultados se cargue completamente
wait = WebDriverWait(navegador, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "s-main-slot")))

soup = BeautifulSoup(navegador.page_source, "html.parser")

datos = {"Nombre": [], "Ratings": [], "Precio": [], "Fecha": []}

listaDivs = soup.find_all("div", attrs={"class": "a-section a-spacing-small puis-padding-left-small puis-padding-right-small"})

for div in listaDivs[:num]:
    Nombre = div.find("span", attrs={"class": "a-size-base-plus a-color-base a-text-normal"})
    Ratings = div.find("span", attrs={"class": "a-size-base puis-bold-weight-text"})
    Precio = div.find("span", attrs={"class": "a-price-whole"})
    Fecha = div.find("span", attrs={"class": "a-color-base a-text-bold"})
    print(Ratings)

    datos["Nombre"].append(Nombre.text.strip() if Nombre else "")
    datos["Ratings"].append(Ratings.text.strip() if Ratings else "")
    datos["Precio"].append(Precio.text.strip() if Precio else "")
    datos["Fecha"].append(Fecha.text.strip() if Fecha else "")

dataDf = pd.DataFrame(datos)
print(dataDf)
dataDf.to_csv("amazon.csv")
print(navegador.title)

navegador.quit()