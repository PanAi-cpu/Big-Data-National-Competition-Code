# 用柱状图显示手机价格区间，既然没有明确说明价格之间的区间是多少，那就默认1000好了
import pandas as pd

df = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第04套\手机\model_comment.csv"
                 , encoding='gbk')
interval = (df['手机品牌'].value_counts())
print(interval)
price_bine = [1000, 2000, 3000, 4000, 5000, 7000, 10000]
price_labels = ['1001-2000元', '2001-3000元', '3001-4000元', '4001-5000元', '5001-7000元', '7001-10000元']
# 先是创建一个价格区间，然后在把它一一对应的数据填入对应的区间中，最后进行统计
df['价格区间'] = pd.cut(df['价格'],
                        bins=price_bine,
                        labels=price_labels,
                        include_lowest=False)
price_count = df['价格区间'].value_counts()

print(price_count)

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
ax = price_count.plot(kind='bar',
                      figsize=(10, 6),
                      color='skyblue',
                      width=0.7,
                      edgecolor='black')

plt.title('各价格区间商品的情况', fontsize=14, fontweight='bold')
plt.xlabel('价格区间', fontsize=12)
plt.ylabel('数量（部）', fontsize=12)

for i, v in enumerate(price_count.values):
    plt.text(i, v + 0.3, str(v),
             ha='center', va='bottom',
             fontsize=10)

plt.grid(axis='y',alpha=0.3,linestyle='--')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()