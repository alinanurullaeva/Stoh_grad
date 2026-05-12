from cottage_data import get_data
from Regression import Regression

if_ln = False
cot_data = get_data(if_ln)
if if_ln:
    b = [5 for i in range(6)]
else:
    b = [12 for i in range(6)]

living_area_flag = True
total_area_flag = True
land_flag = True
dist_flag = True
lake_flag = True
c_flag = True
flag = [living_area_flag, total_area_flag, land_flag, dist_flag, lake_flag, c_flag]
b2 = []
cot_data2 = [cot_data[0]]
for i in range(len(flag)):
    if flag[i]:
        b2.append(b[i])
        cot_data2.append(cot_data[i + 1])
stoh_grad = Regression(cot_data2, b2)
result = stoh_grad.start_alg()
for el in result:
    print(','.join(str(el).split('.')))
'''for i in range(1, 101):
    res = 0
    for j in range(10):
        stoh_grad = Regression(cot_data2, b2)
        result = stoh_grad.start_alg()
        res += stoh_grad.sko()
    print(','.join(str(res / 10).split('.')))'''