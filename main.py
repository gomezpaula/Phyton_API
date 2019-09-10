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
from requests import resp

SCOPES = ['https://www.googleapis.com/auth/drive']
CLIENT_SECRET_FILE = 'credentials.json'
APPLICATION_NAME = 'Drive API Python Quickstart'
authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
credentials = authInst.getCredentials()
http = credentials.authorize(httplib2.Http())
drive_service = discovery.build('drive', 'v3', http=http)


#Crear/subir un archivo
def uploadFile(filename,filepath,mimetype):
    file_metadata = {'name': filename}
    media = MediaFileUpload(filepath, mimetype=mimetype)
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    resp = requests.get('    ')
if resp.status_code != 200:
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
for t_item in resp.json():    
    print('File ID: {} File name: {}' .format (file.get('id'), file.get('description')))

nombreArchivo = input("Nombre archivo: \n")
uploadFile(nombreArchivo,'descarga.jpg','image/jpeg')
