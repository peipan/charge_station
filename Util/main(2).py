import io
import sys

import folium
from PyQt5 import QtWidgets, QtWebEngineWidgets

def visual_all(x, y, **level):

    while True:
        add_g = 'http://webst02.is.autonavi.com/appmaptile?style=6&x={x}&y={y}&z={z}'  # 街道图
        if type(add_g):
            add_g = 'http://webst02.is.autonavi.com/appmaptile?style=6&x={x}&y={y}&z={z}'  # 卫星图
            break

    whm = folium.Map(
         location=[x, y],
         tiles=add_g,
         # 高德地图，暂不支持百度地图的底图
         zoom_start=20,  # 默认放大倍数
         attr='default'
    )

    '''
    表示我用的是高德地图作为底图。为啥要改呢，因为每个不同的地图公司，用的坐标系不一样，高德地图和google地图、soso地图、aliyun地图、mapabc地图所用坐标相同，
    都是国测局（GCJ02）坐标，和百度地图用的坐标系不一样，如果直接拿百度坐标系下的经纬度画在高德地图上，那就会整体偏移，使用之前必须进行坐标转换
    原文链接：https://blog.csdn.net/u012848304/article/details/108073187(该链接就有百度坐标系下的坐标点转换成高德坐标的方法)
    '''
    color = [0 for index in range(len(level))]  # 设置颜色列表 根据输入充电桩个数来设置大小
    html1 = """"""
    html_2 = """"""
    levels = list(level.values())

    for i in range(0, len(level)):  # 判断风险等级
        if levels[i] <= 20:
            color[i] = 'btn btn-danger'  # 代表不合格 用红色表示
        if 20 < levels[i] <= 40:
            color[i] = 'btn btn-warning'  # 代表高风险 用黄色表示
        if 40 < levels[i] <= 60:
            color[i] = 'btn btn-info'  # 代表较高风险 用浅蓝色表示
        if 60 < levels[i] <= 80:
            color[i] = 'btn btn-secondary'  # 代表较低风险 用深蓝色表示
        if 80 < levels[i] <= 100:
            color[i] = 'btn btn-success'  # 代表低风险 用绿色表示

    for i in range(0, len(level)):
        html1 = """<tr><td><button class='""" + color[i] + """'>充电桩 '""" + str(i) + """' </button></td></tr>""" + html1
    html_1 = """<table border="0">""" + html1 + """</table>"""

    pop = folium.Popup(html=folium.Html("""
                    <div>{}</div>""".format(html_1),
                                        script=True,
                                        height=150,
                                        width=100),
                       parse_html=True,
                       max_width=3000,
                       )

    folium.Marker(  # 添加位置标示
        location=[x, y],
        popup=pop,  # 这个位置 作为与html页面交互，现在的问题就是怎么把后端的数据交互进去，并且前端页面怎么做颜色区分
        icon=folium.Icon(color="lightblue", icon="info-sign"),
    ).add_to(whm)

    folium.CircleMarker(  # 圈地
        location=[x, y],
        radius=100,  # 圈半径
        color="#c72e29",
        fill=True,
        fill_color="#c72e29",
    ).add_to(whm)

    folium.LayerControl().add_to(whm)
    data = io.BytesIO()
    whm.save(data, close_file=False)
    return data


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    x = 39.873079
    y = 116.481913
    level = {'1': 2, '2': 30, '3': 90, '4': 65}
    # level = input()
    # level = level.split(",")  # 输入时利用，分隔 并且转换为int型
    # level = [int(level[i]) for i in range(len(level))]

    data = visual_all(x, y, **level)  # 输入x y坐标 和多个充电桩电量 的数据
    w = QtWebEngineWidgets.QWebEngineView()
    w.setHtml(data.getvalue().decode())
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())