import pandas as pd

# 先对数据进行处理，统计各个商圈的酒店总数
df = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第03套\hotel.csv"
                 , encoding='gbk')
hotel_counts = (df.groupby('商圈')['住宿场所名称']
                .count())
# print(hotel_counts)

# 进行可视化处理，用柱状图显示各个商圈的酒店总数
hotel_counts = (hotel_counts
                .sort_values(ascending=False)
                .head(20))
import matplotlib.pyplot as plt

# 预防乱码配置
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 画图
plt.figure(figsize=(10, 6))
bars = plt.bar(hotel_counts.index, hotel_counts.values,
               color='#72231f',
               width=0.6,
               edgecolor='white')
# 添加数值标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2,
             height + 0.1,
             f'{height}',
             ha='center',
             va='bottom',
             fontsize=11)

# 设置标题和坐标轴标签
plt.title('各商区酒店的个数',fontsize=14,fontweight='bold')
plt.xlabel('商区', fontsize=12)
plt.ylabel('酒店数量', fontsize=12)

plt.grid(axis='y',
         alpha=0.3,
         linestyle='--')
plt.ylim(0, max(hotel_counts.values) * 1.15)

plt.tight_layout()
plt.show()
