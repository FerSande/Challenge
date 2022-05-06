import random
import requests
import json

def get_random_member(key,token):
    url = "https://api.trello.com/1/boards/6266b7d00136df5b8778f69a/members"
    query = {'key': key,'token': token}
    response = requests.request("GET",url,params=query)
    lista = json.loads(response.text)
    listaIds = []
    for i in lista:
        listaIds.append(i["id"])
    
    member = random.choice(listaIds)

    return member

def getLabel(category,key,token):
    url = "https://api.trello.com/1/boards/6266b7d00136df5b8778f69a/labels"
    query = {'key': key,'token': token}
    response = requests.request("GET",url,params=query)

    lista = json.loads(response.text)
    id = ""
    for i in lista:
        if category == i["name"]:
            id = i['id']

    return id
