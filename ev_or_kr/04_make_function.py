from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

# tr을 너미면 [{}, {}, {}]
def parse_tr(tr):
    ths = tr.find_all("th")
    tds = tr.find_all("td")

    sido = ths[0].text
    region = ths[1].text

    replace_brackets = lambda x: x.replace("(", "").replace(")","").split(" ")
    form = lambda a,b,c,d,e: {"sido":a, "region":b, "sep1":c, "sep2":d, "value":e}

    민간공고대수 = replace_brackets(tds[2].text)
    접수대수 = replace_brackets(tds[3].text)
    출고대수 = replace_brackets(tds[4].text)
    출고잔여대수 = replace_brackets(tds[5].text)

    print(민간공고대수)

    l = [
        form(sido, region, "민간공고대수", "우선순위", int(민간공고대수[0])),
        form(sido, region, "민간공고대수", "법인과기관", int(민간공고대수[1])),
        form(sido, region, "민간공고대수", "택시", int(민간공고대수[2])),
        form(sido, region, "민간공고대수", "우선비대상", int(민간공고대수[3])),
        form(sido, region, "접수대수", "우선순위", int(민간공고대수[0])),
        form(sido, region, "접수대수", "법인과기관", int(민간공고대수[1])),
        form(sido, region, "접수대수", "택시", int(민간공고대수[2])),
        form(sido, region, "접수대수", "우선비대상", int(민간공고대수[3])),
        form(sido, region, "출고대수", "우선순위", int(민간공고대수[0])),
        form(sido, region, "출고대수", "법인과기관", int(민간공고대수[1])),
        form(sido, region, "출고대수", "택시", int(민간공고대수[2])),
        form(sido, region, "출고대수", "우선비댓ㅇ", int(민간공고대수[3])),
        form(sido, region, "접수잔여대수", "우선순위", int(민간공고대수[0])),
        form(sido, region, "접수잔여대수", "법인과기관", int(민간공고대수[1])),
        form(sido, region, "접수잔여대수", "택시", int(민간공고대수[2])),
        form(sido, region, "접수잔여대수", "우선비댓ㅇ", int(민간공고대수[3]))
    ]

    return l

if __name__ == '__main__':

    f = open("local_info.html", encoding="utf-8")
    page_string = f.read()
    bsobj = BeautifulSoup(page_string)
    table = bsobj.find("table", {"class": "table_02_2_!"})
    trs = table.find("tbody").find_all("tr")

    m = []
    for tr in trs:
        row = parse_tr(tr)
        m += row
    #print(m)

    df = pd.DataFrame(m)
    #print(df)
    #df.to_excel("soudl_busan.xlsx")
    df.to_excel("all_sido.xlsx")
