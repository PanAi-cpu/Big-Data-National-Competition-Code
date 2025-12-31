from pyecharts.charts import Bar
bar = Bar()
bar.add_xaxis(["数学", "物理", "化学", "英语"])
bar.add_yaxis("成绩", [70, 85, 95, 64])
bar.render()