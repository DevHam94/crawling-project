import requests

url = "https://openapi.naver.com/v1/search/blog.json"
res = requests.get(url, headers={"X-Naver-Client-Id": "",
                                 "X-Naver-Client-Secret":""})
r = res.json()

