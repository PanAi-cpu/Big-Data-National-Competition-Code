import pandas as pd

# 读取数据
df = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第05套\clean_month.csv",
                 encoding="gbk")

# 将month列转换为日期格式并提取月份
df['date'] = pd.to_datetime(df['month'], format='%b-%y')
df['month_num'] = df['date'].dt.month

# 按月份分组计算全国所有城市的平均值
national_monthly_avg = df.groupby('month_num').agg({
    'avg_high_tem': 'mean',
    'avg_low_tem': 'mean'
}).reset_index()

# 添加月份名称
month_names = {
    1: 'January', 2: 'February', 3: 'March', 4: 'April',
    5: 'May', 6: 'June', 7: 'July', 8: 'August',
    9: 'September', 10: 'October', 11: 'November', 12: 'December'
}
national_monthly_avg['month_name'] = national_monthly_avg['month_num'].map(month_names)

# 格式化输出，保留1位小数
national_monthly_avg['avg_high_tem'] = national_monthly_avg['avg_high_tem'].round(1)
national_monthly_avg['avg_low_tem'] = national_monthly_avg['avg_low_tem'].round(1)

# 重新排列列顺序
national_monthly_avg = national_monthly_avg[['month_num', 'month_name', 'avg_high_tem', 'avg_low_tem']]

print("=" * 60)
print(f"{'月份':<12} {'平均高温(℃)':<12} {'平均低温(℃)':<12} {'温差(℃)':<12}")
print("-" * 60)
for _, row in national_monthly_avg.iterrows():
    temp_diff = row['avg_high_tem'] - row['avg_low_tem']
    print(f"{row['month_name']:<12} {row['avg_high_tem']:<12} {row['avg_low_tem']:<12} {temp_diff:.1f}")

national_monthly_avg.to_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第05套\01.csv",
                            index=False, encoding='utf-8-sig')
