# 用折线图显示各星级酒店平均评分走势。
import pandas as pd


# 处理成可视化需要的数据，分组每一星级的平均评分
df = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第03套\hotel.csv"
                 , encoding='gbk')
cleanData = df[df['星级']!='无']
group_score = (cleanData.groupby('星级')['评分']
               .mean()
               .round(2)
               .rename('平均评分')
               )

# 实现折线图可视化
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(10, 6))
plt.plot(group_score.index, group_score.values,
         marker='o',
         linewidth=2,
         markersize=8,
         color='skyblue')

plt.xlabel('星级', fontsize=12)
plt.ylabel('平均评分', fontsize=12)
plt.title('平均各星级酒店的评分', fontsize=14, fontweight='bold')

for i, v in enumerate(group_score.values):
    plt.text(i, v + 0.01, f'{v:.2f}',
             ha='center', va='bottom',
             fontsize=10)

plt.grid(True, alpha=0.3, linestyle='--')

plt.tight_layout()
plt.show()