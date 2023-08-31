import requests

url = "https://www.ev.or.kr/portal/localInfo"
data = requests.get(url)
print(data.text)