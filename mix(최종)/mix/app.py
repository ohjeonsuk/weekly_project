import streamlit as st

from page import data1_client as dc1
from page import data2_client as dc2
from page import data3_client as dc3
from page import data4_client as dc4
from page import data5_client as dc5
from page import data6_client as dc6
from page import data7_client as dc7
from page import data8_client as dc8

from page import intro
from page import anl_page_01 as ap1
from page import temp_desc
from page import run_temp

# 페이지 클래스
class Page1:
    def show(self):
        intro.app()
        
class Page2:
    def show(self):
        st.title("Class Diagram")
        ap1.app()

class Page3:
    def show(self):
        st.title('서울 기온 변화 데이터')
        temp_desc.app()

class Page4:
    def show(self):
        st.title("서울 기온 변화")
        run_temp.app()

class Page5:
    def show(self):
        st.title("데이터 분석")
        s_box = st.selectbox('원하는 부분을 고르세요', ('국내 반도체 시장 구조', '국내 반도체 수출액 비중', '경제지수', \
                                              '국내 수출 반도체 수요 분야', '글로벌 반도체 시장', '반도체 자본시장')) 
        if s_box == '국내 반도체 시장 구조':
            dc1.result1()
            dc1.result2()
        elif s_box == '국내 반도체 수출액 비중':
            dc2.result3()
            dc2.result4()
            dc3.result5()
            dc4.result6()
        elif s_box == '경제지수':
            dc5.result7()
            dc5.result8()
            dc5.result9()
        elif s_box == '국내 수출 반도체 수요 분야':
            dc6.result10()
        elif s_box == '글로벌 반도체 시장':
            dc7.result11()
            dc7.result12()
        elif s_box == '반도체 자본시장':
            dc8.result13()
            dc8.result14()


# 페이지 전환을 관리하는 클래스
class MultiPageApp:
    def __init__(self):
        self.pages = {
            "Main": Page1(),
            "Class Diagram": Page2(),
            '서울의 기온 - 데이터 처리 과정': Page3(),
            "서울의 기온 - 시각화": Page4(),
            "데이터 분석": Page5()
        }
        self.page_names = list(self.pages.keys())
        self.current_page = self.page_names[0]

    def run(self):
        st.sidebar.title("2조 Streamlit")
        self.current_page = st.sidebar.selectbox("고르세요", self.page_names)
        self.pages[self.current_page].show()

# 멀티 페이지 애플리케이션 실행
app = MultiPageApp()
app.run()