from cottage_data import get_data
from Stoh_grad_new import Stoh_grad2

if_ln = False
cot_data = get_data(if_ln)
if if_ln:
    # b = [3, 13, 4, -7, 30, -40]
    b = [20, 20, 20, 20, 20, 20]
else:
    # b = [0.075, 0.054, 0.175, -0.028, 28, 2]
    b = [1, 1, 1, 1, 1, 1]

'''stoh_grad = Stoh_grad2(cot_data, b)
result = stoh_grad.start()
print(stoh_grad.sko())'''
'''for el in result:
    print(','.join(str(el).split('.')))

2,387652016
13,68823326
3,135442348
-7,479697096
30,83355945
-40,08330946



# y =
living_area_flag = True

0,020649163
0,145789046
0,135893463
-0,136111907
31,06614269
1,446522141'''

living_area_flag = False
total_area_flag = True
land_flag = False
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
stoh_grad = Stoh_grad2(cot_data2, b2)
result = stoh_grad.start()
print(stoh_grad.sko())
print()
for el in result:
    print(','.join(str(el).split('.')))


'''stoh_grad = Stoh_grad2(cot_data2, b2)
result = stoh_grad.start()
sko = stoh_grad.sko()
for el in result:
    print(','.join(str(el).split('.')))
print(sko)
print(b2)

for i in range(10):
    s = []
    for j in range(1):
        stoh_grad = Stoh_grad2(cot_data2, b2)
        stoh_grad.start()
        s.append(stoh_grad.sko())
    print(sum(s) / len(s))'''