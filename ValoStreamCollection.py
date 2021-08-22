#imports
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import discord
import os
from dotenv import load_dotenv
load_dotenv()
import asyncio
import requests


def ValoStreams():
  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

  page= #Place the VLR page for the team you wish to get streams / game data on e.g - 'https://www.vlr.gg/team/2965/og'
  r3 = requests.get(page,headers=headers)

  page_soup2 = soup(r3.text,"html.parser")
  dataofpage =  page_soup2.findAll("a", {"class":"wf-module-item mod-flex rm-item mod-first mod-tbd"})
  

  valoenemyteam  = page_soup2.find("div", attrs={"class":"rm-item-opponent"}).text
  valoenemyteam = valoenemyteam.strip()   
  tags = page_soup2.findAll("a", {"class":"wf-module-item mod-flex rm-item mod-first mod-tbd", 'href':True })
  games=[]
  for tag in tags:
    games.append(tag['href'])
    #print(tag['href'])


  try:
    matchlink = 'https://www.vlr.gg' + games[0]
    
    r = requests.get(matchlink , headers=headers)

    try:
      page_soup = soup(r.text, "html.parser")
      test = page_soup.findAll("div", {"class":"match-streams-container"})


      headings=[]
      i = 0
      lenrot = len(test)
      
      #Gets stream links
      while(i < (lenrot)):
        for a in test[i].findAll('a', href=True):
          headings.append(a['href'])

          
        i =i+1



      #Getting flag data
      flags=[]
      j = 0
      while (j < (lenrot)):
        try:
          for element in test[j].find_all('i', class_=True):
            flags.append(element["class"])
        except:
          pass
        j = j+1


      flaglen = len(flags)

      flagdata=[]
      k=0
      while (k < (flaglen - 1)):
        try:

          data = flags[k][1]
          datasplit = data.rsplit("-")
          flagdata.append(datasplit[1])

        except:
          pass
        k=k+2

      actualflags=[]
      o=0
      while ((o < len(flagdata)) or (o == 0)):
        try:
          if (flagdata[o]== "un"):
            actualflags.append(":flag_eu:")
          else:
            actualflags.append(":flag_" + flagdata[o] + ":") 
        except:
          pass
        o = o+1


      m=0
      
      streams=""
      while (m < len(headings)):
        streams = str(streams) + actualflags[m] + " <" + headings[m] + ">\n"
        m=m+1

      if(len(flags) == 0):
        streams = "No streams found"

    except:
      streams = "No streams found"

    
    
    return(valoenemyteam,streams,matchlink)
    



  except:
    return("No games found", "No games found", "No games found")
