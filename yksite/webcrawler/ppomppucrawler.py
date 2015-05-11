# -*- coding: utf-8 -*-
import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

http = httplib2.Http()
status, response = http.request('http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')

soup = BeautifulSoup(response, parse_only=SoupStrainer('a', href=True))
cnt = 0
for link in soup.find_all('a'):
    cnt = cnt+1
    print '<%d>' % cnt
    
    if link.has('font') and link.font['class']=='list_title':
        # 제목 추출
        print 'title ::: %s' % link.text
        
    # 내용 링크 추출
    print 'href ::: %s' % link['href']