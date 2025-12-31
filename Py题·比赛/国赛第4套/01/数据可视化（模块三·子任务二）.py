import pandas as pd

df = pd.read_csv(r'E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第04套\商城\清洗03.csv',
                 encoding="utf-8")
# 创建价格区间：每1500元一个区间
df['价格区间'] = (df['价格'] // 1500) * 1500

# 按价格区间分组，求每个区间的总销量
price_sales = df.groupby('价格区间')['销量'].sum().sort_index()

# 分成x轴和y轴数据
x_data = price_sales.index.tolist()  # 价格区间
y_data = price_sales.values.tolist()  # 总销量

print(x_data)
print(y_data)
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(13, 11))
width = 1000  # 根据你的数据范围调整这个值
plt.bar(x_data, y_data, width=width, align='center')
plt.show()
