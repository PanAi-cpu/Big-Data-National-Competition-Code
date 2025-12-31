import pandas as pd

df = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第03套\hotel.csv",
                 encoding='gbk')

valid_df = df.dropna(subset=['商圈'])
hotel_counts = (valid_df.groupby('商圈')['住宿场所名称']
                .count()
                .sort_values(ascending=False))

print(hotel_counts.head(5))

# 2、统计各个商圈所有酒店的平均评分排名，进行倒序排序展示前五名；

hotelScore_mean = (valid_df.dropna(subset=['评分'])
                   .groupby('商圈')['评分']
                   .mean()
                   .sort_values(ascending=False))

print(hotelScore_mean.head(5))

# 3、统计各个商圈酒店的平均房间数，进行正序排序展示前五名；

hotelRoom_mean = (valid_df.dropna(subset=['房间数'])
                  .groupby('商圈')['房间数']
                  .mean()
                  .sort_values())

print(hotelRoom_mean.head(5))
