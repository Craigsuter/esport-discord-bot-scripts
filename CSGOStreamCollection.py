#imports
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import discord
import os
from dotenv import load_dotenv
load_dotenv()
import asyncio
import requests


def CSGOStreams():
  try:
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

    OGpage = #Add the match page here for the team you want to scan e.g - 'https://www.hltv.org/team/10503/og#tab-matchesBox'
    r2 = requests.get(OGpage, headers=headers)

    page_soup2 = soup(r2.text, "html.parser")
    dataofpage = page_soup2.findAll("td", {"class":"matchpage-button-cell"})

    #finds the link to the game page on HLTV, checking if there is a game at all
    linkinfo = []
    for a in dataofpage[0].findAll('a', href=True):

      linkinfo.append(a['href'])

    matchlink = "https://www.hltv.org" + linkinfo[0]  
    r = requests.get(matchlink , headers=headers)
    try:
      #Opens the page for the game and gets the values from it that are needed
      page_soup = soup(r.text, "html.parser")
      tabledata = page_soup.findAll("div",{"class":"external-stream"})
      test = page_soup.findAll("div", {"class":"teamName"})
      team1= test[0].text
      team2 = test[1].text
      headings=[]
      headings2=[]

      links=''

      #for note - we need to use a i / i++ loop to get all the links out of tabledata using an array catch of len-1
      lenrot = len(tabledata)
      i=0
      print(lenrot)
      while(i < (lenrot)):
        for a in tabledata[i].findAll('a', href=True):
          headings.append(a['href'])
        i = i+1
      j=0

      try:
        testingdata = page_soup.findAll("div",{"class":"stream-box-embed"})
        
        #Checks for streams 
        while(j < len(testingdata)):
        
          value = testingdata[j]
          testsplit = str(value).rsplit("=")
          
          splitlink = testsplit[5].rsplit(".")
          splitsecond = splitlink[1]
          link = testsplit[5]
          link2 = link[1:]
          if(splitsecond[0] == "y"):
            headings.insert(j, link2)
          
          j+=1

      except:
        print(":(")
        pass
      
      print(headings)
      print(len(headings))

      

      #This finds the stream table
      moredata = page_soup.findAll("div", {"class":"stream-box-embed"})

      flagdata=[]
      k=0
      #Finds all of the flag images and appends them to the flag table
      while (k < len(moredata)):
        moredata2 = moredata[k].findAll('img')

        for img in moredata2:
          if img.has_attr('src'):
            #print(img['src'])
            flagdata.append(img['src'])
        k= k+1


      flags=[]
      l=0
      #converts flag names into usable flag emotes that discord can use and appends them to the the links to the stream
      while (l<len(flagdata)):
        flag = flagdata[l].rsplit("/")
        flags.append(flag[(len(flag)-1)])
        l=l+1
      #print(flags)

      flags2=[]
      m=0
      while (m<len(flags)):
        test = flags[m].rsplit(".")
        test2 = test[0].lower()
        if (test2 == "world"):
          test2 = "gb"
        flags2.append(test2)
        m=m+1
      #print(flags2)
      j=0
      while(j<len(headings)):
        links=links + ":flag_"+flags2[j]+": " "<" + headings[j] + ">" +"\n"
        j = j+1
    except:
      links = "No streams were found"
      

    
    print(len(flags2))
    print(team1)
    print(team2)
    print(links)
    print(matchlink)
    if links=="":
      links = "No streams were found"


    embed=discord.Embed(title="CSGO Stream links", color=0xff8800)
    embed.add_field(name="The game found", value=team1 + " vs " + team2, inline=True)
    embed.add_field(name="Streams available", value = links, inline=False)
    embed.add_field(name="Game page info", value=matchlink, inline=False)

   
    
    

    return(embed, team1, team2, links, matchlink)

  except:
    embed=discord.Embed(title="No CSGO streams / games were found", color=0xff8800)
    embed.add_field(name="What you can try", value="You can try using !nextcsgo to see if there are any games coming up", inline=True)
    embed.add_field(name="Links", value="OG Liquipedia:  https://liquipedia.net/counterstrike/OG\nOG HLTV: https://www.hltv.org/team/10503/og#tab-matchesBox" , inline=False)
    
    return(embed, "No games found","No games found","No games found","No games found")
