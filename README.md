# Python-NanDingGeEr
用Python画可视的个省份新冠疫情人数未新增的天数的南丁格尔图，数据可视化，数据分析

### 导入相应的库
```
import pandas as pd  
import random  
from pyecharts.charts import Pie  
from pyecharts import options as opts
```

### 准备相关的数据  
```
# 省份
provinces = ['北京', '上海', '黑龙江', '吉林', '辽宁', '内蒙古', '新疆', '西藏', '青海', '四川', '云南', '陕西', '重庆',
             '贵州', '广西', '海南', '澳门', '湖南', '江西', '福建', '安徽', '浙江', '江苏', '宁夏', '山西', '河北',
             '天津']
# 相对应的省份未新增的天数
num = [1, 1, 1, 17, 9, 22, 23, 42, 35, 7, 20, 21, 16, 24, 16, 21, 37, 12, 13, 14, 13, 7, 22, 8, 16, 13, 13]
```

### 用随机方法定义颜色序列的
```
def random_color():
    # 返回一个随机的RGB颜色码
    # "{:02x}{:02x}{:02x}" 是一个字符串格式化模板，它将3个整数值转化为2位的16进制表示。
    # random.randint(0, 255) 随机生成一个在[0, 255]之间的整数，代表RGB颜色中的一个通道值。
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255),
                                        random.randint(0, 255),
                                        random.randint(0, 255))
# 使用列表推导式为每一个省份生成一个随机颜色，结果保存在color_series列表中
color_series = [random_color() for _ in range(len(provinces))]
```
