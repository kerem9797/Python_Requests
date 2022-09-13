# INFORMATION FROM THE SHOPPING SITE

import requests
import json
class hepsiburada:
    def __init__(self):
        self.api_url="https://www.hepsiburada.com"
        self.api_key="E761AF3E6F8549DC23B070AB81390D26"
    def getComputersAndTablets(self):
        result=requests.get(f"{self.api_url}/laptop-notebook-dizustu-bilgisayarlar-c-98?api_key={self.api_key}&sayfa=2")
        return result.json()
        
    def getGamesAndGamesConsoles(self):
        result=requests.get(f"{self.api_url}/oyunlar-oyun-konsollari-c-2147483602?api_key={self.api_key}&sayfa=2")
        return result.json()

hepsiburadaApi=hepsiburada()
while True:
    choice=input('1-Computers and Tablets\n2-Games and Games Consoles\n3-Exit\nChoice:')
    if choice=='1':
        shopping=hepsiburadaApi.getComputersAndTablets()
        print(shopping)
    elif choice=='2':
        shopping=hepsiburadaApi.getGamesAndGamesConsoles()
        print(shopping)
    elif choice=='3':
        break
    else:
        print('Bad option')
    

