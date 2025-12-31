import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Page, WordCloud
from pyecharts.globals import SymbolType

df = pd.read_csv(
    r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第01套\01_app_log\整理后的文件\behavior2023-01-01.csv",
    encoding='utf-8')

Data1 = df["url"].value_counts().to_dict()

wordcloud_data = [(word, count) for word, count in Data1.items()]

def wordcloud() -> WordCloud:
    c = (
        WordCloud()
        .add('',wordcloud_data,word_size_range=[20,100],shape='cardioid')
        .set_global_opts(title_opts=opts.TitleOpts(title = 'WordCloud'))
    )
    return c


wordcloud().render('不同域名用户访问统计词云.html ')