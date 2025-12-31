import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map

df = pd.read_excel(
    r"E:\桌面\pandas&Matplotlib练习\ZZ052-大数据应用与服务赛项 数据源第01套\03_中国地区数据\dim_area.xlsx", header=None)

province_Data = df[1].value_counts().to_dict()
# 这里的 .values_counts() 和 .to_dict()  的意思分别是统计其中value各出现的个数，和将列表转换成字典

# print(province_Data)

# 输出验证；具体如下：'广东：74个'
# for province_Verification, count in province.items():
#     print(f'{province_Verification}:{count}个')

# 标准化省份名称
province_mapping = {
    '北京': '北京市', '天津': '天津市', '上海': '上海市', '重庆': '重庆市',
    '河北': '河北省', '山西': '山西省', '辽宁': '辽宁省', '吉林': '吉林省',
    '黑龙江': '黑龙江省', '江苏': '江苏省', '浙江': '浙江省', '安徽': '安徽省',
    '福建': '福建省', '江西': '江西省', '山东': '山东省', '河南': '河南省',
    '湖北': '湖北省', '湖南': '湖南省', '广东': '广东省', '海南': '海南省',
    '四川': '四川省', '贵州': '贵州省', '云南': '云南省', '陕西': '陕西省',
    '甘肃': '甘肃省', '青海': '青海省', '台湾': '台湾省',
    '内蒙古': '内蒙古自治区', '广西': '广西壮族自治区', '西藏': '西藏自治区',
    '宁夏': '宁夏回族自治区', '新疆': '新疆维吾尔自治区'
}

provinces = list(province_Data.keys())
values = list(province_Data.values())

# 验证
print("省份列表:", provinces[:5])  # 查看前5个省份
print("数值列表:", values[:5])     # 查看前5个数值

# 初始化地图数据（zip组合）
map_Data = []
for province, value in zip(provinces, values):
    standard_name = province_mapping.get(province, province)
    map_Data.append([standard_name, value])

# 创建地图对象
china_map = (
    Map()
    # 2. 添加数据到地图；分别是图例、数据（格式是[['省份','数值',……]]）、地图类型（‘china’，中国地图）
    .add('地区数量', map_Data, 'china')
    # 全局配置
    .set_global_opts(
        # 标题配置
        title_opts=opts.TitleOpts(title='不同省份用户访问量分布'),
        # 视觉映射配置（颜色条）
        visualmap_opts=opts.VisualMapOpts(
            max_=max(values),       # 颜色条最大值
            min_=min(values)        # 颜色条最大值
        ),
    )
)

china_map.render('不同省份用户访问量分布图.html')
