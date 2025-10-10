import pandas as pd
import os

covid_file_name = './data/owid-covid-data.csv'
raw_df = pd.read_csv(covid_file_name, sep = ',')

# data 칼럼을 index로 지정
