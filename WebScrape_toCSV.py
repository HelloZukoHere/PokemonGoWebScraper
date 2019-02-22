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


myURL = 'https://pokemongo.gamepress.gg/pokemon/407'
#Example,
#Mamoswine is 473
#Mewtwo is 150
#Roserade is 407
#


pageRequest = requests.get(myURL)
pageHTML = pageRequest.text

#now, parse the HTML
pageSOUP = soup(pageHTML, "html.parser")

QuickMoves = pageSOUP.findAll("td", {"headers": "view-field-quick-move-table-column"})
ChargeMoves = pageSOUP.findAll("td", {"headers": "view-field-charge-move-table-column"})
MoveGrade = pageSOUP.findAll("td", {"headers": "view-field-offensive-moveset-grade-table-column"})

#print(moves)
for x in QuickMoves:
    Attack = x.article.h2.a.span.span
    print(Attack)

for y in ChargeMoves:
    Charge = y.article.h2.a.span.span
    print(Charge)

for z in MoveGrade:
    Grade = z.div
    print(Grade)

#for line in pageSOUP.findAll("li", {"dir": "ltr"}):

    #print("".join(soup.strings))

movesExplain = pageSOUP.findAll("li", {"dir": "ltr"})
for line in movesExplain:
    text = line.p
    print(text)
