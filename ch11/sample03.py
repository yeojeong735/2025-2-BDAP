import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 1. 데이터 불러오기 및 전처리
file_name = './data_raw.csv'
df_raw = pd.read_csv(file_name)

ds_data = df_raw.groupby(['Country']).size()
top_20_countries = ds_data.nlargest(20)

# 2. 국가명 번역 맵 및 라벨 적용
country_translation = {
    'United States of America': '미국',
    'India': '인도',
    'Germany': '독일',
    'United Kingdom of Great Britain and Northern Ireland': '영국',
    'Canada': '캐나다',
    'France': '프랑스',
    'Brazil': '브라질',
    'Poland': '폴란드',
    'Netherlands': '네덜란드',
    'Spain': '스페인',
    'Italy': '이탈리아',
    'Australia': '호주',
    'Russian Federation': '러시아',
    'Sweden': '스웨덴',
    'Turkey': '터키',
    'Switzerland': '스위스',
    'Austria': '오스트리아',
    'Israel': '이스라엘',
    'Iran, Islamic Republic of...': '이란',
    'Pakistan': '파키스탄'
}

# 라벨을 한글로 번역합니다.
translated_top_20 = top_20_countries.rename(index=country_translation)

# 3. Matplotlib에서 한글 폰트 설정
try:
    font_manager = fm.FontManager()

    # 일반적인 한글 폰트 검색 (Malgun, Nanum, AppleGothic 등)
    korean_fonts = [f.name for f in font_manager.ttflist if
                    'Malgun' in f.name or 'Nanum' in f.name or 'AppleGothic' in f.name]

    if korean_fonts:
        font_name = korean_fonts[0]
    else:
        # 한글 폰트가 없을 경우 기본 폰트를 사용합니다.
        font_name = 'sans-serif'

    plt.rcParams['font.family'] = font_name
    plt.rcParams['axes.unicode_minus'] = False  # 마이너스 부호 깨짐 방지

except Exception as e:
    # 예외 발생 시 기본 폰트 사용
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['axes.unicode_minus'] = False

# 4. 파이 차트 생성 및 화면 출력
plt.figure(figsize=(12, 12))
translated_top_20.plot.pie(  # <--- 번역된 데이터를 사용하여 한글 라벨 출력
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'edgecolor': 'black'},
    textprops={'fontsize': 10}
)

plt.ylabel('')  # Y축 라벨 제거 (파이 차트 기본)
plt.tight_layout()
plt.show()  # <--- 화면에 차트 표시



