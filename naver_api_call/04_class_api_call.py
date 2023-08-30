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

    def get_paging_call(self, keyword, quantity):
        if quantity > 1100:
            # quantity = 1100
            exit("Error 최대 요청할 수 있는 건수는 1100건 입니다.")

        repeat = quantity // 100  # 1000총 10번
        result = []
        for i in range(repeat):
            start = i * 100 + 1
            # 101
            if start > 1000:
                start = 1000
            print(f"{i + 1}번 반복 합니다. start:{start}")
            r = self.call_api(keyword, start=1, display=100)
            print(r['items'][0])
            result += r['items']
        return result

    def blog(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/blog.json"
        return self.get_paging_call(keyword, quantity)

    def news(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/news.json"
        return self.call_api(keyword)

if __name__ == '__main__':
    naver_search_api = NaverSearchApi()
    r = naver_search_api.news("사당역 족발집", 1000)
    print(r['items'][0])