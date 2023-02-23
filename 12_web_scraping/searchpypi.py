#! python3
# searchpypi.py 몇 가지 검색 결과를 열기

import requests, bs4, sys, webbrowser

print('Searching....')

res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
#'https://pypi.org/search/?q=' 
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')
linkElems = soup.select('.package-snippet')

numOpen = min(5, len(linkElems))
print(numOpen)
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    webbrowser.open(urlToOpen)