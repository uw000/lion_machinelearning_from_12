# streamlit에 쓸 파일
# ml은 colab
import streamlit as st

st.title("MachineLearning")
st.header("주식 예측 프로그램")

# Streamlit 애플리케이션 제목
st.title("기업 이름 입력")

# 사용자로부터 기업 이름을 입력받기
company_name = st.text_input("기업 이름을 입력하세요:")