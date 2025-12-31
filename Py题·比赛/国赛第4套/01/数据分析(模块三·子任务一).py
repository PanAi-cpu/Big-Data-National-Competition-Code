# （1）对各品牌进行统计，进行正序排序展示前十名；
# （2）对各商品特征进行统计，进行正序排序前六名；
# （3）统计各品牌的销量，进行正序排序展示前五名。
import pandas as pd

df = pd.read_csv(r'E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第04套\商城\清洗03.csv',
                 encoding="utf-8")
# 按价格降序排序，但保留整个DataFrame
df_price = df.sort_values('价格', ascending=False)
# 取前10行（包含所有列）
df_top10 = df_price.head(10)
df_top10.to_csv(r'E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第04套\商城\价格前10.csv', index=False,
                encoding='utf-8-sig')

# 按价格降序排序，但保留整个DataFrame
df_views = df.sort_values('浏览量', ascending=False)
# 取前6行（包含所有列）
df_top6 = df_views.head(6)
df_top6.to_csv(r'E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第04套\商城\浏览量前6.csv', index=False,
               encoding='utf-8-sig')

df_sales = df.sort_values('销量', ascending=False)
# 提取前5行
df_top5 = df_sales.head(5)
df_top5.to_csv(r'E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第04套\商城\销售前5.csv', index=False,
               encoding='utf-8-sig')
