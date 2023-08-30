import requests

class NaverSearchApi():

    api_url = "https://openapi.naver.com/v1/search/blog.json"
    def call_api(self, keyword, start=1, display=10):
        url = f"{self.api_url}?query={keyword}&start={start}&display={display}"
        res = requests.get(url, headers={"X-Naver-Client-Id": "",
                                         "X-Naver-Client-Secret": ""})
        print(res)
        r = res.json()
        return r

    def blog(self, keyword):
        self.api_url = "https://openapi.naver.com/v1/search/blog.json"
        return self.call_api(keyword)

    def news(self, keyword):
        self.api_url = "https://openapi.naver.com/v1/search/news.json"
        return self.call_api(keyword)

if __name__ == '__main__':
    naver_search_api = NaverSearchApi()
    r = naver_search_api.news("사당역 족발집")
    print(r['items'])