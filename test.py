from decimal import Decimal

import numpy as np
import pandas as pd


location = ((Decimal('116.411498'), Decimal('39.984871'), 33), (Decimal('116.411498'), Decimal('39.984871'), 34), (Decimal('116.411498'), Decimal('39.984871'), 33), (Decimal('116.411498'), Decimal('39.984871'), 33), (Decimal('116.411498'), Decimal('39.984871'), 34), (Decimal('116.411498'), Decimal('39.984871'), 33), (Decimal('116.559404'), Decimal('39.827266'), 33), (Decimal('116.559404'), Decimal('39.827266'), 34), (Decimal('116.559404'), Decimal('39.827266'), 33), (Decimal('116.559404'), Decimal('39.827266'), 33), (Decimal('116.559404'), Decimal('39.827266'), 34), (Decimal('116.559404'), Decimal('39.827266'), 33))
location1 = list([]) # 现在location是列表 需要把i i+1单独存成元组
location2 = list([])

list3 = list([])


for i in range(0, len(location)):
    location1.append(location[i][0])
    location2.append(location[i][1])
    #level.append(location[i][2])
for k in range(0, len(location1)):
    location1[k] = float(Decimal(location1[k]))
    location2[k] = float(Decimal(location2[k]))
local_real = [list(l) for l in zip(location2, location1)]

a = 0
list4 = np.array(list(set([tuple(t) for t in local_real]))).tolist()
level = [[] for x in range(len(list4))]
for k in range(0, len(list4)):
    if a == len(location):
        break
    for i in range(0, len(location)):
        if location2[i] == float(list4[k][0]):
            #list1.append(location[i][2])  # 要把风险等级存入二维列表
            level[k].append(location[i][2])
            a = a+1
        else:
            j = k+1
            level[j].append(location[i][2])
            a = a+1
x = len(local_real)
addr = local_real[len(local_real)-1]
print(x)
print(addr)
print(local_real)
