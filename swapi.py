import requests

#url = requests.get("https://swapi.dev/api/people/1/")
#data = url.json()
#print(data)

#getPerson(index)

def getPerson(index=1):
    result_url = requests.get(f"https://swapi.dev/api/people/{index}")
    return result_url.json()
