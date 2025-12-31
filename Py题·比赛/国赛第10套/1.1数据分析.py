import pandas as pd

# 1，分别统计各个商圈的的酒店总数，进行倒序排序展示前五名；

df = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第03套\hotel.csv",
                 encoding='gbk')
hotel_valid = df.dropna(subset=['商圈'])
hotel_count = (hotel_valid.groupby('商圈')['住宿场所名称']
               .count()
               .sort_values(ascending=False))

print('\n各个商圈的的酒店总数,倒序展示前五名:')
print(hotel_count.head(5))

# 2、统计各个商圈所有酒店的平均评分排名，进行倒序排序展示前五名；

score_mean = (hotel_valid.dropna(subset=['评分'])
              .groupby('商圈')['评分']
              .mean()
              .sort_values(ascending=False))

print('\n各个商圈所有酒店的平均评分排名,倒序展示前五名:')
print(score_mean.head(5))

# 3、统计各个商圈酒店的平均房间数，进行正序排序展示前五名；
hotelHose_mean = (hotel_valid.dropna(subset=['房间数'])
                  .groupby('商圈')['房间数']
                  .mean()
                  .sort_values(ascending=True))

print('\n各个商圈酒店的平均房间数,正序展示前五名:')
print(hotelHose_mean.head(5))