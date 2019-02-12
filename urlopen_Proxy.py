import urllib2

proxy_handler = urllib2.proxy_handler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib2.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')

opener = urllib2.build_opener(proxy_handler, proxy_auth_handler)
# install_opener(), urlopen() 함수 대신에 직접 open() 함수를 사용할 수도 있음
u = opener.open('http://www.example.com/login.html')
