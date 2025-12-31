import pandas as pd
from setuptools.command.rotate import rotate

# 用柱状图显示不同价格区间手机销售情况，了解大众消费情况；
# 先是数据处理,统计出每个区间的手机价格区间,销售情况
df = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第04套\手机\model_comment.csv"
                 , encoding='gbk')
interval = (df['手机品牌'].value_counts())
# print(interval)

price_bine = [0, 2000, 3000, 4000, 5000, 7000, 10000]
price_labels = ['0~2000', '2001~3000', '3001~4000', '4001~5000', '5001~7000', '7001~10000']

df['价格区间'] = pd.cut(df['价格'],
                        bins=price_bine,
                        labels=price_labels,
                        include_lowest=False)
price_count = df['价格区间'].value_counts()
print(price_count)

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
ax = price_count.plot(kind='bar',
                      figsize=(10,6),
                      color='skyblue',
                      width=0.7,
                      edgecolor='black')

plt.title('各价格区间商品的情况',fontsize=14,fontweight='bold')
plt.xlabel('价格区间',fontsize=12)
plt.ylabel('数量(部)',fontsize=12)

for i,v in enumerate(price_count.values):
    plt.text(i,v +0.3,str(v),
             ha='center',va='bottom',
             fontsize=10)

plt.grid(axis='y',alpha=0.3,linestyle='--')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()