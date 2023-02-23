####downloading file from web using requests module

import requests

site = 'https://automatetheboringstuff.com/files/rj.txt'

res = requests.get(site)

#   res.text
#   res.text[:250]
#   res.status_code
#   res.status_code == requests.code.ok


### check error

#res = requests.get('https://inventwithpython.com/page_that_does_not_exist')

#res.raise_for_status()
# 다운로드가 잘못되었을 때 프로그램이 이를 중단 하는 좋은 방법이다. 예기치 않은 오류가 발생하면 그 즉시 프로그램을 중지하고자 할때 유용
# 실패한 다운로드가 프로그램의 주된 문제가 아닌 경우 try except로 감싸서 프로그램 충돌 없이 이 오류를 처리하도록 할 수 있다.

import requests

res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc: #except 문법 주의
    print(f'There was a problem: {exc}')

# AttributeError: partially initialized module 'requests' has no attribute 'get' (most likely due to a circular import)
#파일명이 requests라서 오류 생김 주의!


#### store file

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet','wb')

for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()

