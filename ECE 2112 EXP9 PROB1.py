import pandas as pd

data1 = {'Student': ['Ice Bear','Panda','Grizzly'],
         'Math': [80,95,79]}
math = pd.DataFrame(data1, columns = ['Student','Math'])

data2 = {'Student': ['Ice Bear','Panda','Grizzly'],
         'Electronics': [85,81,83]}
elec = pd.DataFrame(data2, columns = ['Student','Electronics'])

data3 = {'Student': ['Ice Bear','Panda','Grizzly'],
         'GEAS': [90,79,93]}
geas = pd.DataFrame(data3, columns = ['Student','GEAS'])

data4 = {'Student': ['Ice Bear','Panda','Grizzly'],
         'ESAT': [93,89,88]}
esat = pd.DataFrame(data4, columns = ['Student','ESAT'])


m1 = pd.merge(math, elec, how='right', on='Student')
m2 = pd.merge(m1, geas, how='right', on='Student')
m3 = pd.merge(m2, esat, how='right', on='Student')


merge1 = pd.melt(m3, id_vars = 'Student', value_vars = ['Math', 'Electronics', 'GEAS', 'ESAT'])
merge2 = merge1.rename(columns = {'variable': 'Subjects', 'value': 'Grades'})
merge3 = merge2.sort_values('Student').reset_index().drop(columns = 'index')

print(m3,'\n')
print(merge3)