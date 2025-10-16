import matplotlib.pyplot as plt
import os
import pandas as pd
from matplotlib import rc

from ch05.common_function import get_font_name

# 한글 폰트 처리(깨짐처리)
rc('font', family=get_font_name())
plt.rcParams['axes.unicode_minus'] = False

jumsu1_data = [3.5, 4.1, 2.9, 3.9]
jumsu2_data = [3.51, 4.51, 2.79, 2.9]
index_data = [2024,2025,2026,2027]

df = pd.DataFrame(
    {
        '학생1':jumsu1_data,
        '학생2':jumsu2_data,
    }
    ,index = index_data
)

df.plot.line()
plt.show()