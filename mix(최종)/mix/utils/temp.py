from utils import module as md
import pandas as pd
from matplotlib import font_manager as fm

import numpy as np

# 기본 데이터 전처리
font_path = 'NanumGothic.ttf'
fontprop = fm.FontProperties(fname=font_path)

df_main1 = pd.read_csv('SURFACE_ASOS_108_MI_2023-08_2023-08_2023.csv', encoding='euc-kr')
df_main2 = df_main1.fillna(np.nan)		# 결측치 to np.nan
df_main2['일시'] = pd.to_datetime(df_main2['일시'])	# '일시' 열 타입 변환
df_main2.set_index('일시', inplace=True) # '일시' 열 인덱스화

df_main_ = df_main2[:'2023-08-20']	# 8월 1일 ~ 8월 20일
df = df_main_.copy()
df.rename(columns={'기온(°C)':'기온(섭씨)'}, inplace=True)	# 칼럼 쓰기 쉽게 변환
df = md.diffError(df, '기온(섭씨)') # 분별 온도차가 3도를 넘는경우 np.nan 처리
df = md.diffSumError(df, '기온(섭씨)') # 시간마다 분별 온도차의 합이 0.1보다 작은 경우 np.nan 처리

# 80% 확인 후 보간
df_original = df.copy() # 보간 전 데이터( == 결측값 보유한 데이터)
df_itp = md.checkData(df)   # 보간 후 데이터

# 절기학으로 구분된 day열 추가

df_day = md.groupDay(df_itp, 'day')
df_day_copy = df_day.copy()
df_day_copy['day'] = df_day_copy['day'].cat.codes
#print(df_day.corr())
