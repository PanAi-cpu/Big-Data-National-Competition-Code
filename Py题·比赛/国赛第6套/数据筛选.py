# 2011~2021的数据
# 1，筛选出每个城市的最高温
# 2，进行降序排序，将新建一个csv表格将这些数据放进去。

import pandas as pd

df = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第06套\clean_day.csv", encoding='')
# 分组并算出最高温
city_max_temp = df.groupby('city')['hightest_tem'].max().reset_index()
city_max_temp.to_csv(
    r'E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第06套\模块三处理后的数据\每个城市的最高气温.csv',
    index=False, encoding='utf-8-sig')
# 排序
df2 = pd.read_csv(
    r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第06套\模块三处理后的数据\每个城市的最高气温.csv",
    encoding='utf-8')
# 按降序排序，但保留整个DataFrame
df_headMax = df2.sort_values('hightest_tem', ascending=False)
# 取前10行（包含所有列）
df_top10 = df_headMax.head(10)
df_top10.to_csv(
    r'E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第06套\模块三处理后的数据\最高气温前10的城市.csv',
    index=False, encoding='utf-8-sig')
