# 清洗、筛选数据
import pandas as pd

# 读取数据
df = pd.read_csv(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第05套\clean_month.csv",
                 encoding="gbk")

# 日期处理并分组计算
df['month_num'] = pd.to_datetime(df['month'], format='%b-%y').dt.month
# 将month列（格式如"Jan-21"）转换为日期格式
# 提取月份数字（1-12）存储到新列month_num
national_monthly_avg = (df.groupby('month_num')[['avg_high_tem', 'avg_low_tem']]
                        .mean()
                        .round(1)
                        .reset_index())
print(national_monthly_avg)
# 按月份分组，计算每个月的平均高温和平均低温
# .reset_index()：将分组键恢复为列直接输出结果

# 直接基于已有结果处理
# national_monthly_avg['month_name'] = national_monthly_avg['month_num'].apply(
#     lambda x: pd.to_datetime(f"{x}/1/2020", format='%m/%d/%Y').strftime('%B')
# )

# 直接输出

# national_monthly_avg.to_csv(
#     r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第05套\avg_temperature_tem.csv", index=False,
#     encoding='utf-8-sig')
