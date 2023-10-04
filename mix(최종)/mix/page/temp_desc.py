from utils import temp
from utils import module as md
import streamlit as st
import io
import pandas as pd

def app():
    url_temp = 'https://data.kma.go.kr/data/grnd/selectAsosRltmList.do?pgmNo=36&tabNo=1'
    
    st.header('서울 기온 변화')
    st.markdown(f'출처 : {url_temp} 에서 자료형태 : 분 자료, 지점 : 서울특별시 > 서울 (108) 선택, 기간 2023년 ~ 2023년 선택후'                  ' SURFACE_ASOS_108_MI_2023-08_2023-08_2023.zip 다운로드')
    
    st.dataframe(temp.df_main1)
    
    buffer = io.StringIO()
    temp.df_main1.info(buf=buffer)
    info_str = buffer.getvalue()
    
    with st.expander("서울 기온 Info"):
        st.text(info_str)
        st.info('일사량 : 태양으로부터 지구로 복사되는 에너지')
        st.info('일조시간 : 태양의 직사광이 구름이나 안개에 가려지지 않고 지표면에 비친 시간')
        st.info('현지기압 : 기차보정, 온도보정, 중력보정을 거친 기압')
        st.info('해면기압 : 관측소에서 관측한 기압을 관측소의 해발고도에 대해 보정한 기압')
    st.write('최초의 데이터 상태입니다. info를 확인해 보니 33,179개의 행과 11개의 열로 이뤄져있고 '
            '일시가 시간데이터가 아니며 누적 강수량에 결측값이 있습니다.')
    st.write('일조시간과 일사량이 측정 되지않을 시간인 19시 이후에도 값이 존재하고 이전 값과 동일함을 봤을 때'
             ' 이 두 변수의 값은 누적되는 값임을 확인할 수 있고 다음날 00시 01분에 0으로 돌아가는 것으로 보아'
             '하루마다 갱신되는것 같습니다.')
    st.write('필요한 기간이 8월 1일에서 8월 20일까지라 그 부분만 추출하고 다음 작업을 했습니다.')
    st.write('1. 결측치 -> np.nan')
    st.write('2. 일시 -> datetime, 일시 -> index')
    st.write('3. 기온 단위 기호 -> 한글')
    st.write('4. 분별 온도차가 3도를 넘어가면 오류 처리')
    st.write('5. 시간마다 분별 온도차의 합이 0.1보다 작은경우 오류 처리')
    
    st.dataframe(temp.df)
    st.write('작업을 진행한 데이터 입니다.')
    st.dataframe(md.printcheckData(temp.df))
    st.write('기온 데이터의 갯수가 80퍼 이하인 시간대입니다.')
    
    st.dataframe(pd.concat([temp.df_itp['2023-08-05 04'], temp.df_itp['2023-08-10 06':'2023-08-10 07'], temp.df_itp['2023-08-10 09'],
                            temp.df_itp['2023-08-11 10'], temp.df_itp['2023-08-11 18'], temp.df_itp['2023-08-12 00'],
                            temp.df_itp['2023-08-12 21']]))
    url_temp_model = 'https://bd.kma.go.kr/contest/downloadFile.do?fileCd=FIL20221018092548996W1cO719z82'
    st.markdown(f'{url_temp_model} 링크를 참고하여 각 분마다 급격한 기온 변화가 있을거라고 생각하지 않아 시간 선형 보간을 사용하였고'
                ' 적용된 시간대입니다.')
    
    st.dataframe(temp.df_day)
    st.write('하루는 법과 절기학으로 0\~5시는 새벽, 5\~9시는 아침, 9\~17시는 낮, 17\~21시는 저녁, 21\~24시는 밤을 의미합니다. 그에 따라 day라는 열을 추가하였습니다.')

