#import selenium
#import json
import requests
import pandas as pd
import re
import warnings

from bs4 import BeautifulSoup
from datetime import datetime

res = {}
resList = []

editDate = '030321'

warnings.filterwarnings('ignore', message='Unverified HTTPS request')

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.google.com/',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

baseUrl = 'https://www.polri.go.id/tentang-satwil'

result = requests.get(baseUrl, headers = headers, verify = False)
soup = BeautifulSoup(result.content, 'html.parser')

pList = soup.findAll('p', {'class':'m-0'})

for p in pList:
    #print(p)

    addr = p.get_text(separator='<br>').strip()

    x = addr.split('<br>')
    #print(x)

    resList.append(x)

print(resList)

df = pd.DataFrame(resList, columns = ['Satuan kerja', 'Alamat', 'Nomor telepon'])
df.to_csv('satkerPolri_on_' + editDate + '.csv')

#print(soup)