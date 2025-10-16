import platform

from matplotlib import pyplot as plt
from matplotlib import rc

# 현재 파이썬이 실행되는 플랫폼 확인

def is_windows_platform():
    return platform.system() == 'Windows'

def is_mac_platform():
    return platform.system() == 'Darwin' # !!!

def is_linux_platform():
    return platform.system() == 'Linux'

def get_font_name():
    if is_mac_platform():
        return 'AppleGothic'
    elif is_linux_platform():
        return 'linuxFont'
    else:
        return 'Malgun Gothic'

def init_matplotlib():
    # 한글폰트 처리(깨짐 처리)
    rc('font', family=get_font_name()) # rc : run commands, matplotlib의 여러 설정 값을 지정할 때 사용
    # ㄴ 설정 대상 - 'font' / 폰트 계열(family)을 get_font_name()가 반환하는 폰트 이름으로 설정
    plt.rcParams['axes.unicode_minus'] = False
    # ㄴ 그래프의 축에 있는 마이너스 기호를 정상적으로 표시하기 위한 설정