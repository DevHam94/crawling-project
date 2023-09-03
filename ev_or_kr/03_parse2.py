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

replace_brackets = lambda x: x.replace("(", "").replace(")","").split(" ")

민간공고대수 = replace_brackets(tds[2].text)
접수대수 = replace_brackets(tds[3].text)
출고대수 = replace_brackets(tds[4].text)
출고잔여대수 = replace_brackets(tds[5].text)

print(민간공고대수)
print(접수대수)
print(출고대수)
print(출고잔여대수)