# the imports
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io
import os
import datetime
from fillpdf import fillpdfs
from PyPDF2 import PdfReader, PdfWriter
import datetime

CLIENT_ID = 'x'
CLIENT_SECRET = 'y'
REFRESH_TOKEN = 'z'

# Creates a credentials object that holds the authentication details

creds = Credentials(
    None, 
    refresh_token = REFRESH_TOKEN, 
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    token_uri = 'https://oauth2.googleapis.com/token'
)

# Builds google drive api. Requests drive api, the latest v3 version and uses creds to authenticate requests
drive_service = build('drive', 'v3', credentials=creds)

folder_id = '1bsiApSUZ50U1p1PdmRCtY0S-pTXn0DcA'

def get_file_ids(drive_service, folder_id):
    results = drive_service.files().list(
        q=f"'{folder_id}' in parents and trashed = false",
        fields = "files(id, name)"
    ).execute()
    files = results.get('files', [])
    return files

files = get_file_ids(drive_service, folder_id)
file_list = [f['id']for f in files]
file_dict = {f['id']: f['name'] for f in files}
print(file_list)
print(file_dict)

name_list = list(file_dict.values())
print(name_list)

save_folder = r"C:\Python Projects\NHS API\Downloaded Forms"

def downloader_to_folder(drive_service, folder_id, save_folder):
    os.makedirs(save_folder, exist_ok = True)
    more_files = get_file_ids(drive_service, folder_id)

    for f in more_files:
        file_id = f['id']
        file_name = f['name']

        save_path = os.path.join(save_folder, file_name)
        print(f"Downloading {file_name} to {save_path}")

        request = drive_service.files().get_media(fileId=file_id)
        fh = io.FileIO(save_path, 'wb')
        downloader = MediaIoBaseDownload(fh, request)

        done = False
        while not done:
            status, done = downloader.next_chunk()

        fh.close()
        print(f"Download complete to {save_path}")

downloader_to_folder(drive_service, folder_id, save_folder)

for form in os.listdir(save_folder):
    file_path = os.path.join(save_folder, form) # this returns the file names not the paths
    reader = PdfReader(file_path)
    fields = fillpdfs.get_form_fields(file_path)
    print(f"{form} fields are: {fields}")

important_fields = ['patient_forename', 'patient_surname', 'B', 'test_request']
all_patient_data = []

for form_file in os.listdir(save_folder):
    file_path = os.path.join(save_folder, form_file)
    fields = fillpdfs.get_form_fields(file_path)
    extracted_data = {k:fields.get(k,'') for k in important_fields}
    all_patient_data.append(extracted_data)
    print(f"{form_file} has {extracted_data}")

for patient in all_patient_data:
    print(patient)

import csv

csv_file_path = os.path.join(save_folder, 'patients_data.csv')

with open(csv_file_path, mode='w', newline='', encoding = 'utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = important_fields)
    writer.writeheader()
    writer.writerows(all_patient_data)

print(f"Data saved to {csv_file_path}")





