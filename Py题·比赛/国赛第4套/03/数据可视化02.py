# 没有不同地区啊?这种误人子弟的试卷,我做一次气死一次.
import pandas as pd

# 用饼图显示不同手机品牌浏览统计占比。
df = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第04套\手机\model_comment.csv"
                 , encoding='gbk')

# 先是数据处理,分组出不同手机品牌的浏览情况
group_score = (df.groupby('手机品牌')['浏览量']
               .sum()
               .sort_values(ascending=False)
               )
print(group_score)

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(8, 8))  # 饼图讲究的是刚刚好,就像是中心轴对称差不多,所以用到的一般就是上下左右差不多的
plt.pie(group_score.values,
        labels=group_score.index,
        autopct='%1.1f%%',
        startangle=90,
        )
plt.title('不同手机的浏览量')
plt.axis('equal')
plt.tight_layout()
plt.show()