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
    print '<%d> %s' % (cnt, link)
    
    if link.font and 'list_title' in link.font['class']:
        # 제목 추출
        print 'title ::: %s' % link.text
        # 내용 링크 추출
        print 'href ::: %s' % link['href']
        # 내용 읽기
        status, contResponse = http.request('http://www.ppomppu.co.kr/zboard/'+link['href'])
        cont = BeautifulSoup(contResponse, parse_only=SoupStrainer('table'))
        
        for table in cont.find_all('table'):
            print table['class'] if 'class' in table else '((no class tags in table node))'
#             if 'class' in table and 'info_bg' in table['class']:
#                 print 'info ::: %s' % table.text
#             if 'class' in table and 'pic_bg' in table['class']:
#                 print 'cont ::: %s'  % table.text
        
        
        