import pandas as pd
from pyecharts import options
from pyecharts.charts import Line


# 筛选出节假日的访问和工作日的访问，在把工作日的访问详细筛成不同时间段的访问
# 得到节假日的访问量和工作日不同时间段的访问量
df = pd.read_excel(r'')

# 设计的时候因该选择双折线图

y_data1 = df['节假日']
y_data2 = df['工作日']

x_data = df['时间段数据']

line = (
    Line()
    .add_xaxis(xaxis_data=x_data.tolist())
    .add_yaxis(series_name='折线图1',y_axis = y_data1.tolist())
    .add_yaxis(series_name='折线图2',y_axis = y_data2.tolist())
)
line.render('节假日和工作日各时间段网页浏览量统计曲线图.html')
