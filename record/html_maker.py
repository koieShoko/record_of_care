import datetime
import locale

class Html_maker():
    def make_ul(self, labels, values, id):
        html_sentence ='<ul id="{}">'.format(id) 
        for label, value in zip(labels,values):
            html_str = "<li><label>{}</label>{}</li>".format(label, value)
            html_sentence += html_str
        html_sentence += '</ul>'
        return html_sentence


class Date_formatter():
    def __init__(self):
        pass
    def output_day_of_the_week(self, y, m, d ):
        y = int(y)
        m = int(m)
        d = int(d)
        locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
        dt = datetime.datetime(y,m,d)
        result = dt.strftime('%a')
        return result
    def date_translate_to_ja(self, str_date):
        date_list = str_date.split("-")
        y               = int(date_list[0])
        m               = int(date_list[1])
        d               = int(date_list[2])
        day_of_the_week = self.output_day_of_the_week(y,m,d) 
        result = "{}年{}月{}日({})".format(y, m, d, day_of_the_week)
        return result