from bs4 import BeautifulSoup

f = open("local_info.html", encoding="utf-8")
page_string = f.read()
bsobj = BeautifulSoup(page_string, "html.parser")
table = bsobj.find("table", {"class":"table_02_2_1"})
trs = table.find("tbody").find_all("tr")
tr = trs[0]
ths = tr.find_all("th")
tds = tr.find_all("td")

sido = ths[0].text
region = ths[1].text

민간공고대수 = tds[2]
접수대수 = tds[3]
출고대수 = tds[4]
출고단여대수 = tds[5]

