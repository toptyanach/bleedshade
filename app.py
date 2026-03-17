import streamlit as st

# ✦ КОНФИГУРАЦИЯ СТРАНИЦЫ
st.set_page_config(
    page_title="bleedshade | portfolio", 
    page_icon="🦇", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# ✦ КАСТОМНЫЙ СТИЛЬ (ВАЙБОВЫЙ DARK MODE)
st.markdown("""
<style>
    /* Прячем дефолтное меню Streamlit для чистоты */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Стили текста и акцентов */
    .title-text {
        font-size: 4rem;
        font-weight: 900;
        background: -webkit-linear-gradient(45deg, #a78bfa, #f472b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
        padding-bottom: 0;
    }
    .subtitle-text {
        font-size: 1.5rem;
        color: #94a3b8;
        font-weight: 500;
        margin-top: -10px;
        margin-bottom: 20px;
    }
    
    /* Карточки опыта и образования */
    .glass-card {
        background: rgba(30, 41, 59, 0.5);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(167, 139, 250, 0.2);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 16px;
        transition: transform 0.2s, border-color 0.2s;
    }
    .glass-card:hover {
        border-color: rgba(167, 139, 250, 0.6);
        transform: translateY(-2px);
    }
    .card-title {
        color: #f8fafc;
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 4px;
    }
    .card-subtitle {
        color: #a78bfa;
        font-size: 1rem;
        font-weight: 500;
        margin-bottom: 12px;
    }
    .card-date {
        color: #64748b;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 12px;
        display: block;
    }
    
    /* Скиллы (пилюли) */
    .skill-container {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 10px;
    }
    .skill-pill {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid #334155;
        color: #e2e8f0;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 500;
        transition: all 0.2s;
    }
    .skill-pill:hover {
        border-color: #a78bfa;
        color: #a78bfa;
        background: rgba(167, 139, 250, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# ✦ УПРАВЛЕНИЕ СОСТОЯНИЕМ (ЯЗЫК)
if 'lang' not in st.session_state:
    st.session_state.lang = 'ru'

# ✦ ДАННЫЕ (RU & EN)
content = {
    'ru': {
        'name': 'Әсем Әбдрашіт',
        'role': 'Software Engineer / AI & Web Developer',
        'about': 'Привет. Я программист, веб-разработчик и создатель ИИ-решений. Люблю писать чистый код, собирать крутые штуки на Python/C++ и разрабатывать умных Telegram-ботов с искусственным интеллектом. Открыта к переезду и новым вызовам.',
        'exp_header': '✦ Опыт работы',
        'edu_header': '✦ Образование',
        'skills_header': '✦ Стек и навыки',
        'contact_header': '✦ Контакты',
        'location': 'Шымкент, Казахстан',
        'relocation': 'Готова к переезду (Астана, Москва, Тбилиси)',
        'exp': [
            {'role': 'Фрилансер', 'company': 'Профи (profi.ru)', 'date': 'Июнь 2023 — Настоящее время', 'desc': 'Беру интересные проекты, занимаюсь разработкой, обеспечиваю техподдержку и менторю/репетиторствую.'},
            {'role': 'Python-разработчик', 'company': 'TOO «MAGIC ENGINEERING»', 'date': 'Июнь 2024 — Июль 2024', 'desc': 'Писала софт для автоматизации расчетов и смет. Никакой рутины, только хардкорная автоматизация.'},
            {'role': 'Backend-разработчик', 'company': 'TOO ZHIBER.KZ', 'date': 'Февраль 2024 — Март 2024', 'desc': 'Занималась бэкендом: отлавливала баги, устраняла дефекты на стороне сервера и делала так, чтобы всё работало быстро.'},
            {'role': 'Flutter разработчик', 'company': 'Lief & Co.', 'date': 'Июнь 2023 — Январь 2024', 'desc': 'Пилила мобильные приложения на Flutter. Отвечала за разработку программного обеспечения с нуля.'},
            {'role': 'Разработчик ПО (C++)', 'company': 'Turandot', 'date': 'Июль 2023 — Декабрь 2023', 'desc': 'Разработка на C++ с использованием Qt5, JS, Node.js. Создавала ПО и внедряла его в CRM систему. Оказывала техподдержку и консультировала.'}
        ],
        'edu': [
            {'degree': 'Информационные технологии и прикладная математика', 'place': 'ЮКУ им. М. Ауэзова', 'date': '2024 — 2027'},
            {'degree': 'Техник-программист (ВТиПО)', 'place': 'Колледж «Мирас»', 'date': 'Окончила в 2024'}
        ]
    },
    'en': {
        'name': 'Assem Abdrashit',
        'role': 'Software Engineer / AI & Web Developer',
        'about': "Hey. I'm a software engineer, web developer, and AI enthusiast. I build clean, scalable solutions using Python/C++ and create smart AI-powered Telegram bots. Always open to relocation and exciting new challenges.",
        'exp_header': '✦ Experience',
        'edu_header': '✦ Education',
        'skills_header': '✦ Tech Stack',
        'contact_header': '✦ Contacts',
        'location': 'Shymkent, Kazakhstan',
        'relocation': 'Open to relocate (Astana, Moscow, Tbilisi)',
        'exp': [
            {'role': 'Freelance Developer', 'company': 'Profi.ru', 'date': 'June 2023 — Present', 'desc': 'Taking on custom projects, developing software solutions, providing tech support, and tutoring.'},
            {'role': 'Python Developer', 'company': 'MAGIC ENGINEERING LLC', 'date': 'June 2024 — July 2024', 'desc': 'Developed specialized software for estimate automation. Turned routine tasks into optimized code.'},
            {'role': 'Backend Developer', 'company': 'ZHIBER.KZ LLC', 'date': 'Feb 2024 — March 2024', 'desc': 'Handled server-side operations, hunted down bugs, and fixed backend defects to ensure smooth performance.'},
            {'role': 'Flutter Developer', 'company': 'Lief & Co.', 'date': 'June 2023 — Jan 2024', 'desc': 'Built cross-platform mobile applications from scratch using Flutter.'},
            {'role': 'Software Developer (C++)', 'company': 'Turandot', 'date': 'July 2023 — Dec 2023', 'desc': 'Developed software using C++, Qt5, JS, and Node.js. Integrated solutions into CRM systems and provided technical consulting.'}
        ],
        'edu': [
            {'degree': 'IT and Applied Mathematics', 'place': 'Auezov South Kazakhstan University', 'date': '2024 — 2027'},
            {'degree': 'Software Technician', 'place': 'Miras College', 'date': 'Graduated 2024'}
        ]
    }
}

skills = [
    "Python", "C++", "C#", "JavaScript", "Flutter", 
    "AI Development", "Telegram API", "Node.js", "Qt5",
    "SQL", "MySQL", "JSON", "Linux", "Windows", 
    "HTML5 / CSS", "System Administration", "PC Diagnostics"
]

# Функция переключения языка
def set_lang(lang_code):
    st.session_state.lang = lang_code

t = content[st.session_state.lang]

# ✦ САЙДБАР (Навигация и Контакты)
with st.sidebar:
    st.markdown("<h2 style='color: #a78bfa;'>settings_</h2>", unsafe_allow_html=True)
    
    # Кнопки переключения языка
    col1, col2 = st.columns(2)
    with col1:
        st.button("🇷🇺 RU", on_click=set_lang, args=('ru',), use_container_width=True, type="primary" if st.session_state.lang == 'ru' else "secondary")
    with col2:
        st.button("🇬🇧 EN", on_click=set_lang, args=('en',), use_container_width=True, type="primary" if st.session_state.lang == 'en' else "secondary")
    
    st.markdown("---")
    
    st.markdown(f"<h3>{t['contact_header']}</h3>", unsafe_allow_html=True)
    st.markdown("📧 **Email:**<br>top.tyanach@gmai.com", unsafe_allow_html=True)
    st.markdown("📱 **Phone:**<br>+7 (706) 663-83-14", unsafe_allow_html=True)
    st.markdown(f"📍 **Location:**<br>{t['location']}", unsafe_allow_html=True)
    st.markdown(f"✈️ **Status:**<br>{t['relocation']}", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.8rem;'>built by bleedshade 🦇</p>", unsafe_allow_html=True)


# ✦ ОСНОВНОЙ КОНТЕНТ
# Заголовок
st.markdown("<h1 class='title-text'>bleedshade</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='subtitle-text'>{t['name']} // {t['role']}</p>", unsafe_allow_html=True)

# Обо мне
st.write(t['about'])
st.markdown("<br>", unsafe_allow_html=True)

# Разделение на две колонки для контента
left_col, right_col = st.columns([1.5, 1])

with left_col:
    st.markdown(f"<h3>{t['exp_header']}</h3>", unsafe_allow_html=True)
    
    for job in t['exp']:
        st.markdown(f"""
        <div class="glass-card">
            <span class="card-date">{job['date']}</span>
            <div class="card-title">{job['role']}</div>
            <div class="card-subtitle">@{job['company']}</div>
            <div style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.5;">{job['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

with right_col:
    st.markdown(f"<h3>{t['edu_header']}</h3>", unsafe_allow_html=True)
    
    for ed in t['edu']:
        st.markdown(f"""
        <div class="glass-card">
            <span class="card-date">{ed['date']}</span>
            <div class="card-title">{ed['degree']}</div>
            <div class="card-subtitle">{ed['place']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<h3>{t['skills_header']}</h3>", unsafe_allow_html=True)
    
    # Генерация HTML для скиллов
    skills_html = '<div class="skill-container">'
    for skill in skills:
        skills_html += f'<span class="skill-pill">{skill}</span>'
    skills_html += '</div>'
    
    st.markdown(skills_html, unsafe_allow_html=True)
