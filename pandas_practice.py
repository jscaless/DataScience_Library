import numpy as np
import pandas as pd
from numpy.random import randn

# labels = ['a','b','c']
# my_list = [10,20,30]
# arr = np.array([10,20,30])
# d = {'a':10,'b':20,'c':30}

# print(pd.Series(data=my_list))
# print(pd.Series())

np.random.seed(101)
df = pd.DataFrame(randn(5, 4), index='A,B,C,D,E'.split(","), columns='W,X,Y,Z'.split(","))
print(df)
print('-' * 40)
print(df['W'])
print('-' * 40)
print(df['W'] > 0)
print('-' * 40)
print(df[df['W'] > 0])
print('-reset-' * 40)
print(df.reset_index())
print('-' * 40)
newindex = 'GA,AL,TN,FL,SC'.split(',')
df['States'] = newindex
print(df)
print('-' * 40)
df.set_index('States')
print(df)
print('-' * 40)
df.set_index('States', inplace=True)
print(df)
print('-' * 40)

# Index Levels
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)
print('-' * 40)
df = pd.DataFrame(np.random.randn(6, 2), index=hier_index, columns='A,B'.split(","))
print(df)
print('-' * 40)
print(df.loc['G1'])
print('-' * 40)
print(df.loc['G1'].loc[1])
print('-' * 40)
print(df.index.names)
print('-' * 40)
df.index.names = ['Group','Number']
print(df)
print(df.xs('G1'))
print(df.loc['G1'])
print('-' * 40)
print(df.xs(['G1', 1]))
print(df.loc['G1'].loc[1])
print(df.xs(1,level='Number'))