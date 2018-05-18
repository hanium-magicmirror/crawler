#squre jjshouse
import requests
from bs4 import BeautifulSoup
import urllib.request as rq

def download(URL, number):
    fullname = str(number) + '.png'
    rq.urlretrieve(URL, fullname)

total_page_num = 2
image_name_num = 0
for page in range(total_page_num):
    URL = "https://www.jjshouse.com/Cheap-Wedding-Dresses-c2/Square-Neckline_p8i800/"
    sourcecode = requests.get(URL).text
    soup = BeautifulSoup(sourcecode, 'html.parser')
    image_datas = soup.find_all("div", class_="pic")
    for image in image_datas:
        if(image.find("a").find("img")["src"][0] == 'h'):
            download(image.find("a").find("img")["src"], image_name_num)
            image_name_num = image_name_num + 1

        else:
            pass
    #download()


