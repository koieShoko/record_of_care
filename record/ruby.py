import requests
import xml.etree.ElementTree as ET

class Ruby_maker():
    '''yahooのルビ振りAPIを利用して、ルビのついたHTML文を作成する
    https://developer.yahoo.co.jp/webapi/jlp/furigana/v1/furigana.html'''
    target_url = "https://jlp.yahooapis.jp/FuriganaService/V1/furigana"
    api_key    = "dj00aiZpPVIwV0ZrbkJJNkJZSSZzPWNvbnN1bWVyc2VjcmV0Jng9MTU-"
    def __init__(self):
        self.grade = '1'
    def set_target_url(target_url):
        self.target_url = target_url
    def set_api_key(api_key):
        self.api_key    = api_key
    def set_grade(grade):
        '''ルビの適応範囲を指定する。1(全漢字) 〜 8(常用漢字以外)'''
        self.grade      = str(grade)
    def output(self, sentence):
        data = {
            "appid"     : self.api_key,
            "grade"     : self.grade,
            "sentence"  : sentence,
        }
        response    = requests.post(self.target_url, data=data)
        root        = ET.fromstring(response.text)
        ruby_dict   = {}
        text        = []

        for line in root:
            if len(line) == 0:#変換の対象がない時は処理しない
                return
            for word_list in line[0]:
                kanzi = word_list[0].text
                text.append(kanzi)
                if len(word_list) > 1:#ルビがあれば
                    ruby = word_list[1].text
                    ruby_dict[kanzi] = ruby
        html_list=[]      
        for word in text:
            if word in list(ruby_dict.keys()):
                html_list.append("<ruby> {} <rp>".format(word))
                html_list.append("（</rp><rt>{}</rt><rp>）</rp></ruby>".format(ruby_dict[word]))        
            else:
                html_list.append(word)
        html_text="".join(html_list)          
        return html_text

