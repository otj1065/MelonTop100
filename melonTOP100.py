import requests as rq
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
now=dt.now()
import time

# 1) 크롤링 하기

# 타겟 사이트 정의
targetSite='https://www.melon.com/chart/index.htm'

# 사이트 연결
# melonrq = rq.get('https://www.melon.com/chart/index.htm')
# print(melonrq) #<Response [406]> => 헤더 정보 때문에 읽어오지 못함

# 헤더 정보 때문에 웹사이트의 데이터를 읽어오지 못할 경우 아래와 같이 헤더 정보를 설정한 후 읽어 와야 한다.
# https://developers.whatismybrowser.com/ 사이트 참고
# https://developers.whatismybrowser.com/useragents/explore/layout_engine_name/trident
header = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
melonrqRetry=rq.get(targetSite, headers=header)
# print(melonrqRetry)

# 사이트 html 읽기
melonht=melonrqRetry.text
# print(melonht)

# beautifulSoup 활용
melonsp=bs(melonht,'html.parser')
# print(melonsp)

# findAll 혹은 select 활용하여 필요한 정보 수집
# class="checkEllipsis"
artists=melonsp.findAll('span',{'class' :'checkEllipsis'})
# 조금 더 까다로움 가공할 때에! - html을 잘 관찰하여서 다른 부분에서 따옴!
# print(artists)
# ellipsis rank01
titles=melonsp.findAll('div',{'class' :'ellipsis rank01'})

# 출력
##print(now.strftime('%Y.%b.%d %a %p %H : %M : %S'))
##print('==========멜론 인기차트 TOP 100==========')
##for i in range(len(titles)):
##     artist = artists[i].text.strip()
##     title = titles[i].text.strip()
##     print('{0:3d}위. {1} - {2}'.format(i+1,artist,title))

# 2) 크롤링한 데이터를 텍스트 파일에 저장

file = open('melonTOP100.txt','w',-1,'UTF-8')

time = now.strftime('%Y.%b.%d %a \n%p %H : %M : %S')
line='==========멜론 인기차트 TOP 100=========='
file.write(time+'\n'+line+'\n')

for i in range(len(titles)):
     artist = artists[i].text.strip()
     title = titles[i].text.strip()
     data = '{0:3d}위. {1} - {2}'.format(i+1,artist,title)
     file.write(data+'\n')

file.close()
print('melonTOP100.txt 파일에 쓰기 완료')

# 3) 텍스트 파일에 저장된 크롤링된 데이터를 화면에 출력

file=open('melonTOP100.txt','r',-1,'UTF-8')
lines=file.readlines()
for line in lines:
     print(line.strip())
     #line,end='' 도 사용가능
file.close()
print('melonTOP100.txt 파일에 읽기 완료')
