import pandas as pd
import json

data = []

with open(r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第06套\ECharts\chengdu.js", 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip():  # 跳过空行
            data.append(json.loads(line.strip()))


df = pd.DataFrame(data)