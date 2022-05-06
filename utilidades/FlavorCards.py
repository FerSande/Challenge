import requests
from random_word import RandomWords
import random
from utilidades.getFuntions import get_random_member,getLabel
from utilidades.decrypt import decrypt

key = decrypt("NzE4YmY4MDcyYmQ5YzVkOWM0NjE1MWNiMTJiOTg3NTg=")
token = decrypt("NzMxYjdjNWQyZDY2OTYwZjI5NDgyMWRhM2YwMDYzMzgxMzY0NjdmZTA3MDNlN2Q1YjZjMzE2YzhhNWY1MGFjOQ==")


def total(task):
    print(task.dict())
    i = task.dict()
    typeTask = (i["type"])
    url = f"https://api.trello.com/1/cards"

    if typeTask == "issue":
        querystring = {"name": i["title"], "idList": "6266b7d00136df5b8778f69b", "desc":i["description"], "key": key, "token": token}
    elif typeTask == "bug":
        r = RandomWords()
        card_name = "bug-{0}-{1}".format(r.get_random_word(),random.randint(1,100))
        randomMembers = get_random_member(key,token)
        querystring = {"name": card_name, "idList": "6266b7d00136df5b8778f69b", "desc":i["description"],"idLabels":"6266c1d16f1dfb4c638b63a6","idMembers" : randomMembers, "key": key, "token": token}
    elif typeTask == "task":
        label = getLabel(i["category"],key,token)
        querystring = {"name": i["title"], "idList": "6266b7d00136df5b8778f69b", "idLabels":label, "key": key, "token": token}

    response = requests.request("POST", url, params=querystring)
    card_id = response.json()["id"]
    return card_id
