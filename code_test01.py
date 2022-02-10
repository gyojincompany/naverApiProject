import urllib.request

client_id = '_Zgd7DjzVM9oRwOEi2Ro'
client_secret = 'IV7LzYz4_i'

url1 = "https://openapi.naver.com/v1/search/news.json?query='BTS'&start=1&display=100"
url2 = "https://openapi.naver.com/v1/search/news.json?query='BTS'&start=101&display=100"
url3 = "https://openapi.naver.com/v1/search/news.json?query='BTS'&start=201&display=100"

req = urllib.request.Request(url) # 네이버서버에 보낼 요청객체를 생성
req.add_header("X-Naver-Client-Id",client_id) # 위에서 만들어진 요청객체에 client_id를 포함시킴
req.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(req) # 네이버서버에 요청객체 req를 전달하여 응답을 받아 response에 저장
print(response) # 200이 오면 정상승인

ret = response.read().decode('utf-8')
print(ret)