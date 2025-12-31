import pandas as pd

df = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第04套\商城\清洗03.csv"
                 , encoding='utf')

df['品牌'] = '其它'
df.loc[df['名称'].str.contains('小米'), '品牌'] = '小米'
df.loc[df['名称'].str.contains('Redmi'), '品牌'] = '小米'
df.loc[df['名称'].str.contains('苹果'), '品牌'] = '苹果'
df.loc[df['名称'].str.contains('Apple'), '品牌'] = '苹果'
df.loc[df['名称'].str.contains('三星'), '品牌'] = '三星'
df.loc[df['名称'].str.contains('华为'), '品牌'] = '华为'
df.loc[df['名称'].str.contains('宏碁'), '品牌'] = '宏碁'
df.loc[df['名称'].str.contains('戴尔'), '品牌'] = '戴尔'
df.loc[df['名称'].str.contains('惠普'), '品牌'] = '惠普'
df.loc[df['名称'].str.contains('联想'), '品牌'] = '联想'
df.loc[df['名称'].str.contains('荣耀'), '品牌'] = '荣耀'
df.loc[df['名称'].str.contains('华硕'), '品牌'] = '华硕'
df.loc[df['名称'].str.contains('Meizu'), '品牌'] = 'Meizu'
df.loc[df['名称'].str.contains('vivo'), '品牌'] = 'vivo'

brand_counts = (df['品牌'].value_counts().sort_values())
print(brand_counts.head(10))

# 浏览量

views = df.sort_values('浏览量', ascending=True)
print(views.head(6))

sales = (df.groupby('品牌')['销量']
         .sum()
         .sort_values()
         .head(5))
print(sales)
