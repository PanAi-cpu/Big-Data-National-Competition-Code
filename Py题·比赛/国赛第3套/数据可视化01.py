# 子任务二
import pandas as pd

# 第一小题，用bar显示每个商区的酒店数量
df = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第03套\hotel.csv"
                 , encoding='gbk')
# 处理成可视化需要的数据，即只有商区和酒店的数量的二维表，即DataFrame

quantity_Data = (df.groupby('商圈')['住宿场所名称']
                 .count()
                 .rename('酒店数量')
                 .reset_index()
                 )
sort_Data = (quantity_Data.sort_values('酒店数量', ascending=False).head(20))
print(sort_Data)
# 可视化操作
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']


x = sort_Data['商圈']
height = sort_Data['酒店数量']

plt.figure(figsize=(12, 8))

plt.barh(x, height)  # barh()用于水平条形图

# 美化图表
plt.xlabel('酒店数量')
plt.ylabel('商圈')
plt.title('各商圈酒店数量统计')
plt.grid(axis='x', which='major', alpha=0.3)  # 水平网格线

# 在条形末端显示数值
for i, v in enumerate(height):
    plt.text(v + 0.1, i, str(v), va='center')

plt.tight_layout()
plt.show()