from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

class EvGoKrSubsidyParser():


    trs = []

    def __init__(self, html_text):
        bsobj = BeautifulSoup(html_text, page_string)
        table = bsobj.find("table", {"class": "table_02_2_!"})
        print(table)
        self.trs = table.find("tbody").find_all("tr")

    # tr을 넘기면 [{}, {}, {}]
    def parse_tr(self, tr):
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

    def parse(self):
        collected_list = []
        for tr in self.trs:
            row = self.parse_tr(tr)
            collected_list += row
        return  collected_list

    def save_to_excel(self, excel_filename):
        df = pd.DataFrame(collected_list)
        # print(df)
        df = pd.DataFrame(collected_list)
        df.to_excel("all_sido.xlsx")


if __name__ == '__main__':

    f = open("local_info.html", encoding="utf-8")
    page_string = f.read()
    bsobj = BeautifulSoup(page_string, "html.parser")
    table = bsobj.find("table", {"class":"table_02_2_1"})
    trs = table.find("tbody").find_all("tr")

    ev_or_kr_parse = EvGoKrSubsidyParser()

    m = []
    for tr in trs:
        row = ev_or_kr_parse.parse_tr(tr)
        m += row
    #collected_list = ev_or_kr_parse.parse()
    #print(collected_list)

    #df = pd.DataFrame(collected_list)
    #print(df)
    #df.to_excel("soudl_busan.xlsx")
    #df.to_excel("all_sido.xlsx")
    #ev_or_kr_parser.save_to_excel("all_sido2.xlsx")