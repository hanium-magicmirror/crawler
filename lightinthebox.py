#squre lightinthebox


import requests
from bs4 import BeautifulSoup
import urllib.request as rq

def download(URL, number):
    fullname = str(number) + '.png'
    rq.urlretrieve(URL, fullname)

total_page_num = 2
image_name_num = 0
for page in range(total_page_num):
    URL = "https://www.lightinthebox.com/ko/n/square-neck-LAN-TING-BRIDE%C2%AE_c52996?ns=v191611t0&prm=1.4.215.0#nohash"
    sourcecode = requests.get(URL).text
    soup = BeautifulSoup(sourcecode, 'html.parser')
    image_datas = soup.find_all("div", class_="img-box")
    for image in image_datas:
        if(image.find("img")["src"][0] == 'h'):
            download(image.find("img")["src"], image_name_num)
            image_name_num = image_name_num + 1

        else:
            pass
    #download()










