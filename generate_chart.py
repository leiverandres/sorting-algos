import json
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sorting_times = json.load(open('sorting_times.json'))

df_data = {
    'Data_quantity':
    list(map(lambda x: int(x), sorting_times['cocktail'].keys())),
    'Quick':
    list(float(x) for x in sorting_times['quick'].values()),
    'Heap':
    list(float(x) for x in sorting_times['heap'].values()),
    'Cocktail':
    list(float(x) for x in sorting_times['cocktail'].values())
}
# df = pd.DataFrame(
#     data=df_data,
# index=list(sorting_times['cocktail'].keys()),
# )
# print(df)
# df = df.cumsum()
# plt.tick_params(labelsize='xx-large')
# plt.ylabel('Tiempo (seg)')
# plt.xlabel('Cantidad')
# pt = df.plot(
#     x='Data_quantity',
#     y='Cocktail',
#     fontsize='xx-large',
#     legend=True,
#     title='Tamaño del array vs tiempo de ordenamiento')
# # plt.show()

# plt.waitforbuttonpress()
print(df_data['Data_quantity'])
print(df_data['Cocktail'])
plt.plot(
    df_data['Data_quantity'],
    df_data['Cocktail'],
)
plt.show()