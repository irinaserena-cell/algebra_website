import streamlit as st

# Настройки страницы
st.set_page_config(page_title="Алгебра Экзамен", layout="wide")

# Функция для подключения CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# --- КОНТЕНТ (1-10 ВОПРОСОВ) ---
CONTENT = {
    "1. Общее уравнение прямой. Каноническое уравнение прямой": {
        "theory": r"""
            $$Ax + By + C = 0$$
            $$\frac{x - x_0}{p} = \frac{y - y_0}{q}$$
        """,
        "example": r"""
            Через точку $M(1, 2)$ с вектором $\vec{a}(3, 4)$:
            $$\frac{x - 1}{3} = \frac{y - 2}{4}$$
        """,
        "image": "https://raw.githubusercontent.com/manim-community/manim/main/logo/cropped.png" # Заглушка
    },
    "2. Уравнение прямой в отрезках. Параметрическое уравнение прямой": {
        "theory": r"""
            В отрезках: $$\frac{x}{a} + \frac{y}{b} = 1$$
            Параметрическое: $$\begin{cases} x = x_0 + pt \\ y = y_0 + qt \end{cases}$$
        """,
        "example": r"""
            Для $2x + 4y = 8$: $$\frac{x}{4} + \frac{y}{2} = 1$$
        """,
        "image": None
    },
    "3. Расстояние от точки до прямой. Угол между двумя прямыми": {
        "theory": r"""
            Расстояние: $$d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}$$
            Угол: $$\cos \phi = \frac{|A_1 A_2 + B_1 B_2|}{\sqrt{A_1^2 + B_1^2} \cdot \sqrt{A_2^2 + B_2^2}}$$
        """,
        "example": r"""
            От $(0,0)$ до $3x+4y-5=0$: $$d = \frac{|-5|}{\sqrt{9+16}} = 1$$
        """,
        "image": None
    },
    "4. Уравнение прямой в отрезках. Уравнение плоскости в отрезках": {
        "theory": r"""
            Для плоскости: $$\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$$
        """,
        "example": r"""
            Через точки $(2,0,0), (0,3,0), (0,0,1)$: $$\frac{x}{2} + \frac{y}{3} + \frac{z}{1} = 1$$
        """,
        "image": None
    },
    "5. Условие параллельности и перпендикулярности двух прямых": {
        "theory": r"""
            Параллельность: $$\frac{A_1}{A_2} = \frac{B_1}{B_2}$$
            Перпендикулярность: $$A_1 A_2 + B_1 B_2 = 0$$
        """,
        "example": r"""
            $y=2x+1$ и $y=2x-5$ параллельны, так как коэффициенты при $x$ равны (2).
        """,
        "image": None
    },
    "6. Общее уравнение плоскости. Расстояние от точки до плоскости": {
        "theory": r"""
            Уравнение: $$Ax + By + Cz + D = 0$$
            Расстояние: $$d = \frac{|Ax_0 + By_0 + Cz_0 + D|}{\sqrt{A^2 + B^2 + C^2}}$$
        """,
        "example": r"""
            От $(1,1,1)$ до $x+2y+2z-11=0$: $$d = \frac{|1+2+2-11|}{\sqrt{1+4+4}} = 2$$
        """,
        "image": None
    },
    "7. Уравнение окружности. Уравнение сферы": {
        "theory": r"""
            Окружность: $$(x-x_0)^2 + (y-y_0)^2 = R^2$$
            Сфера: $$(x-x_0)^2 + (y-y_0)^2 + (z-z_0)^2 = R^2$$
        """,
        "example": r"""
            Сфера с $R=5$ в начале координат: $$x^2 + y^2 + z^2 = 25$$
        """,
        "image": None
    },
    "8. Понятие вектора. Правил сложения векторов, умножение на скаляр": {
        "theory": r"""
            Сумма: $$\vec{a} + \vec{b} = (a_x+b_x, a_y+b_y)$$
            Умножение: $$\lambda \vec{a} = (\lambda a_x, \lambda a_y)$$
        """,
        "example": r"""
            $\vec{a}=(1,2), \vec{b}=(3,0) \Rightarrow \vec{a}+\vec{b}=(4,2)$
        """,
        "image": None
    },
    "9. Определение скалярного произведения. Формула через координаты": {
        "theory": r"""
            $$\vec{a} \cdot \vec{b} = a_x b_x + a_y b_y + a_z b_z$$
            $$\vec{a} \cdot \vec{b} = |\vec{a}| |\vec{b}| \cos \phi$$
        """,
        "example": r"""
            $\vec{a}=(1,2), \vec{b}=(4,5) \Rightarrow 1\cdot4 + 2\cdot5 = 14$
        """,
        "image": None
    },
    "10. Формула вычисления угла между векторами": {
        "theory": r"""
            $$\cos \phi = \frac{a_x b_x + a_y b_y + a_z b_z}{\sqrt{\sum a_i^2} \cdot \sqrt{\sum b_i^2}}$$
        """,
        "example": r"""
            Между $(1,1)$ и $(1,0)$: $$\cos \phi = \frac{1}{\sqrt{2} \cdot 1} \Rightarrow 45^\circ$$
        """,
        "image": None
    }
}

# --- ИНТЕРФЕЙС ---

# Боковое меню (текстовые ссылки)
st.sidebar.markdown("### ВОПРОСЫ")
selected_q = st.sidebar.radio("Navigation", list(CONTENT.keys()), label_visibility="collapsed")

# Основной экран
st.markdown(f'<div class="main-title">{selected_q}</div>', unsafe_allow_html=True)

q_data = CONTENT[selected_q]

# Секция Теории
st.markdown('<div class="section-label">Теория и формулы</div>', unsafe_allow_html=True)
st.markdown(f'<div class="formula-block">{q_data["theory"]}</div>', unsafe_allow_html=True)

# Изображение
if q_data["image"]:
    st.markdown('<div class="centered-image">', unsafe_allow_html=True)
    st.image(q_data["image"], width=300)
    st.markdown('</div>', unsafe_allow_html=True)

# Секция Примера
st.markdown('<div class="section-label">Пример решения</div>', unsafe_allow_html=True)
st.markdown(f'<div class="example-block">{q_data["example"]}</div>', unsafe_allow_html=True)
