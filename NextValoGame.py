#imports
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import discord
import os
from cleardota import cleardota
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
from discord.utils import get
#from datetime import date
#from datetime import datetime
import datetime
from time import strptime
from googletrans import Translator, LANGUAGES
import asyncio
from itertools import cycle
import asyncio
import requests
import time

def ValoCheck(channelDataID):
  try:
    #Loads OG VLR page
    testv = #Set the team you wish to follow here - "https://www.vlr.gg/team/2965/og"
    uClient = uReq(testv)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    now = datetime.datetime.now()
    #Gets current time for later comparisons
    dt_string_day = now.strftime("%d")
    dt_string_month = now.strftime("%m")
    dt_string_year= now.strftime("%y")
    dt_string_hour= now.strftime("%H")
    dt_string_minute= now.strftime("%M")
    dt_string_second= now.strftime("%S")


    tabledata = page_soup.find("div", attrs = {"class":"wf-card "})
    tabledata2 = page_soup.findAll("div", {"class":"text-of"})
    tabledata3 = page_soup.findAll("div", {"class":"rm-item-date"})
    carrot = "carrot"
    #Gets the enemy team's name
    valoenemyteam  = page_soup.find("div", attrs={"class":"rm-item-opponent"}).text
    random = page_soup.find("span", {"class": "rm-item-score-eta"})
    random2 = str(random)
    
    #This will error out of the check if the score value is null [catching if the game found has already happened / started]
    if random2 == "None":
      carrot = carrot  + 1
      print(carrot)
      print("test")

    
    valotimeofgame = tabledata3[0].text
    datebeforesplit = valotimeofgame.strip()
    datesplit = datebeforesplit.rsplit(" ")
    actualdatebeforeclean = datesplit[1]
    testing = actualdatebeforeclean.split()
    #Creating date / time from all values from VLR
    dateOfGame = testing[1]
    timeOfGame = datesplit[0]
    prefixOfTime = testing[0]
    nameOfEnemy = valoenemyteam.strip() 
    datesections = dateOfGame.rsplit("/")
    datep1 = datesections[0]
    datep2 = datesections[1]
    datep3 = datesections[2]
    dateOfGame = datep3 + "/" + datep2 + "/" + datep1
    #Splitting out the date vlaues
    yearofgame = datep1
    monthnumber = datep2
    dayofgame2 = datep3

    print(timeOfGame)

    try:
      tags = page_soup.findAll("a", {"class":"wf-module-item mod-flex rm-item mod-first mod-tbd", 'href':True })
      games=[]
      for tag in tags:
        games.append(tag['href'])
        #print(tag['href'])

      matchlink = 'https://www.vlr.gg' + games[0]
    except:
      pass

    

    UTCTime = timeOfGame.rsplit(":")
    UTCTime2 = timeOfGame.rsplit(":")
    UTCBC = int(UTCTime[0]) - 1
    if UTCBC > 12:
      if prefixOfTime == "AM":
        prefixOfTime = "PM"
        
      else:
        prefixOfTime = "AM"
    if UTCBC > 12:
      hourofvalo = str(UTCBC-12)
      UTCTime = str(UTCBC - 12) + ":" + UTCTime[1] + prefixOfTime
    else:
      hourofvalo= UTCBC
      UTCTime = str(UTCBC) + ":" + UTCTime[1] + prefixOfTime
    
    #date/time comparisions to get a countdown

   
    if prefixOfTime == "PM":
      hourofvalo = hourofvalo + 12
    minuteofgame = UTCTime2[1]
    dt_string_year = "20" + str(dt_string_year)
    a = datetime.datetime(int(yearofgame), int(monthnumber), int(dayofgame2), int(hourofvalo), int(minuteofgame), 0)
    
    b = datetime.datetime(int(dt_string_year), int(dt_string_month), int(dt_string_day), int(dt_string_hour), int(dt_string_minute), int(dt_string_second))

    print(a)
    print(b)
    c = a-b
    print(c) 
    #Will check if the game has already begun
    if (c.days < 0):
      c = "The game is meant to have begun!"
    



    valorantTeams = "OG vs " + nameOfEnemy
    valorantTeamTime = dateOfGame + " - " + UTCTime + " UTC"


    return(valorantTeams, valorantTeamTime, c, dayofgame2, matchlink)

  except:
    return("No games planned", "No games planned", "No games planned")
   
