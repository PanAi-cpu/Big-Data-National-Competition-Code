import pandas as pd

# 统计OPPO Reno品牌手机的正向、中性、负向评价数量
df = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第04套\手机\model_comment.csv"
                 , encoding='gbk')
# 依旧经典筛选，等一下给我背熟，还要你写在笔记上
oppoData = df[df['手机品牌'].str.contains('OPPO Reno', case=False, na=False)]['情感倾向'].value_counts()
print(oppoData)

# 可视化操作,绘制折线图
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(12, 7))

plt.plot(oppoData,
         marker='o',
         markersize=8,
         linewidth=2.5,
         color='#2E86AB',
         linestyle='-',
         label='情绪倾向')

plt.title('OPPO Reno 的情绪倾向 折线图', fontsize=16, fontweight='bold')
plt.xlabel('情绪倾向', fontsize=12)
plt.ylabel('条数', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=10)
for i, v in enumerate(oppoData):
    plt.text(i, v + 0.3, str(v), ha='center', va='bottom')

plt.tight_layout()
plt.show()




# 简要分析（由于未创建docx文件所以就再下面标注一下业务分析的内容了）

# 由于，这个数据的限制，导致图像中没有时间显示，这也导致这种数据分析是一种非常不健康的
# 图像显示正向的评价是中性和负向的两倍，这个牌子的手机大体观感是不错的，有一些小瑕疵，但是不影响对它的使用