import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts

df = pd.read_excel(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第01套\03_中国地区数据\dim_area.xlsx",header=None)

group_Data = df[2].value_counts().to_dict()

# 验证Data
# print(group_Data)

y = []
x = []
for sp_ , num_ in group_Data.items():
    x.append(sp_)
    y.append(num_)

# 验证x轴数据，y轴数据
# print(sp)
# print(num)
bar = Bar()
bar.add_xaxis(x)
bar.add_yaxis('数据',y)
bar.render()
