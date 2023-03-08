import yfinance as yf
import pandas as pd
import streamlit as st

# Настройки приложения
st.set_page_config(layout='wide')

# Заголовок и подзаголовок для приложения
st.title('Котировки компании Apple :chart_with_upwards_trend:')
st.subheader('Показывает цены акций в момент закрытия торгов и их объем компании Apple')

# Данные для визуализации в приложении
aapl = yf.Ticker('AAPL')

# Select_Slider
period_graph = st.select_slider('Выбери период',
                                 options = ['5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'max'])

aapl_df = aapl.history(period=period_graph, interval='1d')

#Колонки
col1, col2 = st.columns(2, gap='large')

# Графики
with col1:
    st.write("""
    Цена акции в момент закрытия торгов
    """)
    st.line_chart(aapl_df.Close, y='Close')

with col2:
    st.write("""
    Объем акций
    """)
    st.line_chart(aapl_df.Volume, y='Volume') 