# （1）删除shopping.csv中库存小于 10 或库存大于 10000 的数据，并存入shop1.csv；
# （2）将涉及“刷单”、“捡漏”等字段的数据删除，并存入shop2.csv；
# （3）将商品中涉及“女装”字段的数据删除，并存入shop3.csv；
# （4）将shopping.csv中手机价格为区间数据的，设置为价格区间的平均数，存入shop4.csv。

import pandas as pd

df = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第04套\商城\shopping.csv",
                 encoding="utf-8")

# (1) 删除库存小于10或大于10000的数据
df1 = df[(df['库存'] >= 10) & (df['库存'] <= 10000)].copy()
df1.to_csv(r'E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第04套\商城\筛选01.csv', index=False,
           encoding='utf-8')

# (2) 删除涉及"刷单"、"捡漏"等字段的数据
df1 = df1.reset_index(drop=True)
keywords_remove_1 = ['刷单', '捡漏']
pattern = '|'.join(keywords_remove_1)
mask = df1['名称'].str.contains(pattern, na=False)
df2 = df1[~mask].copy()
df2.to_csv(r'E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第04套\商城\清洗01.csv', index=False,
           encoding='utf-8-sig')

# (3)
df2 = df2.reset_index(drop=True)
keywords_remove_2 = ['女士', '女装', '裙', ]
pattern1 = '|'.join(keywords_remove_2)
mask1 = df2['名称'].str.contains(pattern1, na=False)
dress = df2[mask1].copy()
dress.to_csv(r'E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第04套\商城\女装数据.csv', index=False,
             encoding='utf-8-sig')
df3 = df2[~mask1].copy()
df3.to_csv(r'E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第04套\商城\清洗02.csv', index=False,
           encoding='utf-8-sig')

# (4)
df3 = df3.reset_index(drop=True)
for i in range(len(df3)):
    price = df3.loc[i, '价格']  # 直接拿到价格字符串
    # 判断：如果有"-"就是区间数
    if '-' in price:
        # 分割成两部分
        num1, num2 = price.split('-')
        num1 = float(num1)
        num2 = float(num2)
        # 去掉杂质，转成数字
        # num1 = float(start.replace('元', '').replace('¥', '').strip())
        # num2 = float(end.replace('元', '').replace('¥', '').strip())
        # 算平均数
        avg = (num1 + num2) // 2
        # 更新回去
        df3.loc[i, '价格'] = f"{avg}"
df3.to_csv(r'E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第04套\商城\清洗03.csv', index=False,
           encoding='utf-8-sig')
