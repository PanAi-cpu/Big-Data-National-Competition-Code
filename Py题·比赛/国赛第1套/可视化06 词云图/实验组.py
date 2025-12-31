import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import WordCloud

df = pd.read_csv(
    r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第01套\01_app_log\整理后的文件\behavior2023-01-01.csv",
    encoding='utf-8')

Data1 = df["url"].value_counts().to_dict()
wordcloud_data = []
for url, count in Data1.items():
    # 提取主域名
    if '://' in url:
        domain = url.split('://')[1].split('/')[0]
    else:
        domain = url.split('/')[0]
    wordcloud_data.append((domain, count))

print(wordcloud_data)

# 创建词云图
wordcloud = (
    WordCloud(init_opts=opts.InitOpts(width="1200px", height="800px"))
    .add(
        series_name="网站访问",
        data_pair=wordcloud_data,
        word_size_range=[20, 80],
        shape="circle"  # 词云形状：circle, cardioid, diamond, triangle, etc.
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="热门网站访问量词云图",
            title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
)

wordcloud.render('实验组.html')






































