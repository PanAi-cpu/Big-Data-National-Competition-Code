import pandas as pd

# 对各品牌进行统计，进行正序排序展示前十名；

df = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第04套\商城\清洗03.csv"
                 , encoding='utf')
# 创建一个新列，把每一行的品牌总结放进去
df['品牌'] = '其它'
df.loc[df['名称'].str.contains('Radmi'), '品牌'] = '小米'
df.loc[df['名称'].str.contains('小米'), '品牌'] = '小米'
df.loc[df['名称'].str.contains('苹果'), '品牌'] = '苹果'
df.loc[df['名称'].str.contains('Apple'), '品牌'] = '苹果'
df.loc[df['名称'].str.contains('三星'), '品牌'] = '三星'
df.loc[df['名称'].str.contains('华为'), '品牌'] = '华为'
df.loc[df['名称'].str.contains('Meizu'), '品牌'] = 'Meizu'
df.loc[df['名称'].str.contains('vivo'), '品牌'] = 'vivo'
df.loc[df['名称'].str.contains('惠普'), '品牌'] = '惠普'
df.loc[df['名称'].str.contains('宏碁'), '品牌'] = '宏碁'
df.loc[df['名称'].str.contains('联想'), '品牌'] = '联想'
df.loc[df['名称'].str.contains('华硕'), '品牌'] = '华硕'
df.loc[df['名称'].str.contains('戴尔'), '品牌'] = '戴尔'
df.loc[df['名称'].str.contains('荣耀'), '品牌'] = '荣耀'

brand_counts = (df['品牌'].value_counts().sort_values())
print(brand_counts)

# 对各品牌的销量进行统计
sales = (df.groupby('品牌')['销量']
          .mean()
          .sort_values()
         .round(2)
          )
print(sales)
