#Matthew Lee
#Second web scraper
#from https://www.youtube.com/watch?v=XQgXKtPSzUI



#Goal
#take information from https://pokemongo.gamepress.gg/pokemon/473
#for example mamoswine
#print to CSV or just show the best movesets
#additional features - GUI to type in pokemon name (lookup table for the number to alter the URL

import urllib
from urllib.request import urlopen as uReq
import csv
import requests
from bs4 import BeautifulSoup as soup

#import National Dex table
with open('NationalDex.csv', mode='r') as infile:
    reader = csv.reader(infile)
    NatDex = {rows[0]: rows[1] for rows in reader}

#get user input from the console
#user types name of pokemon they want the moveset for
pokeInput = input("Enter the Pokemon name to lookup \n")
type(pokeInput)
print(pokeInput)
print("OK! Let's look up the best Pokemon Go movesets for " + pokeInput)
pokeNum = NatDex[pokeInput.lower()]


myURL = 'https://pokemongo.gamepress.gg/pokemon/' + pokeNum
print(myURL)
#Example,
#Mamoswine is 473
#Mewtwo is 150
#Roserade is 407


pageRequest = requests.get(myURL)
pageHTML = pageRequest.text

#now, parse the HTML
pageSOUP = soup(pageHTML, "html.parser")

#find the quick moves, charge moves, and the grade of each pair
QuickMoves = pageSOUP.findAll("td", {"headers": "view-field-quick-move-table-column"})
ChargeMoves = pageSOUP.findAll("td", {"headers": "view-field-charge-move-table-column"})
MoveGrade = pageSOUP.findAll("td", {"headers": "view-field-offensive-moveset-grade-table-column"})

listAttack = []
listCharge = []
listGrade = []

for x in QuickMoves:
    Quick = str(x.article.h2.a.span.span.text)
    listAttack.append(Quick)

for y in ChargeMoves:
    Charge = str(y.article.h2.a.span.span.text)
    listCharge.append(Charge)

for z in MoveGrade:
    Grade = str(z.div.text)
    listGrade.append(Grade)

movesExplain = pageSOUP.findAll("li", {"dir": "ltr"})
for line in movesExplain:
    print(line.p.text)

print(listAttack[0] + " + " + listCharge[0] + " = " + listGrade[0])
print(listAttack[1] + " + " + listCharge[1] + " = " + listGrade[1])
print(listAttack[2] + " + " + listCharge[2] + " = " + listGrade[2])
print(listAttack[3] + " + " + listCharge[3] + " = " + listGrade[3])

