import requests

url = "https://finance.naver.com/item/main.naver?code=00"
res = requests.get(url)
print(res.text)