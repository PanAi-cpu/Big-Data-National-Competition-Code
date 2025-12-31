# 由于这种乐色题目的连题意都没有描述出来，我只好跟着小白做了
# 饼图显示不同手机品牌销售统计占比，虽然它是对销售的量进行统计的，但是我为了更加贴近一点原题意就将浏览量代替了
# 先分组吧，然后按照品牌对浏览量进行统计
import pandas as pd

df = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第04套\手机\model_comment.csv"
                 , encoding='gbk')

views_5 = (df.groupby('手机品牌')['浏览量']
           .sum()
           .sort_values(ascending=False)
           .head(5)
           )
print(views_5)

# 可视化步骤，（pie）
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']

plt.figure(figsize=(8,8))
plt.pie(views_5.values,
        labels=views_5.index,
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        explode=(0,0.1,0,0,0),
        shadow=True)
plt.title('不同手机的销售额',fontsize=16,fontweight='bold')
plt.axis('equal')
plt.tight_layout()
plt.show()