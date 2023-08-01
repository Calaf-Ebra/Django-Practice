import pandas as pd
x=[1,2,3,4,6,7,8,9,11,2,2,333,555,666,777]
raw = {'data':x}
y= []

data = pd.DataFrame(raw)
print(data.head())

data['data'] = data['data'].astype('int')


for i in range (data['data']):

    if i[0] <10:
        i += 1
        y.append(i)
    else: 
        pass

print(y)