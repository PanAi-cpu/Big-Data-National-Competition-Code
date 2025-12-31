import pandas as pd

# 一行代码转换
# pd.read_csv(
#     r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第06套\模块三处理后的数据\每个城市的最高气温.csv").to_json(
#     r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第06套\模块三处理后的数据\转为js后\每个城市的最高气温.js",
#     orient='records', indent=2, force_ascii=False)
# orient='records' 指定JSON的格式结构;indent=2 使用2个空格进行缩进，使JSON文件更易读;force_ascii=False 保持原字符显示（如："北京"）;
# 'records',用于图表数据；'index'按索引组织，字典查找式；'columns' 按列组织，列运算；'values' 纯值数组，矩阵计算
pd.read_csv(
    r"E:\桌面\front-end\Vue.js + ECharts\可视化\成都1~12个月最高最低气温堆叠图\avg_temperature_tem.csv").to_json(
    r"E:\桌面\front-end\Vue.js + ECharts\可视化\成都1~12个月最高最低气温堆叠图\avg_temperature_tem.js",
    orient='records', indent=2, force_ascii=False)
