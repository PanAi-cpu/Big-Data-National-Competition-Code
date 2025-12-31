from operator import index

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")  # 设置深色网格主题
plt.rcParams['font.sans-serif'] = ['SimSun']  # 设置中文字体为宋体
plt.rcParams['font.size'] = plt.rcParams['font.size'] * 3
plt.figure(figsize=(12, 7))

df = pd.read_csv(
    r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第06套\模块三处理后的数据\最高气温前10的城市.csv",
    encoding='utf-8')

x = df['city']
y = df['hightest_tem']

ax = sns.barplot(x=x, y=y, hue=x, palette="hls", legend=False)

for i, (city, tem) in enumerate(zip(x, y)):
    ax.annotate(f'{tem:.2f}℃',
                (i, tem),
                textcoords="offset points",  # 指定偏移坐标系
                xytext=(0, 5),
                ha='center',
                va='bottom',
                color='black',
                fontsize=10
                )

plt.title('2011-2021中高温城市排名')

plt.xlabel('城市')
plt.ylabel('最高温(℃)')
plt.ylim(0, 55)
plt.yticks(range(0, 56, 5))  # 显示0,5,10,...,55的刻度
plt.show()
