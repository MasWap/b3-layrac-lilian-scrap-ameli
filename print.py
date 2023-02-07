import requests
from bs4 import BeautifulSoup

url = "http://annuairesante.ameli.fr/professionnels-de-sante/recherche/liste-resultats-page-1-par_page-20-tri-aleatoire.html"


r = requests.Session()
response = r.get(url)
soup = BeautifulSoup(response.content, "html.parser")
print(r.status_code)

# with open("pageDocteurs.html", "w") as file:
#     file.write(str(soup))