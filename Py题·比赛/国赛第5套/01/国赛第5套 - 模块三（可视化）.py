import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# (1) 设置主题、字体和字体大小
sns.set_theme(style="darkgrid")  # 设置深色网格主题
plt.rcParams['font.sans-serif'] = ['SimSun']  # 设置中文字体为宋体
plt.rcParams['font.size'] = plt.rcParams['font.size'] * 2  # 字体大小加倍
plt.rcParams['axes.unicode_minus'] = False  # 确保负数显示负号

# 读取数据
df1 = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第05套\Data_C\avg_temperature_tem.csv",
                  encoding="gbk")

# 准备数据
# 月份标签
x = ["01月", "02月", "03月", "04月", "05月", "06月", "07月", "08月", "09月", "10月", "11月", "12月"]
# 平均高温数据
y1 = df1["avg_high_tem"]
# 平均低温数据
y2 = df1["avg_low_tem"]

# 创建12x6英寸的画布
plt.figure(figsize=(12, 6))

# (2) 平均高温面积图
sns.lineplot(x=x, y=y1, color="#CC3300", linewidth=2, marker='o', label='平均最高温')
plt.fill_between(x, y1, alpha=0.4, color="#CC3300")
# lineplot: 创建红色折线，带圆点标记
# fill_between: 在折线下方填充半透明红色区域

# (3) 平均低温面积图
sns.lineplot(x=x, y=y2, color="#339999", linewidth=2, marker='o', label='平均最低温')
plt.fill_between(x, y2, alpha=0.7, color="#339999")
# 创建青绿色折线，带圆点标记
# 在折线下方填充半透明青绿色区域
# (6) 添加数据标签
for i, (month, temp_high, temp_low) in enumerate(zip(x, y1, y2)):
    # 平均高温数据标签
    plt.annotate(f'{temp_high:.2f}℃',
                 (i, temp_high),
                 textcoords="offset points",
                 xytext=(0, 10),
                 ha='center',
                 color='#996600',
                 fontsize=plt.rcParams['font.size'] * 0.6)

    # 平均低温数据标签
    plt.annotate(f'{temp_low:.2f}℃',
                 (i, temp_low),
                 textcoords="offset points",
                 xytext=(0, 10),
                 ha='center',
                 color='#996600',
                 fontsize=plt.rcParams['font.size'] * 0.6)

# (7) 设置标题
plt.title('2011-2021年月份气温均值')

# (8) 设置坐标轴标签
plt.xlabel('月份')
plt.ylabel('温度(℃)')

# (9) 设置横轴刻度标签
plt.xticks(range(len(x)), x)

# (10) 设置纵轴范围
plt.ylim(-5, 35)

# (11) 显示图例
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()
