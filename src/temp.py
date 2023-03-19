# import pandas as pd

# data = {'letters': ['A', 'B', 'C'], 'numbers': [0, 1, 2]}
# df = pd.DataFrame(data)

# df['letters'] = df['letters'].str.casefold()
# print(df)

# alist = [1,2,3,4,4]
# print(alist.index(max(alist)))

x = [5]
print(id(x))
x[0] = 6
print(id(x))