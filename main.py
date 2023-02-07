import requests
import csv
from bs4 import BeautifulSoup

url = "http://annuairesante.ameli.fr/recherche.html"

query = {
    "type": "ps",
    "ps_profession": "Médecin généraliste",
    "ps_localisation": "HERAULT (34)",
    "localisation_category": "departements",
    "submit_final": "Rechercher",
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

r = requests.Session()
response = r.get(url, params=query, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

doctors = []
for doctor in soup.find_all("div", class_="item-professionnel-inner"):
    name = doctor.find("h2", class_="ignore-css").text
    phone = doctor.find("div", class_ ="item left tel").text.replace("\xa0", "") if doctor.find("div", class_ ="item left tel") else "Non renseigné"
    address = doctor.find("div", class_="item left adresse").text
    doctors.append({"name": name, "phone": phone, "address": address})

with open("doctors.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "phone", "address"])
    writer.writeheader()
    writer.writerows(doctors)

# for i in range(min(20, len(doctors))):
#     print(doctors[i])