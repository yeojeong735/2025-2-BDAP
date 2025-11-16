import pandas as pd
import matplotlib.pyplot as plt

file_name = './data_raw.csv'
df_raw = pd.read_csv(file_name)

# 개발자 연령대

COLUMN_AGE = 'Age'

sr_data = df_raw[COLUMN_AGE]
print('-'*100)
print(sr_data)

print('-'*100)
print(sr_data.unique())

print('-'*100)
print(type(sr_data.drop_duplicates()))
print(sr_data.drop_duplicates())

ds_data = df_raw.groupby([COLUMN_AGE]).size()

reindex_column = [
         '25-34 years old',
         '35-44 years old',
      'Under 18 years old',
         '18-24 years old',
         '45-54 years old',
        '55-64 years old',
      '65 years or older',
     'Prefer not to say'
]
ds_data = ds_data.reindex(reindex_column)

#ds_data.plot.line(rot=45)
#ds_data.plot.bar()
ds_data.plot.barh()

plt.tight_layout()
plt.show()
