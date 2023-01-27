#!/usr/bin/python
#PYTHON Google Excell Usage
import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)

file = gspread.authorize(creds)
workbook = file.open("budget")
sheet = workbook.sheet1

#cell = sheet.find(row_name)
#row_values = sheet.row_values(cell.row)
#print(row_values)

#ROW find function
def row_find():
    row_name = input("Please specify row name:\n")
    cell = sheet.find(row_name)
    row_values = sheet.row_values(cell.row)
    print(row_values[1])

row_find()

















#for cell in sheet.range('A2:A5'):
#    print(cell.value)
#print(sheet.acell('A2').value)

#update data
#sheet.update_acell('A2', 'NEWVALUE')