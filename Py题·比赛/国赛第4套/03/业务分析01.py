import pandas as pd
from matplotlib.lines import lineStyles

# 统计OPPO Reno品牌手机的正向、中性、负向评价数量
df = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第04套\手机\model_comment.csv"
                 , encoding='gbk')
oppoData = df[df['手机品牌'].str.contains('OPPO Reno', case=False, na=False)]['情感倾向'].value_counts()
print(oppoData)

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(12, 8))
plt.plot(oppoData,
         marker='o',
         markersize=8,
         linewidth=2.5,
         linestyle='-',
         label='情感倾向'
         )
plt.title('OPPo Reno 的情感倾向 折线图', fontsize=16, fontweight='bold')
plt.xlabel('情绪倾向', fontsize=12)
plt.ylabel('条数', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=10)
for i, v in enumerate(oppoData):
    plt.text(i, v + 0.3, str(v), ha='center', va='bottom')

plt.tight_layout()
plt.show()
