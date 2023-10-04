from utils import temp
from utils import module as md
import streamlit as st
import pandas as pd
from PIL import Image as img
import os

path = os.path.dirname(__file__)
parent_path = os.path.dirname(path)
utils_path = os.path.join(parent_path, 'utils')
data_path = os.path.join(utils_path, 'data')
image_path = os.path.join(data_path, 'image')
image_ = []

for i in range(1,10):
    image_.append(os.path.join(image_path,f'Khanun{i}.png'))

def app():

    # 8월 1일 ~ 8월 20일 하루 평균 기온 변화
    fig = md.hourmeantemp(temp.df_itp)
    st.pyplot(fig)
    st.write('8월 1일 ~ 8월 20일간의 하루 평균 기온 그래프입니다. 보통 우리가 생각하는 밤, 새벽에 쌀쌀하고 낮, 저녁에 더운,'
             ' 그런 온도 변화입니다.')

    fig_hour = md.hourgraph(temp.df_original, temp.df_itp)
    fig_day = md.dailygraph(temp.df_original, temp.df_itp)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.pyplot(fig_hour)
    with col2:
        st.pyplot(fig_day)
    
    st.write('왼쪽은 시간별 평균 기온이고 오른쪽은 일별 평균 기온입니다.')
    st.write('시간별 그래프 보간 전은 그래프가 몇군데 끊어진 부분이 있고'
             ' 일별 그래프 보간 전은 끊어진 곳이 없는데'
             ' 이는 데이터의 결측값이 특정 시간 전체여서 시간별 평균 기온 그래프에는 결측값이 표시가 되고'
             ' 일별 평균 기온 그래프에선 그 하루의 평균을 낸거라 결측부분이 존재하지않아 보이지 않는 것입니다.')
    st.write('10일 ~ 12일 기온이 급격하게 떨어지고 강수량이 높아지는데'
             ' 이 때가 태풍 카눈이 상륙한 날이여서 그런것 같습니다.')
    
    with st.expander('태풍 경로(10일, 11일)'):
        image_index = st.slider("이미지 선택", 0, 8, 0)
        st.image(img.open(image_[image_index]), caption=f"이미지 {image_index + 1}", use_column_width=True)
    
    # 8월1일~8월20일 시간대별 평균, 최대, 최소 기온
    df_day_gpd = md.monthstemp(temp.df_day) 
    st.dataframe(df_day_gpd)
    st.write('법과 절기학적으로 하루를 나누는것에 따라 새벽, 아침, 낮, 저녁, 밤으로 구분하여 1일~20일 전체의 평균, 최대, 최소 기온을 알아봤습니다.'
             ' 보통 낮이 아무리 추워도 밤이나 새벽보단 따뜻할텐데 낮, 저녁의 최소 기온값이 낮게 나온 이유는 태풍의 영향인것 같습니다.') 

    # 8월 10일 낮, 저녁, 밤 시간대 기온의 최솟값
    df1 = temp.df_day['2023-08-10'][temp.df_day['2023-08-10']['day'] == '낮'].resample('D').min()
    df2 = temp.df_day['2023-08-10'][temp.df_day['2023-08-10']['day'] == '저녁'].resample('D').min()
    new_df = pd.concat([df1, df2])
    st.dataframe(new_df)
    #st.dataframe(temp.df_day['2023-08-10'][temp.df_day['2023-08-10']['day'] == '낮'].resample('D').min())
    st.write('태풍 카눈의 상륙 날짜인 8월 10일 낮, 저녁 시간대 기온의 최솟값을 알아보니 추측이'
             ' 맞습니다.')
    
    # 일별 시간대 평균 기온 그래프
    fig = md.dailytemp(temp.df_day) 
    st.pyplot(fig)
    st.write('일별 시간대 평균 기온 그래프와 평균 기온이 제일 높은 낮과 제일 낮은 아침 그래프입니다. 태풍 시기를 제외하면'
             ' 대체적으로 낮, 저녁이 기온이 높고 아침, 새벽이 기온이 낮으며 밤이 그 중간인걸 알 수 있습니다.')

    # 이동 평균 그래프
    fig = md.meangraph(temp.df_itp)
    st.pyplot(fig)
    st.write('원본 그래프는 시간대에 따라 매일 비슷한 기온 변화 양상을 보이는데 '
    '전체적인 추세를 파악하기엔 불편합니다. 그래서 이동평균을 표시해 봤습니다.'
    ' 1, 3, 8시간은 범위가 작아서인지 원본과 비슷하지만 1일은 기온 변화의 추세를'
    ' 보기 쉽게 보여주고 있습니다.'
    ' 1일 그래프를 보면 9일까진 중간에 기온이 떨어지기는 하나 대체적으로 기온이'
    ' 상승하고 있습니다. 9일 이후 11일까지는 태풍의 영향으로 기온이 급격하게 '
    '떨어지고 이후 점차 정상적인 기온으로 회복하고 있는 것을 알 수 있습니다.')
    st.write('8월 1일~2일 부분이 원본 그래프와 비슷한 것은'
    ' 하루 이동 평균을 구하는 거라 2일 전까진 데이터가 부족해서 그렇습니다.')

    # 변수들간 상관성 파악을 위한 그래프 그리기
    fig = md.scatt(temp.df_day_copy)
    st.pyplot(fig)
    st.write('기온과 나머지 변수들 간의 산점도 그래프입니다. 기온을 기준으로 습도, 일사량, 일조시간이 상관성을 보이고'
             ' 예상과 다르게 강수량은 큰 상관성을 가지지는 않은것으로 보입니다.')

    # 기온 ~ 나머지변수 간의 상관관계 알아보기
    p_values_df = md.corr(temp.df_day_copy)
    st.dataframe(p_values_df)
    st.write('상관계수가 유의미한지에 대한 p-value 값입니다. 전부 0으로 상관계수가 유효하다는걸 알 수 있습니다.')
    
    # 기온 ~ 나머지 변수의 상관계수
    st.write(temp.df_day_copy.corr())
    st.write('기온에 대해 습도가 가장 높은 상관관계를 가진것으로 나타났고 일조시간, 일사량, 누적강수량 순으로 높은'
              ' 상관관계를 가지고 있습니다. 누적강수량은 그래프에서 확인한거와 달리 적당한 상관관계를 가지고 있고'
              ' 풍향, 풍속, 현지기압, 해면기압은 상관관계에 있기는 하나 그 수치가 낮습니다.')

    # 기온 ~ 상관관계에 있는 변수들 그래프
    fig = md.hourgraph_all(temp.df_day_copy)
    st.pyplot(fig)
    st.write('기온과 상관관계에 있는 변수들에 대한 그래프 입니다. 시간의 흐름에 따라 대체적으로 비슷하게'
             ' 변화하는것이 반복되고 태풍 시기에만 다른것을 확인 할 수 있습니다. 8월 20일보다 뒤에 그래프가 더 '
             '이어지는것은 8월20일 부분이 8월 20일 0시여서 그 이후인 8월 20일 23시까지 표시된것 입니다.')

    # 8월 2일과 8월 10일부분만 그래프로 나타내기
    fig = md.hourgraph_oneday(temp.df_day_copy)
    st.pyplot(fig)
    st.write('이전 그래프에서 반복되는 부분과 반복되지 않는 부분만 따로 뽑아봤습니다.')
    st.write('상관계수에서 파악했던 것과 같이 습도, 일조시간, 일사량, 강수량의 변화에 따라 기온도 같이 변화합니다.'
             ' 8월 2일에는 18시쯤 해가 떨어져 기온도 떨어집니다.'
             ' 8월 10일은 태풍 카눈이 한국에 상륙한 날로 일조시간은 0이고 누적 강수량을 봤을때 새벽3시부터'
             ' 태풍의 영향권에 들었음을 알 수 있습니다.')


