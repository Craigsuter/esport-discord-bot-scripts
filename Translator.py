#imports
from googletrans import Translator, LANGUAGES
#imports
import discord
from dotenv import load_dotenv
load_dotenv()


def translations(nexttrans, author, msgID):
      #Setting up the translator service
      translator = Translator(service_urls=['translate.googleapis.com'])
      texttotranslate = str(nexttrans)
      translation = translator.translate(texttotranslate, dest='en')
      language = ((LANGUAGES.get(translation.src)).capitalize())
      detection1 = translator.detect(texttotranslate)
      confidence = str(detection1.confidence * 100) + "%"
      #Getting translation data
      translation= translation.text
      #sending message
      titleoftrans = "The following message was sent by: " + str(author)
      #Creating translation embed
      embed=discord.Embed(title=titleoftrans,color=0xff8800)
      embed.set_thumbnail(url=#SetAnImageHere)
      embed.add_field(name="The language the message was sent in", value = language + "\n Google's confidence on language: " + confidence, inline=False)
      embed.add_field(name="The original message was", value=nexttrans, inline=True)
      embed.add_field(name="The translated version", value=translation,inline=False)
      embed.add_field(name="Link to message", value="[The message can be found here]("+msgID+")", inline=False)
      
      return(embed)
    
  #This script will use a Google Translate API to return the message translated, useful for moderating multi-lingual servers, also find: https://top.gg/bot/871841361375154227#/
  #On your requirements.txt fild for python, be sure to include SPECIFICALLY: googletrans==3.1.0a0 - as this is the version I have found to work, and wasn't able to use the latest one
