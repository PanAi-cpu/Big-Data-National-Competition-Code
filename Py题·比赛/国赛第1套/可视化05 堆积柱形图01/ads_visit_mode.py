import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar

df = pd.read_csv(
    r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第01套\01_app_log\整理后的文件\behavior2023-01-01.csv",
    encoding='utf-8')

Data1 = df["device_type"].value_counts().to_dict()

class_l = []
num_l = []
for class_, num_ in Data1.items():
    class_l.append(class_)
    num_l.append(num_)

bar = (
    Bar()
    .add_xaxis(['设备统计'])
    .add_yaxis(class_l[0], [num_l[0]], stack='stack1')
    .add_yaxis(class_l[1], [num_l[1]], stack='stack1')
    .set_global_opts(
        title_opts=opts.TitleOpts(title='设备类型分布'),
        xaxis_opts=opts.AxisOpts(name="设备类型"),
        yaxis_opts=opts.AxisOpts(name="数量")
    )
)
bar.render("网站访客设备类型统计堆积柱形图.html")