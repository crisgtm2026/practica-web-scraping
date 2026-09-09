import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, "html.parser")
tarjetas_citas = soup.find_all("div", class_="quote")

datos = []
for tarjeta in tarjetas_citas:
    cita = tarjeta.find("span", class_="text").text.strip()
    autor = tarjeta.find("small", class_="author").text.strip()
    tags_elementos = tarjeta.find_all("a", class_="tag")
    etiquetas = ", ".join([tag.text.strip() for tag in tags_elementos])

    datos.append({
        "cita": cita,
        "autor": autor,
        "etiquetas": etiquetas
    })

df = pd.DataFrame(datos)
df.to_csv("citas_famosas.csv", index=False)
print("Scraping exitoso y archivo citas_famosas.csv creado.")
