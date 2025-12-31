# 对于第三套试卷模块三的数据处理
import pandas as pd

# 一：分别统计各个商圈的的酒店总数，进行倒序排序展示前五名；
# 先按商圈进行分组并统计出每个商圈的酒店总数，后对商圈进行倒序展示
df = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第03套\hotel.csv"
                 , encoding='gbk')
count_hotelData = df.groupby('商圈')['住宿场所名称'].count()
sort_hotelData = count_hotelData.sort_values(ascending=False)
print(sort_hotelData.head(5))

# 统计各个商圈酒店的平均房间数，进行正序排序展示前五名；
avg_hotelData = (df.groupby('商圈')['房间数']
                 .mean()
                 .rename('平均酒店房间数量')
                 .reset_index()
                 .sort_values('平均酒店房间数量')
                 .head(5))
print(avg_hotelData)

# 统计所有五星级酒店的平均评分。
print('\n')
avg_sore = df[df['星级'] == '五星级']['评分'].mean()
print(f'五星级酒店的平均评分：{avg_sore.round(2)}')