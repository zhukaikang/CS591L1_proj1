import pandas as pd
import os

input_true = """
print(df_lst)
import pandas as pd
lst = ['a', 'b', 'c', 'd']
tuple = ('a', 'b', 'c', 'd')
dict = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
concat1 = {'a': [1, 2, 3, 4],
           'b': [1, 2, 3, 4]}

concat1 = {'a': [5, 6, 7, 8],
           'b': [5, 6, 7, 8]}
           
readin = pd.read_csv("test.csv")
df_lst = pd.DataFrame(lst) 
df_tupe = pd.DataFrame(tuple)
df_dict = pd.DataFrame(dict)
df_readin = pd.DataFrame(readin)
print(df_readin)
df_dict = pd.DataFrame(dict)
df_concat = pd.concat([concat1, concat2])
#df_concat = pd.merge([concat1, concat2])
"""

input_wrong = """
print(df_lst)
import pandas as pd
lst = ['a', 'b', 'c', 'd']
tuple = ('a', 'b', 'c', 'd')
dict = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
concat1 = {'a': [1, 2, 3, 4],
           'b': [1, 2, 3, 4]}

concat1 = {'a': [5, 6, 7, 8],
           'b': [5, 6, 7, 8]}
           
readin = pd.read_csv("test.csv")
df_lst = pd.DataFrame(lst) 
df_tupe = pd.DataFrame(tuple)
df_dict = pd.DataFrame(dict)
df_readin = pd.DataFrame(readin)
print(df_readin)
df_dict = pd.DataFrame(dict)
df_concat = pd.concat([concat1, concat2])
df_concat = pd.merge([concat1, concat2])
"""