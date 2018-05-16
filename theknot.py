# -*- coding: utf-8 -*-
# https://www.theknot.com/fashion/sweetheart-wedding-dresses
import requests
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]="3"
import urllib.request
from bs4 import BeautifulSoup

def main():
    global dir

    print("Type Your Neck-line Type Number\n")
    print("1. V-Neck\n")
    print("2. Sweetheart\n")
    print("3. Halter\n")
    print("4. Square\n")
    number = input("input: ")
    number = int(number)
    if number == 1:
        dir = 'v-neck'
    elif number == 2:
        dir = 'sweetheart'
    elif number == 3:
        dir = 'halter'
    elif number == 4:
        dir = 'square'
    else:
        print("Nothing to Search")
        return
    print("input the start number of your file")
    start = input("input: ")
    start = int(start)

    # make directory
    if not os.path.exists(dir):
        os.makedirs(dir)
    # set opener
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)

    print('Search ', dir, '\n')
    crawlImages(1,dir, start)
    print("Images crawled Complete!")
    return


# crawling the images per page
def crawlImages(page,type, start):
    print("Start "+str(page)+"page")
    req = requests.get('https://www.theknot.com/fashion/'+type+'-wedding-dresses?page=' + str(page), stream=True)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.select('div.product-result-image > a > picture > img')

    for image in images:
        # change image quality
        url = "https:" + image.get('src')
        url.replace('webp', 'png')
        url = url[:-2] + "100"
        full_name = type + str(start)
        urllib.request.urlretrieve(url, dir + '/' + full_name + '.png')
        start +=1 
    next = soup.select('span.page-next')[0].get('class')
    if "inactive" not in next:
        crawlImages(page+1,type, start)

if __name__ == "__main__":
    main()
