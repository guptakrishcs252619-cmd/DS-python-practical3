import requests
from bs4 import BeautifulSoup

url = "https://www.wikipedia.org/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

paragraphs = soup.find_all("p")

print("FIRST 3 PARAGRAPHS:")
for i, p in enumerate(paragraphs[:3], 1):
    print(f"{i}. {p.get_text(strip=True)}")

images = soup.find_all("img")

print("\nIMAGE SRC URLs:")
for img in images:
    src = img.get("src")
    if src:
        print(src)

links = soup.find_all("a")

print("\nTOTAL NUMBER OF LINKS:", len(links))

print("\nHEADINGS:")

headings = soup.find_all(["h1", "h2", "h3"])

for heading in headings:
    text = heading.get_text(strip=True)
    if text:
        print(text)

print("\nLANGUAGE NAMES:")

languages = soup.select(".central-featured-lang")

for language in languages:
    name = language.find("strong")
    if name:
        print(name.get_text(strip=True))
