import requests
from bs4 import BeautifulSoup

url = "http://annuairesante.ameli.fr/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

with open("page.html", "w") as file:
    file.write(str(soup))