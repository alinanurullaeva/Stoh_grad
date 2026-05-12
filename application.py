from application_data import application_data
from Classification2 import Classification


b = [-0.0001 for i in range(11)]
data = application_data()
stoh_grad = Classification(data, b)
result = stoh_grad.start_alg()
for el in result:
    print(','.join(str(el).split('.')))
print(stoh_grad.tr())