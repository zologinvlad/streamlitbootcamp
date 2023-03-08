import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.express as px


# Title
st.title('Иследование датасета tips.csv')

# Read and data preparation
path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(path)

def data_preparation(data):
    func_replace = lambda x: str(x).replace('_', ' ')
    func_capitalize = lambda x: str(x).capitalize()
    data.rename(func_replace, axis='columns', inplace=True)
    data.rename(func_capitalize, axis='columns', inplace=True)
    return data

df = data_preparation(tips)

# Print dataset
st.write('''
### Данные для иследования
''')
rows_count = st.slider('Количество строк', 0, 244, 1)
st.dataframe(df.head(rows_count), use_container_width=True)

# First graph
st.write('''
### Гистограмма Total bill
''')
fig = sns.displot(df['Total bill'], height=3, aspect=3)
st.pyplot(fig)

# Second graph
st.write('''
### Scatterplot показывающий взаимосвязь Totall bill и Tip
''')
fig = px.scatter(df, x='Total bill', y='Tip', color='Day')
st.plotly_chart(fig, use_container_width=True)

# Third graph
st.write('''
### Графики зависимости Total bill, Tip и Size
''')
x_axe = st.multiselect('Варианты оси X', ['Total bill', 'Tip', 'Size'], ['Total bill', 'Tip'])
y_age = st.multiselect('Варианты оси Y', ['Total bill', 'Tip', 'Size'], ['Size', 'Total bill'])
fig = sns.pairplot(df, x_vars=x_axe, y_vars=y_age, height=2, aspect=2)
st.pyplot(fig)

# Fourth graph
st.write('''
### Графики зависимости между днем недели и размером счета
''')
fig = px.box(df, x='Day', y='Total bill', color='Day')
st.plotly_chart(fig, use_container_width=True)

# Fifth graph
st.write('''
### Scatterplot зависимости дня недели и размера чаевых
''')
fig = px.scatter(df, x='Tip', y='Day', color='Sex')
st.plotly_chart(fig, use_container_width=True)

# Six graph
st.write('''
### Boxplot зависимости Total bill за каждый день, разбитый по времени
''')
fig = px.box(df, x='Day', y='Total bill', color='Time')
st.plotly_chart(fig, use_container_width=True)

# Seven graph
st.write('''
### Гистограммы чаевых на обед и ланч
''')
fig = sns.FacetGrid(df, col='Time')
fig.map(plt.hist, 'Tip')
st.pyplot(fig)

# Eight graph
st.write('''
### Два scatterplots (для мужчин и женщин), показывающих связь размера счета и чаевых, дополнительно разбитые по курящим/некурящим.
''')
fig = sns.FacetGrid(df, col='Sex', hue='Smoker')
fig.map(plt.scatter, 'Total bill', 'Tip')
fig.add_legend()
st.pyplot(fig)