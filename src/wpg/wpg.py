#%%
import pandas as pd
import requests
import seaborn as sns
import matplotlib.pyplot as plt

with open('temp.html', 'w', encoding='utf-8') as temp_file:
    response = requests.get('https://halloween.friko.net/slonce/Wroclaw')
    response.encoding = response.apparent_encoding
    temp_file.write(response.text)

def convert_time(s:str):
    num_s = ''.join(c for c in s if c.isdigit())
    if len(num_s) != 6:
         num_s = '000000'
    h,m,sec = int(num_s[:2]), int(num_s[2:4]), int(num_s[4:])
    num_s = sec+60*m+3600*h
    return num_s

table = pd.read_html('temp.html')[5]['Styczeń 2023']
day_length = table[['Dzień', 'Wschód-Zachód.2']]
day_length.columns = ['Dzień','Długość Dnia']
day_length = day_length.copy()
day_length['Długość Dnia'] = day_length['Długość Dnia'].apply(lambda s: convert_time(s))
day_length = day_length[day_length['Długość Dnia'] > 0]
plot = sns.relplot(data = day_length, x='Dzień', y='Długość Dnia')
plt.show()





# %%
