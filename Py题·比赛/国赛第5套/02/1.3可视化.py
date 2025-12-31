# 它的意思是说什么，我算是看明白了，还得是自己先处理数据
# 看题目因该是求出2011年~2021年，平均每月的气温平均值
# 然后才是进行可视化处理
# 数据处理这一块
# 这他妈是不同地区的一年平均气温吧，这题目出的个啥？他妈2011年到2021年的平均每月气温都来了。我现在严重怀疑出题人前一天晚上拿脑子往马桶里塞，脑子里进屎了他妈能想出这种题目的。前言不搭后语，拉屎不脱裤子，吃饭不用筷子
# 气发完了可以继续做了，既然数据是每个地区的话，那就计算每个地区


import pandas as pd

df = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第05套\clean_month.csv",
                 encoding='gbk')
# 看了一下csv图表，第一步因该是将Jay-25 这样的月份数据转换成 2025-01-01
df['month_num'] = pd.to_datetime(df['month'], format='%b-%y').dt.month
# 时间部分处理完了就可以开始进行统计就算了
avg_weatherData = (df.groupby('month_num')[['avg_high_tem', 'avg_low_tem']]
                   .mean()
                   .round(1)
                   .reset_index())
print(type(avg_weatherData))
# 数据处理成DataFrame了，就差月份了，如果需要可以创建一个英文月份的x表格
# 可视化部分，处理成面积图,就是加上渐变色的折线图嘛,Come on Come on
import matplotlib.pyplot as plt
import seaborn as sns

# 2011-2021年月份气温均值
# 基础配置
sns.set_style('darkgrid')  # 主题设置
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据导入
x = ["01月", "02月", "03月", "04月", "05月", "06月", "07月", "08月", "09月", "10月", "11月", "12月"]
y1 = avg_weatherData['avg_high_tem']
y2 = avg_weatherData['avg_low_tem']

# 画布创建
# 妈的这吊题目说的云里雾里的,我真操了.他妈的你得先做一张折线图然后再按照题目上面进行更改美化.什么毛病!
plt.figure(figsize=(12, 6))

# 最高温面积图创建
sns.lineplot(x=x, y=y1, color='#CC3300', linewidth=2, marker='o', label='平均最高温')
plt.fill_between(x, y1, alpha=0.4, color='#CC3300')
# 最低气温面积图创建
sns.lineplot(x=x, y=y2, color='#339999', linewidth=2, marker='o', label='平均最低温')
plt.fill_between(x, y2, alpha=0.7, color='#339999')

# 添加标签
for i, (month, high, low) in enumerate(zip(x, y1, y2)):
    plt.annotate(f'{high:.2f}℃',
                 (i, high),
                 textcoords='offset points',
                 xytext=(0, 10),
                 ha='center',
                 va='bottom',
                 color='#996600')
    plt.annotate(f'{low:.2f}℃',
                 (i,low),
                 textcoords='offset points',
                 xytext=(0,-10),
                 ha='center',
                 color='#996600')


plt.title('2011~2021年月份气温平均值')

plt.xlabel('月份')
plt.ylabel('温度(℃)')

plt.ylim(-5,35)
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()