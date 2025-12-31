from pyecharts import options as opts
from pyecharts.charts import Map

province_dis = {'宁夏回族自治区': 55, '河南省': 145, '北京市': 137, '河北省': 121, '辽宁省': 112,
                '江西省': 16, '上海市': 120, '安徽省': 110, '江苏省': 116, '湖南省': 119,
                '浙江省': 113, '海南省': 12, '广东省': 212, '湖北省': 18, '黑龙江省': 111,
                '澳门特别行政区': 11, '陕西省': 111, '四川省': 17, '内蒙古自治区': 13, '重庆市': 13,
                '广西壮族自治区': 81, '云南省': 16, '贵州省': 21, '吉林省': 31, '山西省': 11,
                '山东省': 111, '福建省': 41, '青海省': 51, '天津市': 11, '新疆维吾尔自治区': 150,
                '西藏自治区': 170, '甘肃省': 120, '台湾省': 31}

province = list(province_dis.keys())
values = list(province_dis.values())

china = (
    Map()
    .add("", [list(z) for z in zip(province, values)], "china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国地图"),
        visualmap_opts=opts.VisualMapOpts(
            max_=220,  # 最大值设为220
            min_=0,  # 最小值设为0
        )
    )
)

# 打开html
china.render("初体验地图.html")
