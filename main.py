import io
import sys

import folium
from PyQt5 import QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import Qt
from MapDisplay import MapDisplay


def visual_all(x, y, *level):
    #app = QtWidgets.QApplication(sys.argv)
    whm = folium.Map(
        location=[39.873079, 116.481913],
        tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}',  # bug
        # 高德地图，暂不支持百度地图的底图
        zoom_start=20,  # 默认放大倍数
        attr='default'
    )

    '''
    表示我用的是高德地图作为底图。为啥要改呢，因为每个不同的地图公司，用的坐标系不一样，高德地图和google地图、soso地图、aliyun地图、mapabc地图所用坐标相同，
    都是国测局（GCJ02）坐标，和百度地图用的坐标系不一样，如果直接拿百度坐标系下的经纬度画在高德地图上，那就会整体偏移，使用之前必须进行坐标转换
    原文链接：https://blog.csdn.net/u012848304/article/details/108073187(该链接就有百度坐标系下的坐标点转换成高德坐标的方法)
    '''

    color = [0 for index in range(len(level[0]))]
    html1 = """"""

    for i in range(0, len(level[0])):
        level_num = int(level[0][i])
        if level_num <= 20:
            color[i] = 'btn btn-danger'
        if 20 < level_num <= 40:
            # color[1] = 'btn btn-warning'
            color[i] = 'btn btn-warning'
        if 40 < level_num <= 60:
            # color[2] = 'btn btn-info'
            color[i] = 'btn btn-info'
        if 60 < level_num <= 80:
            # color[3] = 'btn btn-secondary'
            color[i] = 'btn btn-secondary'
        if 80 < level_num <= 100:
            # color[4] = 'btn btn-success'
            color[i] = 'btn btn-success'

    for i in range(0, len(level[0])):
        html1 = """<tr><td><button class='""" + color[i] + """'>充电桩 '""" + str(i) + """' </button></td></tr>""" + html1
    html_1 = """<table border="0">""" + html1 + """</table>"""

    pop = folium.Popup(html=folium.Html("""
                    <div>{}</div>""".format(html_1),
                                        script=True,
                                        width=100),
                       parse_html=True,
                       max_width=3000,
                       )

    folium.Marker(  # 添加位置标示
        location=[39.873079, 116.481913],
        popup=pop,  # 这个位置 作为与html页面交互，现在的问题就是怎么把后端的数据交互进去，并且前端页面怎么做颜色区分
        icon=folium.Icon(color="lightblue", icon="info-sign"),
    ).add_to(whm)

    folium.CircleMarker(  # 圈地
        location=[39.873079, 116.481913],
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
    risk_level = [10, 30, 50, 70, 90]
    data = visual_all(1141.111111, 1221.222222, risk_level)
    w = QtWebEngineWidgets.QWebEngineView()
    w.setHtml(data.getvalue().decode())
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())