from pyecharts import options as opts
from pyecharts.charts import Bar

devices = ["手机", "平板", "电脑"]
mobile_visits = [120, 150, 180]
tablet_visits = [80, 100, 120]
pc_visits = [200, 250, 300]

bar = (
    Bar()
    .add_xaxis(["2021年", "2022年", "2023年"])  # 横轴为年份
    .add_yaxis("手机", mobile_visits, stack="stack1")  # 堆叠组名为 stack1
    .add_yaxis("平板", tablet_visits, stack="stack1")
    .add_yaxis("电脑", pc_visits, stack="stack1")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="不同设备类型的访问次数"),
        xaxis_opts=opts.AxisOpts(name="年份"),
        yaxis_opts=opts.AxisOpts(name="访问次数"),
        legend_opts=opts.LegendOpts(is_show=True)
    )
)
bar.render("stacked_bar_chart.html")
