import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Line

df = pd.read_excel(r'',)
x_data = df['时间']
y_data = df['浏览量']

line = (
  Line()
  .add_xaxis(x_data.tolist())
  .add_yaxis('网页浏览量',y_data.tolist())
)
line.render('不同时间段网页浏览量统计曲线图.html')