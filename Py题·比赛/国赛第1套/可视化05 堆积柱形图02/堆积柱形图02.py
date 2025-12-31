import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar

df = pd.read_csv(
    r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第01套\01_app_log\整理后的文件\behavior2023-01-01.csv",
    encoding='utf-8')
Data1 = df["type"].value_counts().to_dict()

class_type = list(Data1.keys())
# print(class_type)
class_num = list(Data1.values())
# print(class_num)

bar = (
    Bar()
    .add_xaxis(['2023-01-01'])
    .add_yaxis(class_type[0], [class_num[0]], stack='stack1')
    .add_yaxis(class_type[1], [class_num[1]], stack='stack1')
    .add_yaxis(class_type[2], [class_num[2]], stack='stack1')
    .set_global_opts(
        title_opts=opts.TitleOpts(title='上网模式类型分布'),
        xaxis_opts=opts.AxisOpts(name="设备类型"),
        yaxis_opts=opts.AxisOpts(name="数量")
    )
)
bar.render("网站访客上网模式统计堆积柱形图.html")
