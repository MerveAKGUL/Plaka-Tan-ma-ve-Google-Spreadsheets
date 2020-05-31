#Gerekli kütüphaneleri yüklüyoruz
import cv2
import datetime
import requests
import base64
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):  # s tuşu ile fotoğraf çekebiliriz
        an = datetime.datetime.now()
        isim=datetime.datetime.strftime(an,'%d%m%Y_%H%M')
        cv2.imwrite("fotograflar/"+ str(isim) + ".jpg",frame)
        break
capture.release()
cv2.destroyAllWindows()

IMAGE_PATH = ("fotograflar/"+ str(isim) + ".jpg")
SECRET_KEY = 'YOUR OPENALPR SECRET KEY' #OPENALPR Secret Key bu alana girilebilir. 

with open(IMAGE_PATH, 'rb') as image_file:
    img_base64 = base64.b64encode(image_file.read())

url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=tr&secret_key=%s' % (SECRET_KEY) #country değiştirilebilir
r = requests.post(url, data = img_base64)
try:
    # Google ile bağlantı sağlayacak kodlar:
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive.file', "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('xxx.json', scope) #Google API den indirdiğiniz JSON dosyasının adını belirtiyoruz
    client = gspread.authorize(creds)
    sheet = client.open("Plakalar").sheet1 #Google Drive da oluşturduğumuz tablonun adını yazıyoruz
    data = sheet.get_all_records()
    row = (len(data) + 2)
    sheet.update_cell(row, 1, datetime.datetime.strftime(an, '%d/%m/%Y')) #Tablonun 1. sütununa tarih bilgisini yazıyor.
    sheet.update_cell(row, 2, datetime.datetime.strftime(an, '%X')) #Tablonun 2. sütununa saat bilgisini yazıyor.
    sheet.update_cell(row, 3, (r.json()['results'][0]['plate'])) #Tablonun 3. sütununa OPENALPR sunucusundan gelen "plaka" bilgisini yazıyor.
    print("İşlem Başarılı")
except:
    print("Plaka Okunamadı")




