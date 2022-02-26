if __name__== '__main__':
    data = (('d', 3), ('b', 3), ('c', 3))
    values = list([])
    x = list([])
    for i in range(0, len(data)):
        x.append(data[i][0])
        # x.append(str(data[i][1]) + "-" + str(data[i][2])) #这样写法 横坐标填满了，不好看
        values.append(data[i][1])  # 需要把x变成充电区域名称
    print(x, values)