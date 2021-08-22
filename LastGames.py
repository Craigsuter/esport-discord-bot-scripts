#imports
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import discord
import os
from dotenv import load_dotenv
load_dotenv()
import asyncio


def LastGames():
  testurl = "https://liquipedia.net/dota2/OG/Played_Matches"
  uClient = uReq(testurl)
  page_html = uClient.read()
  uClient.close()
  page_soup = soup(page_html,"html.parser")

  tabledata = page_soup.find("div", attrs ={"class": "table-responsive recent-matches"})
  #print(tabledata)
  tabledata2 = tabledata.tbody.find_all("tr")
  tabledata3 = tabledata2[1].find_all("td")
  try:
    LastgameDate1 = tabledata3[0].text
    LastGameTime1 = tabledata3[1].text
    LastGameTier1 = tabledata3[2].text
    LastGameType1 = tabledata3[3].text
    LastGameTourni1 = tabledata3[5].text
    LastGameScore1 = tabledata3[6].text
    LastGameEnemy1 = tabledata3[7].text
    embed=discord.Embed(title="The last game OG Dota played",url='https://liquipedia.net/dota2/OG/Played_Matches', color=0xf10909)
    Dateandtime1 = LastgameDate1 +  " - " + LastGameTourni1
  except:
    print("kek")
    
  
  tabledata4 = tabledata2[2].find_all("td")
  try:
    LastgameDate2 = tabledata4[0].text
    LastGameTime2 = tabledata4[1].text
    LastGameTier2 = tabledata4[2].text
    LastGameType2 = tabledata4[3].text
    LastGameTourni2 = tabledata4[5].text
    LastGameScore2 = tabledata4[6].text
    LastGameEnemy2 = tabledata4[7].text
    Dateandtime2 = LastgameDate2 +  " - " + LastGameTourni2
  except:
    print("kek2")
    

  tabledata5 = tabledata2[3].find_all("td")
  try:
    LastgameDate3 = tabledata5[0].text
    LastGameTime3 = tabledata5[1].text
    LastGameTier3 = tabledata5[2].text
    LastGameType3 = tabledata5[3].text
    LastGameTourni3 = tabledata5[5].text
    LastGameScore3 = tabledata5[6].text
    LastGameEnemy3 = tabledata5[7].text
    Dateandtime3 = LastgameDate3 +  " - " + LastGameTourni3
  except:
    print("kek3")


  return(Dateandtime1,Dateandtime2,Dateandtime3,LastGameScore1,LastGameScore2,LastGameScore3,LastGameEnemy1,LastGameEnemy2,LastGameEnemy3)


#Usage - in main call the definition and you can poll the values you want from the list above, alternatively, you could build an embed / message within this file
