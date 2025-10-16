import pandas as pd
import matplotlib.pyplot as plt
from ch05.common_function import init_matplotlib

init_matplotlib()

# 전달받은 파일명에 해당하는 Data 리턴 함수
def get_data(filename):
    # 1. csv 파일 읽기
    kor_df = pd.read_csv(filename)

    # 2. 인덱스로 사용할 열 이름 지정
    index_name = 'date'

    # 3. 인덱스 설정
    kor_index_df = kor_df.set_index(index_name)

    # 4. 특정 열 선택 및 반환
    return kor_index_df['total_cases']
# end-def

kor_data = get_data('./data/covid_kor.csv')
usa_data = get_data('./data/covid_usa.csv')
index_name = kor_data.index

df = pd.DataFrame(
    {
        '대한민국':kor_data,
        '미국': usa_data,
    },
    index=index_name
)
df.plot.line()
plt.show()

