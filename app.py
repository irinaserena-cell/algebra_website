import streamlit as st

# Настройки страницы
st.set_page_config(
    page_title="Алгебра: Подготовка к экзамену",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- УЛУЧШЕННЫЙ CSS СТИЛЬ ---
st.markdown("""
    <style>
    /* Подключение шрифта */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
        background-color: #ffffff;
    }

    /* Скрытие стандартных кружочков в радио-кнопках (Меню) */
    [data-testid="stSidebarNav"] {display: none;}
    [data-testid="stWidgetLabel"] {display: none;}
    
    .stRadio > div {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    
    .stRadio label {
        background-color: transparent !important;
        border: none !important;
        padding: 5px 0px !important;
        color: #555 !important;
        font-size: 16px !important;
        cursor: pointer;
        transition: 0.3s;
    }
    
    .stRadio label:hover {
        color: #000 !important;
        font-weight: bold;
    }

    .stRadio div[role="radiogroup"] > label > div:first-child {
        display: none !important; /* Прячем сами кружочки */
    }

    /* Контейнер для формул (голубой) */
    .formula-block {
        background-color: #e3f2fd;
        padding: 30px;
        border-radius: 15px;
        margin: 20px 0;
        text-align: center;
        border: 1px solid #bbdefb;
    }

    /* Контейнер для примеров (салатовый) */
    .example-block {
        background-color: #f1f8e9;
        padding: 30px;
        border-radius: 15px;
        margin: 20px 0;
        text-align: center;
        border: 1px solid #dcedc8;
    }

    /* Центрирование заголовков и текста */
    .center-text {
        text-align: center;
    }
    
    /* Стилизация заголовка вопроса */
    .question-title {
        font-size: 28px;
        font-weight: 700;
        color: #222;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# --- ДАННЫЕ (Вопросы 1-10) ---
# Для визуализации используем прямые ссылки на SVG/PNG схемы. 
# Если изображение не загрузится, будет показан текст.

CONTENT = {
    "1. Общее уравнение прямой. Каноническое уравнение прямой": {
        "theory": r"""
            Общее уравнение прямой на плоскости:
            $$Ax + By + C = 0$$
            Каноническое уравнение прямой (через точку и направляющий вектор):
            $$\frac{x - x_0}{p} = \frac{y - y_0}{q}$$
        """,
        "example": r"""
            **Задача:** Составить уравнение прямой через точку $M(1, 2)$ с направляющим вектором $\vec{a}(3, 4)$.
            <br>**Решение:** Подставляем в каноническую форму:
            $$\frac{x - 1}{3} = \frac{y - 2}{4}$$
        """,
        "img_url": "https://img.freepik.com/free-vector/coordinate-geometry-abstract-concept-vector-illustration-analytical-geometry-coordinate-system-line-equation-graphing-curves-geometric-problems-algebraic-equations-software-abstract-metaphor_335657-1786.jpg"
    },
    "2. Уравнение прямой в отрезках. Параметрическое уравнение прямой": {
        "theory": r"""
            Уравнение в отрезках (пересечение с осями $a$ и $b$):
            $$\frac{x}{a} + \frac{y}{b} = 1$$
            Параметрическое уравнение (через параметр $t$):
            $$\begin{cases} x = x_0 + pt \\ y = y_0 + qt \end{cases}$$
        """,
        "example": r"""
            **Задача:** Дано уравнение $2x + 4y = 8$. Привести к виду в отрезках.
            <br>**Решение:** Разделим всё на 8:
            $$\frac{x}{4} + \frac{y}{2} = 1$$
            Отрезки на осях: $a=4, b=2$.
        """,
        "img_url": None
    },
    "3. Расстояние от точки до прямой. Угол между двумя прямыми": {
        "theory": r"""
            Расстояние от точки $M_0(x_0, y_0)$ до прямой $Ax+By+C=0$:
            $$d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}$$
            Угол $\phi$ между прямыми с нормалями $\vec{n_1}$ и $\vec{n_2}$:
            $$\cos \phi = \frac{|A_1 A_2 + B_1 B_2|}{\sqrt{A_1^2 + B_1^2} \cdot \sqrt{A_2^2 + B_2^2}}$$
        """,
        "example": r"""
            **Пример:** Найти расстояние от $(0,0)$ до $3x+4y-5=0$.
            $$d = \frac{|3(0)+4(0)-5|}{\sqrt{3^2+4^2}} = \frac{5}{5} = 1$$
        """,
        "img_url": None
    },
    "4. Уравнение прямой в отрезках. Уравнение плоскости в отрезках": {
        "theory": r"""
            Уравнение плоскости, отсекающей на осях $Ox, Oy, Oz$ отрезки $a, b, c$:
            $$\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$$
        """,
        "example": r"""
            Если плоскость пересекает оси в точках $(2,0,0), (0,3,0), (0,0,1)$, её уравнение:
            $$\frac{x}{2} + \frac{y}{3} + \frac{z}{1} = 1$$
        """,
        "img_url": None
    },
    "5. Условие параллельности и перпендикулярности двух прямых": {
        "theory": r"""
            Для прямых $A_1x+B_1y+C_1=0$ и $A_2x+B_2y+C_2=0$:
            <br>**Параллельность:**
            $$\frac{A_1}{A_2} = \frac{B_1}{B_2} \neq \frac{C_1}{C_2}$$
            **Перпендикулярность:**
            $$A_1 A_2 + B_1 B_2 = 0$$
        """,
        "example": r"""
            Прямые $y=2x+1$ и $y=2x-5$ параллельны, так как $k_1 = k_2 = 2$.
            Прямые $y=2x$ и $y=-0.5x$ перпендикулярны, так как $2 \cdot (-0.5) = -1$.
        """,
        "img_url": None
    },
    "6. Общее уравнение плоскости. Расстояние от точки до плоскости": {
        "theory": r"""
            Общее уравнение плоскости:
            $$Ax + By + Cz + D = 0$$
            Расстояние от точки $M_0(x_0, y_0, z_0)$ до плоскости:
            $$d = \frac{|Ax_0 + By_0 + Cz_0 + D|}{\sqrt{A^2 + B^2 + C^2}}$$
        """,
        "example": r"""
            Найти расстояние от $(1,1,1)$ до плоскости $x+2y+2z-11=0$.
            $$d = \frac{|1+2+2-11|}{\sqrt{1+4+4}} = \frac{6}{3} = 2$$
        """,
        "img_url": None
    },
    "7. Уравнение окружности. Уравнение сферы": {
        "theory": r"""
            Окружность с центром $(x_0, y_0)$:
            $$(x-x_0)^2 + (y-y_0)^2 = R^2$$
            Сфера с центром $(x_0, y_0, z_0)$:
            $$(x-x_0)^2 + (y-y_0)^2 + (z-z_0)^2 = R^2$$
        """,
        "example": r"""
            Уравнение сферы с радиусом 5 и центром $(0,0,0)$:
            $$x^2 + y^2 + z^2 = 25$$
        """,
        "img_url": None
    },
    "8. Понятие вектора. Правил сложения векторов, умножение на скаляр": {
        "theory": r"""
            Сложение векторов по координатам:
            $$\vec{a} + \vec{b} = (a_x+b_x, a_y+b_y, a_z+b_z)$$
            Умножение на число $\lambda$:
            $$\lambda \vec{a} = (\lambda a_x, \lambda a_y, \lambda a_z)$$
        """,
        "example": r"""
            $\vec{a} = (1, 2)$, $\vec{b} = (3, 0)$. 
            Сумма: $\vec{a}+\vec{b} = (4, 2)$. 
            Умножение $2\vec{a} = (2, 4)$.
        """,
        "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Vector_addition.svg/300px-Vector_addition.svg.png"
    },
    "9. Определение скалярного произведения. Формула через координаты": {
        "theory": r"""
            Скалярное произведение через угол:
            $$\vec{a} \cdot \vec{b} = |\vec{a}| |\vec{b}| \cos \phi$$
            Через координаты:
            $$\vec{a} \cdot \vec{b} = a_x b_x + a_y b_y + a_z b_z$$
        """,
        "example": r"""
            $\vec{a} = (1, 2, 3)$, $\vec{b} = (4, 5, 6)$.
            $$\vec{a} \cdot \vec{b} = 1\cdot4 + 2\cdot5 + 3\cdot6 = 4 + 10 + 18 = 32$$
        """,
        "img_url": None
    },
    "10. Формула вычисления угла между векторами": {
        "theory": r"""
            Угол $\phi$ между векторами:
            $$\cos \phi = \frac{a_x b_x + a_y b_y + a_z b_z}{\sqrt{a_x^2+a_y^2+a_z^2} \cdot \sqrt{b_x^2+b_y^2+b_z^2}}$$
        """,
        "example": r"""
            Найти угол между $(1,1)$ и $(1,0)$.
            $$\cos \phi = \frac{1}{\sqrt{2} \cdot 1} = \frac{1}{\sqrt{2}} \Rightarrow \phi = 45^\circ$$
        """,
        "img_url": None
    }
}

# --- ЛОГИКА ПРИЛОЖЕНИЯ ---

# Боковое меню
st.sidebar.markdown("### МЕНЮ")
selected_q = st.sidebar.radio("", list(CONTENT.keys()))

# Основной контент
st.markdown(f'<div class="question-title">{selected_q}</div>', unsafe_allow_html=True)

data = CONTENT[selected_q]

# Блок Теории (Голубой)
st.markdown('<div class="center-text"><b>ТЕОРИЯ И ФОРМУЛЫ</b></div>', unsafe_allow_html=True)
st.markdown(f'<div class="formula-block">{data["theory"]}</div>', unsafe_allow_html=True)

# Визуализация (если есть URL)
if data["img_url"]:
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    st.image(data["img_url"], width=350)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="center-text" style="color:#ccc;">[ Схематичное изображение ]</div>', unsafe_allow_html=True)

# Блок Примера (Салатовый)
st.markdown('<div class="center-text"><b>ПРИМЕР РЕШЕНИЯ</b></div>', unsafe_allow_html=True)
st.markdown(f'<div class="example-block">{data["example"]}</div>', unsafe_allow_html=True)

# Футер
st.sidebar.markdown("---")
st.sidebar.markdown("<small>Algebra Exam Prep v2.0</small>", unsafe_allow_html=True)
