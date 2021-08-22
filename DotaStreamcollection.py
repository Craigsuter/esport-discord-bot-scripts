#imports
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import discord
import os
from dotenv import load_dotenv
load_dotenv()
import asyncio
import requests

#Gets the streams from OG's Liquipedia
def DotaStreams():
  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
  try:
    my_url10 = #InsertYourLinkToATeamsLiquipedia, example - "https://liquipedia.net/dota2/OG"

    my_url10 = str(my_url10)
    uClient10 = uReq(my_url10)
    page_html10 = uClient10.read()
    uClient10.close()
    page_soup10 = soup(page_html10, "html.parser")

    #Web scrapes for the first game and finds its url
    v_table = page_soup10.find("table", attrs={"class": "wikitable wikitable-striped infobox_matches_content"})
    tabledata = v_table.tbody.find_all("tr")
    #for td in tabledata[1].find_all('a', href=True):
      #print ("Found the URL:", td['href'])

    #puts that URL into the new webscraping
    tablestorage = tabledata[1].find_all('a', href=True)
    URL = tablestorage[0]['href']
    extendedURL = "https://liquipedia.net" + URL


    #Parses the HTML data - Dota
    containers = page_soup10.findAll(
        "span", {"class": "team-template-team2-short"})
    containers2 = page_soup10.findAll(
        "span", {"class": "team-template-team-short"})

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

  
    


    #Opens the new page, and checks for the stream table
    page=extendedURL
    r3 = requests.get(page,headers=headers)
    try:
      page_soup2 = soup(r3.text,"html.parser")
      streamtable = page_soup2.find("table",{"style": "text-align:center;margin:0;margin-bottom:1em"})
      table_body = streamtable.find('tbody')
      


      test=[]
      for tr in streamtable.findAll('tr'):
        for td in tr.findAll('td'):
          #print(td)
          test.append(td)
          
      #appends flags / links to their array to match up
      i=0
      streamlinks=[]
      flags=[]
      while (i < len(test)):
        if (i < (len(test) / 2)):
          test2 = test[i].find_all(href=True)
          flag = test2[0].get('href')
          flag2 = flag.rsplit(":")
          flags.append(flag2[(len(flag2)-1)])
        else:
          test2 = test[i].find_all(href=True)
          streamlinks.append(test2[0].get('href'))
        
        i=i+1
      
      #Creates the flags into versions that Discord can use
      flagsToSend=[]
      counter3=0
      if (len(streamlinks) == len(flags)):
        while counter3 < (len(flags)):
          if (flags[counter3] == "Indonesia"):
            flagsToSend.append(':flag_id:')
          elif(flags[counter3] == "Philippines"):
            flagsToSend.append(':flag_ph:')
          elif(flags[counter3]=="DeAt_hd.png"):
            flagsToSend.append(':flag_de:')
          elif (flags[counter3] == "UsGb_hd.png"):
            flagsToSend.append(':flag_gb:')
          elif (flags[counter3] == 'Russia'):
            flagsToSend.append(':flag_ru:')
          elif (flags[counter3] == 'Spain'):
            flagsToSend.append(':flag_es:')
          elif (flags[counter3] == 'France'):
            flagsToSend.append(':flag_fr:')
          elif (flags[counter3]=='Pl_hd.png'):
            flagsToSend.append(':flag_pl:')
          elif(flags[counter3]=='Cn_hd.png'):
            flagsToSend.append(':flag_cn:')
          elif(flags[counter3]=='China'):
            flagsToSend.append(':flag_cn:')
          elif(flags[counter3]=='EsMx_hd.png'):
            flagsToSend.append(':flag_es:')
          elif(flags[counter3]=='PtBr_hd.png'):
            flagsToSend.append(':flag_br:')
          elif(flags[counter3]=='Ph_hd.png'):
            flagsToSend.append(':flag_ph:')
          elif(flags[counter3]=='Germany'):
            flagsToSend.append(':flag_de:')
          elif(flags[counter3]=='Thailand'):
            flagsToSend.append(':flag_th:')
          elif(flags[counter3]=='Serbia'):
            flagsToSend.append(':flag_rs:')
          elif(flags[counter3]=='Vietnam'):
            flagsToSend.append(':flag_vn:')
          else:
            flagsToSend.append(':pirate_flag:')
          counter3 += 1

        #Creates the text that goes into the message attached the flags + streams together 
        counter4=0
        flagMessage=""
        while counter4 < (len(flagsToSend)):
          flagadd = str(flagsToSend[counter4])
          streamsAdd = str(streamlinks[counter4])
          flagMessage = flagMessage + flagadd + " <" + streamsAdd + ">\n"
          counter4 += 1  

    except:
        flagMessage="No streams were found for this game"
      
    convertedURL = "<" + extendedURL + ">"


    return(Teams1, Teams2, flagMessage, convertedURL)
    #embed=discord.Embed(title="Dota streams found!", color=0xf10909)
    #embed.add_field(name="The game found", value= Teams1 + " vs " + Teams2, inline=True)
    #embed.add_field(name="Streams available", value=flagMessage, inline=False)
    #embed.add_field(name="Where I found the streams", value= convertedURL, inline=False)
    #await message.channel.send(embed=embed)


  except:
    return("No games found","No games found","No games found","No games found")


  #This will pass back the data about the teams playing / and the stream links including flags in Discord format and a link to the page it found the streams
  #Update line 15 with team link
