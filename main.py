from __future__ import print_function
import httplib2
import os, io
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import pickle
import os.path
import auth
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
SCOPES = ['https://www.googleapis.com/auth']


#Crear/subir un archivo
def createFile(filename,filepath,mimetype):
   file_metadata = {'name': filename}
media = MediaFileUpload(filepath, 
                        mimetype= mimetype)
file = drive_service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()

if not createFile:
        print('Status:404')
    else:
        createFile('descarga.jpg','descarga.jpg','image/jpeg')
print ('File ID: %s' % file.get('name') % file.get('id')% 'Status:200')



#Buscar un archivo que contenga una palabra enviada por parámetro
def searchFile():

    page_token = None
while True:
    response = drive_service.files().list(q="mimeType='image/jpeg'",
                                          spaces='drive',
                                          fields='nextPageToken, files(id, name)',
                                          pageToken=page_token).execute()
    for file in response.get('files', []):
       
        print ('Found file: %s (%s)' % (file.get('name'), file.get('id')))
    page_token = response.get('nextPageToken', None)
    if page_token is None:
        break

if not items:
        print('Status:404')
    else:
        searchFile('id='"1-9QLUIcs-g8PVxzOfoBzlF5IvrABFOYv"'','fullText contains '"API"'')
        print('Status:200')
        
