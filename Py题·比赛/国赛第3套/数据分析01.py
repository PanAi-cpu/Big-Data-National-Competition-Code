# 以月度为单位统计每月该酒店的正向、中性、负向评价数量
import pandas as pd
from IPython.core.pylabtools import figsize


# 按月进行分组，然后统计正向、中性、负向评价的数量
df = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第03套\standard.csv"
                 , encoding='utf')
# 转换格式成时间格式
df['评论日期'] = pd.to_datetime(df['评论日期'])
df['年月'] = df['评论日期'].dt.to_period('M')

group_monthData = (df.groupby(['年月', '情感倾向'])['编号']
                   .count()
                   .unstack(fill_value=0))
print(group_monthData)

# 图表的绘制
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize(13, 6))
group_monthData.plot(kind='line',
                     marker='o',
                     linewidth=2,
                     markersize=6,)

plt.title('情感倾向月的变化趋势',
          fontsize=14,
          fontweight='bold')
plt.xlabel('年月', fontsize=12)
plt.ylabel('评论数量', fontsize=12)

plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(title='情感倾向', fontsize=10)
plt.xticks(rotation=45)
result = []
for i in range(0, 100, 5):  # range支持步长参数
    result.append(i)
plt.yticks(result)
plt.tight_layout()
plt.show()
