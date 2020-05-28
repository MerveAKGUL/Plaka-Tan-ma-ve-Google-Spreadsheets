# OPENALPR Kullanarak Plaka Tespiti ve Google Tablolara Kayıt (Raspberry Pi)

## **Projenin Amacı**
  Raspberry Pi kullanarak OpenALPR kütüphanesi ile araç plakalarını okuyup, karakterlere çevirmek ve elde edilen veriyi google tablolara kaydetmek. 

![Demo](plate_recognition.gif)

## **Kullanılan Donanım**
-Rasberry Pi 3B <br/>
-SD Kart <br/>
-Raspberry Pi Camera <br/>
-HDMI Kablo <br/>
## **Gerekli Python Kütüphaneleri**
```
-cv2 <br/>
-datetime <br/>
-requests <br/>
-gspread <br/>
-oauth2client.service_account <br/>
```
## **Kurulum**
1. [openalpr](https://cloud.openalpr.com/) adresinden bir hesap oluşturun ve gizli anahtarı test.py kod dosyasına ekleyin.
2. Kayıtlar için bir Google Drive da dökümanımızı oluşturalım. [(Gerekli adımlar için..)](plate_recognition)
## **Çalıştırma**
Raspberry terminal üzerinden <br/>
`test.py`
