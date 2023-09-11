import pandas as pd
import random
from pyecharts.charts import Pie
from pyecharts import options as opts

# 准备数据 省份和省份未新增新冠病毒的天数
provinces = ['北京', '上海', '黑龙江', '吉林', '辽宁', '内蒙古', '新疆', '西藏', '青海', '四川', '云南', '陕西', '重庆',
             '贵州', '广西', '海南', '澳门', '湖南', '江西', '福建', '安徽', '浙江', '江苏', '宁夏', '山西', '河北',
             '天津']
num = [1, 1, 1, 17, 9, 22, 23, 42, 35, 7, 20, 21, 16, 24, 16, 21, 37, 12, 13, 14, 13, 7, 22, 8, 16, 13, 13]

# 用随机方法定义颜色序列的
def random_color():
    # 返回一个随机的RGB颜色码
    # "{:02x}{:02x}{:02x}" 是一个字符串格式化模板，它将3个整数值转化为2位的16进制表示。
    # random.randint(0, 255) 随机生成一个在[0, 255]之间的整数，代表RGB颜色中的一个通道值。
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255),
                                        random.randint(0, 255),
                                        random.randint(0, 255))
# 使用列表推导式为每一个省份生成一个随机颜色，结果保存在color_series列表中
color_series = [random_color() for _ in range(len(provinces))]

# 使用数据创建一个DataFrame
df = pd.DataFrame({'provinces': provinces, 'num': num})

# 根据'num'列的值进行降序排序
df.sort_values(by='num', ascending=False, inplace=True)

# 提取数据列表
v = df['provinces'].values.tolist()
d = df['num'].values.tolist()

# 创建Pie图表实例
pie1 = Pie(init_opts=opts.InitOpts(width='1350px', height='750px'))

# 设置颜色序列
pie1.set_colors(color_series)

# 向饼图中添加数据，并设置相关参数如半径、中心、南丁格尔图类型等
pie1.add("", [list(z) for z in zip(v, d)],
         radius=["30%", "135%"],
         center=["50%", "65%"],
         rosetype="area"
         )

# 设置全局配置，如标题、图例和工具箱
pie1.set_global_opts(title_opts=opts.TitleOpts(title='玫瑰图示例'),
                     legend_opts=opts.LegendOpts(is_show=False),
                     toolbox_opts=opts.ToolboxOpts())

# 设置系列配置，如标签显示方式等
pie1.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position="inside", font_size=12,
                                               formatter="{b}:{c}天", font_style="italic",
                                               font_weight="bold", font_family="Microsoft YaHei"
                                               ),
                     )

# 渲染生成html文档
pie1.render('南丁格尔玫瑰图1.html')
