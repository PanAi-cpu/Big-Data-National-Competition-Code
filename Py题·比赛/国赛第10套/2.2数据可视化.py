# 用折线图显示各星级酒店平均评分走势。
import pandas as pd

# 先是数据处理，处理出每一星级酒店的平均分
df = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第03套\hotel.csv"
                 , encoding='gbk')
df = df[df['星级'] != '无']
valid_stay = (df.dropna(subset='星级')
              .groupby('星级')['评分']
              .mean()
              .round(2))
# print(valid_stay)

# 可视化操作
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(10, 6))
plt.plot(valid_stay.index, valid_stay.values,
         marker='o',
         linewidth=2,
         markersize=8,
         color='skyblue')

plt.xlabel('星级', fontsize=12)
plt.ylabel('平均评分', fontsize=12)
plt.title('平均各星级酒店的评分', fontsize=14, fontweight='bold')

for i, v in enumerate(valid_stay.values):
    plt.text(i, v + 0.01, f'{v:.2f}',
             ha='center',
             va='bottom',
             fontsize=10)

plt.grid(True,alpha=0.3,linestyle='--')

plt.tight_layout()
plt.show()