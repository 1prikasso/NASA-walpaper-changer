'''
Thats the project, that get picture of a day from 
https://apod.nasa.gov/ website and change the desktop image

Author: Oleksandr 
inst: @1prikasso
'''

from datetime import date
from bs4 import BeautifulSoup
import requests
import os
import time
import tk

# import tkMessageBox


NASA = 'https://apod.nasa.gov/apod/'



class GetImage():
    def __init__(self, WEB):
        self.WEB = WEB
    
    def download_image(self):
        r = requests.get(self.WEB, allow_redirects=True)
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
        links = soup.find_all('a')

        image = self.WEB+(links[1].find('img')['src'])
        r = requests.get(image)

        open('apod_nasa.jpg', 'wb').write(r.content)
        
        return (os.path.abspath('apod_nasa.jpg'))

class SetImage():
    def __init__(self, image):
        self.image = image
        
    def set_image(self):
        os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri "+self.image)
        
while True:
    try:
        SetImage(GetImage(NASA).download_image()).set_image()

        local_time = time.ctime()
        print(local_time, ' was changed wallpaper')
        
        time.sleep(86400)
    except requests.exceptions.MissingSchema:
        for i in range(15):
            print('!something wrong with Nasa request!\nDm me in the instagram: @1prikasso')
            time.sleep(0.7)
        break