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



def DotaCheck(channelDataID):
    #Opening OG's Liquipedia page
      
      headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}


      OGpage = #Assign the URL here for the team you would like to follow on the command - 'https://liquipedia.net/dota2/OG'
      my_url = OGpage
      r2 = requests.get(OGpage, headers=headers)

      page_soup2 = soup(r2.text, "html.parser")



      
      links = 'OG Liquipedia: https://liquipedia.net/dota2/OG'

      now = datetime.datetime.now()
      #Getting current date / time values
      dt_string_day = now.strftime("%d")
      dt_string_month = now.strftime("%m")
      dt_string_year= now.strftime("%y")
      dt_string_hour= now.strftime("%H")
      dt_string_minute= now.strftime("%M")
      dt_string_second= now.strftime("%S")



      #Parses the HTML data - Dota - grabbing time / both team HTML
      containers = page_soup2.findAll(
          "span", {"class": "team-template-team2-short"})
      containers2 = page_soup2.findAll(
          "span", {"class": "team-template-team-short"})
      containers3 = page_soup2.findAll(
          "span", {"class": "timer-object timer-object-countdown-only"})

      try:
        v_table = page_soup2.find("table", attrs={"class": "wikitable wikitable-striped infobox_matches_content"})
        tabledata = v_table.tbody.find_all("tr")


        tablestorage = tabledata[1].find_all('a', href=True)
        URL = tablestorage[0]['href']
        extendedURL = "https://liquipedia.net" + URL
        links = links + "\n Tournament: " + extendedURL
      except:
        pass

      #This finds the next match time - Dota
      try:
          nextgametime = containers3[0].text
          print(nextgametime)
      except:
          pass

      #Adds game to containers - dota
      try:
          team1 = containers[0]
          team2 = containers2[0]
      except:
          pass

      #Grabbing 1st team - Dota 2
      try:

          Teams1 = team1.a["title"]
      except:
          try:

              Teams1 = team1["data-highlightingclass"]

          except:
              pass

      #Grabbing 2nd team - Dota 2
      try:

          Teams2 = team2.a["title"]

      except:
          try:

              Teams2 = team2["data-highlightingclass"]

          except:
              pass

      #prints next dota 2 game
      try:
          Teams = (Teams1 + " vs " + Teams2)
          nextdotagame = ("<:OGpeepoThumbsUp:734000712169553951> " + Teams1 + " vs " + Teams2 + " on " +
                          nextgametime +
                          ", more information can be found at - " +
                          my_url)
          datetimesplit = nextgametime.rsplit(" ")
          monthofgame = datetimesplit[0]
          dayofgame1 = datetimesplit[1]
          dayofgame2 = dayofgame1[:-1]
          yearofgame = datetimesplit[2]
          timeofgame = datetimesplit[4]
          timesplit = timeofgame.rsplit(":")
          hourofgame = timesplit[0]
          minuteofgame = timesplit[1]
          dt_string_year = "20" + str(dt_string_year)

          try:
            monthnumber = strptime(monthofgame,'%B').tm_mon
          except:
            monthnumber = strptime(monthofgame,'%b').tm_mon
          
          #Compares the time between current  time and when game starts 
          a = datetime.datetime(int(yearofgame), int(monthnumber), int(dayofgame2), int(hourofgame), int(minuteofgame), 0)

          b = datetime.datetime(int(dt_string_year), int(dt_string_month), int(dt_string_day), int(dt_string_hour), int(dt_string_minute), int(dt_string_second))

          c = a-b
          print(c)       
          #Verifies if the game has begun
          if (c.days < 0):
            
            c = "The game is meant to have begun!"

  



      except:
        #If no game available - will tell user
          Teams = 'No games planned'
          nextgametime = 'No games planned'
          dayofgame2 = 'no games planned'
          
          c = "No games planned"

      #Verifies the channels if in pro-match 
      if((channelDataID #assign any values you want here to have shorter versions of the result):
        c= str(c)
        if (c == "No games planned"):
          embed = "No games planned currently - For more information use !nextdota in <#721391448812945480>"
        else:
          embed= Teams + " - Starts in: " + c + " - For more information use !nextdota in <#721391448812945480>"

      #Creates the embed with all the details
      else:
        embed=discord.Embed(title="OG Dota's next game", url="https://liquipedia.net/dota2/OG", color=0xf10909)
        embed.set_thumbnail(url="https://liquipedia.net/commons/images/thumb/0/00/OG_RB_Logo.png/600px-OG_RB_Logo.png")
        embed.add_field(name=Teams, value=nextgametime, inline=True)
        embed.add_field(name="Time remaining", value = c, inline=False)
        embed.add_field(name="Notice",value="Please check Liquipedia by clicking the title of this embed for more information as the time might not be accurate", inline=False)
        embed.add_field(name="Links", value=links, inline=False)

      return(embed, Teams,nextgametime, c, links,dayofgame2)
