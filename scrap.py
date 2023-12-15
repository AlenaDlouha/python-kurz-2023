from requests_html import HTMLSession
session = HTMLSession()
stranka = session.get("https://apps.kodim.cz/python-data/dhmo")
for znacka in stranka.html.find('h2'):
    print(znacka.text)

for odkaz in stranka.html.find('a'):
    print(odkaz.attrs['href'])

for obrazek in stranka.html.find('img'):
    print(obrazek.attrs['src'])