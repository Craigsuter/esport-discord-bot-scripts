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



def CSGOCheck(channelDataID):
  try:
    #Loading HLTV of OG
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}


    OGpage = #Set the HLTV matchbox url for the team you wish to track here e.g - 'https://www.hltv.org/team/10503/og#tab-matchesBox'
    r2 = requests.get(OGpage, headers=headers)

    page_soup2 = soup(r2.text, "html.parser")
    dataofpage = page_soup2.findAll("td", {"class":"matchpage-button-cell"})


    linkinfo = []
    #If game found - open the page via the href / link info
    for a in dataofpage[0].findAll('a', href=True):

      linkinfo.append(a['href'])

    matchlink = "https://www.hltv.org" + linkinfo[0]


   
    
    r = requests.get(matchlink , headers=headers)
    
    #Load the page of the match
    page_soup = soup(r.text, "html.parser")
    test = page_soup.findAll("div", {"class":"teamName"})
    team1= test[0].text
    team2 = test[1].text
    
    #Grab time / date
    test2 = page_soup.findAll("div", {"class":"time"})
    
    test3 = page_soup.findAll("div",{"class":"date"})
    
    #Time till game count down via HLTV value
    test4 = page_soup.findAll("div", {"class":"countdown"})
    time1 = test4[0].text
    time2 = time1.replace(" ","")
    
    #Link to the tournament page
    link4tourni = page_soup.findAll("div", {"class":"event text-ellipsis"})

    for a in link4tourni[0].findAll('a', href=True):
        link4tourni = "https://www.hltv.org" + a['href']
  
    teams = team1 + " vs " + team2
    dateofgame = test2[0].text
    timeofgame = test3[0].text
    

    datep1 = dateofgame.rsplit(":")
    datep2 = int(datep1[0]) - 2
    if(datep2 < 10):
      datep3 = "0" + str(datep2) + ":" + datep1[1]

    else:
      datep3 = str(datep2) + ":" + datep1[1]

    #Prints based on pro-match channel - will give a more chat friendly version
    if((channelDataID #Assign the values for the channels you want a shorter version of the result to be sent too here):
      embed=teams + " - Starts in: " + time2 + " - For more information use !nextcsgo in <#721391448812945480>"
    else:
      embed=discord.Embed(title="OG CSGO's next game", url="https://www.hltv.org/team/10503/og#tab-matchesBox",color=0xff8800)
      embed.set_thumbnail(url="https://liquipedia.net/commons/images/thumb/0/00/OG_RB_Logo.png/600px-OG_RB_Logo.png")
      embed.add_field(name=teams, value= timeofgame + " - " + datep3 + " UTC", inline=True)
      embed.add_field(name="Time till game", value=time2, inline=False)
      embed.add_field(name="Notice", value="Please check HLTV by clicking the title of this embed for more information as the time might not be accurate", inline=False)
      embed.add_field(name="Links", value="OG Liquipedia: https://liquipedia.net/counterstrike/OG\nOG HLTV: https://www.hltv.org/team/10503/og#tab-matchesBox\nGame page: " + matchlink +"\nTournament: " + link4tourni, inline=False)


    return(teams, timeofgame, datep3, time2, matchlink, link4tourni, embed)



  except:
    if((channelDataID == 690952309827698749) or (channelDataID == 689903856095723569)):
      embed= "There is currently no games planned for OG, for more information use !nextcsgo in <#721391448812945480>"
    else:
      embed=discord.Embed(title="OG CSGO's next game", url="https://www.hltv.org/team/10503/og#tab-matchesBox",color=0xff8800)
      embed.set_thumbnail(url="https://liquipedia.net/commons/images/thumb/0/00/OG_RB_Logo.png/600px-OG_RB_Logo.png")
      embed.add_field(name="No games planned", value="No games planned", inline=True)
      embed.add_field(name="Links", value="https://www.hltv.org/team/10503/og#tab-matchesBox/ https://liquipedia.net/counterstrike/OG", inline=False)
    
    return("No games planned","No games planned","No games planned","No games planned","No games planned","No games planned", embed)
