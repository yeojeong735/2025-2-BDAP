import matplotlib.pyplot as plt
import os
import pandas as pd
from matplotlib import rc

rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

jumsu_data = [3.5, 4.1, 2.9, 3.9]
index_data = [2024,2025,2026,2027]

df = pd.DataFrame(
    {
        '학생1':jumsu_data,
    }
    ,index = index_data
)

df.plot.line()
plt.show()