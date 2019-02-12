import urllib2

# HTTP 기본 인증 요청을 위한 핸들러 생성
auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(realm='PDQ Application',
                          uri='https://mahler:8092/site-updates.py',
                          user='klem',
                          passwd='kadidd!ehopper')
opener = urllib2.build_opener(auth_handler)
.
# 디폴트 오프너로 설정하면 urlopen() 함수로 요청 가능
urllib2.install_opener(opener)
u = urllib2.urlopen('http://www.example.com/login.html')
