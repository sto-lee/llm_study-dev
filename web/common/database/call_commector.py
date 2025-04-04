from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os

########################################################
# 데이터베이스 영역
# @st.cache_resource -> 만약 connector가 메모리 존재하지 않을 때만, connector 생성 
# -> 메모리에 존재한다면, 기존 connector 리턴 
########################################################
@st.cache_resource 
def get_connector():
  return st.connection(
    name="my_db",
    type="sql",
    dialect="postgresql",
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME"),
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
  )