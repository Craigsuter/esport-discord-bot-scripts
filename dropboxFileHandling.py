import dropbox
import os

dbx = dropbox.Dropbox(os.getenv('DROPBOX_ACCESS_TOKEN'))

def download_file(filename, savehere):
  dbx.files_download_to_file(savehere, filename)
  #Usage: data = download_file('/dropreminders.txt', 'reminders.txt') - this will download the dropreminders file to the bot, and save it as 'reminders.txt' to access this

  


def upload_file(filename, localfile):

  with open(localfile, "rb") as f:
    dbx.files_upload(f.read(), filename, mode=dropbox.files.WriteMode.overwrite)
    
 #Usage: upload_file('/dropreminders.txt', 'reminders.txt' ) - passing hte file location in the inital spot for where the file will be saved too, this file will overwrite the current file there, writing the reminders.txt file for example
tag
