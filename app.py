import streamlit as st
import plotly.graph_objects as go
import numpy as np
from content import QUESTIONS

# Настройка страницы
st.set_page_config(page_title="Algebra Exam", layout="wide")

# Загрузка CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css("style.css")

# Боковое меню
st.sidebar.markdown("<h2 style='text-align: center;'>Вопросы</h2>", unsafe_allow_html=True)
selected_title = st.sidebar.radio("", list(QUESTIONS.keys()))

# Заголовок
st.markdown(f'<div class="title-text">{selected_title}</div>', unsafe_allow_html=True)

# Функция для создания реальных визуализаций
def draw_geometry(title):
    fig = go.Figure()
    
    if "1." in title: # Прямая
        x = np.linspace(-5, 5, 10)
        y = (2*x + 13)/3
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Прямая'))
        fig.update_layout(title="График прямой", height=300)

    elif "7." in title: # Сфера (проекция)
        theta = np.linspace(0, 2*np.pi, 100)
        fig.add_trace(go.Scatter(x=4*np.cos(theta), y=4*np.sin(theta), fill="toself", name='Сфера (сечение)'))
        fig.update_layout(title="Сечение сферы R=4", height=300, yaxis=dict(scaleanchor="x"))

    elif "8." in title: # Векторы
        fig.add_trace(go.Scatter(x=[0, 1], y=[0, 2], mode='lines+markers', name='Вектор A'))
        fig.add_trace(go.Scatter(x=[1, 4], y=[2, 3], mode='lines+markers', name='Вектор B'))
        fig.add_trace(go.Scatter(x=[0, 4], y=[0, 3], mode='lines+markers', name='Сумма A+B'))
        fig.update_layout(title="Сложение векторов", height=300)

    if len(fig.data) > 0:
        fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig, use_container_width=True)

# РЕНДЕРИНГ КОНТЕНТА
data = QUESTIONS[selected_title]

# Блок Теории
st.markdown('<div class="theory-block">', unsafe_allow_html=True)
st.markdown(f'<span class="centered">{data["theory_text"]}</span>', unsafe_allow_html=True)
for m in data["theory_math"]:
    st.latex(m)
st.markdown('</div>', unsafe_allow_html=True)

# Визуализация (между блоками)
draw_geometry(selected_title)

# Блок Примера
st.markdown('<div class="example-block">', unsafe_allow_html=True)
st.markdown(f'<span class="centered">{data["example_text"]}</span>', unsafe_allow_html=True)
for m in data["example_math"]:
    st.latex(m)
st.markdown('</div>', unsafe_allow_html=True)
