# neemepoo
yksung's practicing room, so not for public use, but i opened it!

## 2015-04-23
* 간단한 검색 예제를 검색한 결과를 볼 수 있습니다.
* 검색 조건은 testApp > view.py 의 url에 다음과 같은 조건을 바꾸면 됩니다.
  - search_json.jsp? query = 검색어
  -                  collection = sample_kms / sample_edu / sample_terms 중 하나
  -                  sort = DATE

## 2015-04-16
* 첫 생성!
* yksite 업로드되었습니다. Download Zip 후에 다음과 같이 실행해보세요.(실행전에 python 개발환경과 django가 설치돼야 합니다~)

1. 다운 받은 파일의 압축을 해제한 디렉토리로 이동.
2. yksite/manage.py runserver localhost:[원하는포트번호]
3. 브라우저에서 http://localhost:[입력한포트]
4. hello world가 포함된 페이지가 등장!!
