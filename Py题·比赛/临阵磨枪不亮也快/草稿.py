import pandas as pd
df = pd.read_csv(r"E:\桌面\hotel.csv", encoding='gbk')
# 1. 条件计数
print(f"北京的人数: {(df['城市'] == '北京').sum()}")
print(f"工资>10000的人数: {(df['工资'] > 10000).sum()}")

# 2. 多条件统计
condition = (df['城市'] == '北京') & (df['工资'] > 7000)
print(f"北京且工资>7000的人数: {condition.sum()}")

# 3. 使用query
print("\n北京的员工:")
beijing_employees = df.query("城市 == '北京'")
print(beijing_employees)

# 4. 分组条件统计
print("\n各部门高工资人数（>8000）:")
high_salary_count = df[df['工资'] > 8000].groupby('部门').size()
print(high_salary_count)


print("=== 方法一：value_counts() ===")
# 统计每个商圈的酒店数量
hotel_counts = df['商圈'].value_counts()
print("各个商圈酒店数量:")
print(hotel_counts)
print(f"\n数据类型: {type(hotel_counts)}")

# 转换为DataFrame
hotel_counts_df = hotel_counts.reset_index()
hotel_counts_df.columns = ['商圈', '酒店数量']
print("\n转换为DataFrame:")
print(hotel_counts_df)

# 按酒店数量排序
print("\n按酒店数量降序排列:")
print(hotel_counts.sort_values(ascending=False))