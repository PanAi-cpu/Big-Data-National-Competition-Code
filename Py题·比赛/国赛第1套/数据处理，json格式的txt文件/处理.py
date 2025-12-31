import pandas as pd
import json

data = []
with open(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第01套\01_app_log\文本文档格式\behavior2023-01-01.log",'r',encoding='utf-8') as f:
    for line in f:
        if line.strip():  # 跳过空行
            data.append(json.loads(line.strip()))

# 创建DataFrame
df = pd.DataFrame(data)

# 导出为CSV文件
df.to_csv(r'E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第01套\01_app_log\整理后的文件\behavior2023-01-01.csv', index=False, encoding='utf-8-sig')