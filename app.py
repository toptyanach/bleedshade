import streamlit as st

# Настройки страницы
st.set_page_config(
    page_title="Resume | Assem Abdrashit",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- МОЩНЫЙ CSS ДЛЯ АНИМАЦИЙ И PREMIUM-ДИЗАЙНА ---
st.markdown("""
<style>
    /* Плавное появление всей страницы при загрузке */
    @keyframes slideUpFade {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .block-container {
        animation: slideUpFade 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    /* Анимация картинок (ч/б по умолчанию, цветнеют при наведении) */
    [data-testid="stImage"] img {
        filter: grayscale(100%) opacity(0.8);
        transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
        border-radius: 12px;
    }
    [data-testid="stImage"] img:hover {
        filter: grayscale(0%) opacity(1);
        transform: scale(1.03);
    }
    
    /* Анимация карточек-контейнеров Streamlit */
    [data-testid="stVerticalBlockBorderWrapper"] {
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        border-radius: 16px !important;
        background: #ffffff;
        border: 1px solid #f1f3f5 !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.06);
        border-color: #d8b4fe !important; /* Легкий фиолетовый оттенок рамки при наведении */
    }

    /* Кастомные анимированные кнопки контактов */
    .contact-container {
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
        margin-top: 15px;
        margin-bottom: 25px;
    }
    .contact-btn {
        text-decoration: none;
        color: #495057;
        background: #f8f9fa;
        padding: 8px 18px;
        border-radius: 30px;
        font-size: 0.95rem;
        font-weight: 600;
        border: 1px solid #e9ecef;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .contact-btn:hover {
        background: #212529;
        color: #ffffff !important;
        transform: translateY(-3px);
        box-shadow: 0 8px 15px rgba(33, 37, 41, 0.2);
    }
    
    /* Особая кнопка для Instagram */
    .insta-btn:hover {
        background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
        color: #ffffff !important;
        border: none;
        box-shadow: 0 8px 15px rgba(220, 39, 67, 0.3);
    }

    /* Настройка вкладок */
    .stTabs [data-baseweb="tab-list"] {
        gap: 30px;
        justify-content: center;
        border-bottom: 2px solid #f1f3f5;
    }
    .stTabs [data-baseweb="tab"] {
        padding-top: 15px;
        padding-bottom: 15px;
        font-weight: 700;
        letter-spacing: 1px;
        transition: color 0.3s;
    }
    .stTabs [aria-selected="true"] {
        color: #212529 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- ШАПКА ПРОФИЛЯ ---
col_logo, col_info = st.columns([1, 6])

with col_logo:
    # Векторный аватар 
    st.image("https://api.dicebear.com/7.x/bottts/svg?seed=Assem&backgroundColor=transparent", width=120)

with col_info:
    st.title("ASSEM ABDRASHIT")
    st.markdown("<span style='font-size: 1.2rem; color: #868e96; font-weight: 600; letter-spacing: 2px;'>WEB & AI DEVELOPER</span>", unsafe_allow_html=True)
    
    # Кастомные анимированные кнопки контактов
    st.markdown("""
    <div class="contact-container">
        <a href="tel:+77066638314" class="contact-btn">📞 +7 (706) 663-83-14</a>
        <a href="mailto:top.tyanach@gmail.com" class="contact-btn">✉️ top.tyanach@gmail.com</a>
        <a href="https://instagram.com/bleedshade" target="_blank" class="contact-btn insta-btn">📸 @bleedshade</a>
        <a href="https://bleedshade.streamlit.app" target="_blank" class="contact-btn">🔗 bleedshade.app</a>
    </div>
    """, unsafe_allow_html=True)

st.write("") # Небольшой отступ вместо жесткой линии

# --- ВЕРХНЕЕ МЕНЮ (ВКЛАДКИ) ---
tab_profile, tab_exp, tab_edu, tab_skills = st.tabs([
    "👤 PROFILE", 
    "💼 EXPERIENCE", 
    "🎓 EDUCATION", 
    "🛠 TECH STACK"
])

# --- РАЗДЕЛ 1: ПРОФИЛЬ ---
with tab_profile:
    col1, col2 = st.columns([1.8, 1])
    
    with col1:
        st.header("Blending Math, Code, and AI")
        st.write("""
        I am an IT and Applied Math student passionate about **Artificial Intelligence** and advanced technologies. I blend technical skills with creative problem-solving 
        through academic research and practical software development.
        
        My goal is to build scalable, clean, and efficient systems. I am actively 
        seeking tech internships, freelance projects, and entry-level roles where 
        I can apply my analytical mindset to solve real-world problems.
        """)
        
    with col2:
        st.image("https://illustrations.popsy.co/amber/freelancer.svg", use_container_width=True)

# --- РАЗДЕЛ 2: ОПЫТ РАБОТЫ ---
with tab_exp:
    st.write("") # Отступ
    with st.container(border=True):
        st.subheader("PROFI.RU")
        st.markdown("**Freelance Software Engineer** | *June 2023 - Present*")
        st.write("""
        * Comprehensive expertise in the operational mechanics of global internet entities, including high-traffic search engines, secure fintech payment gateways, and large-scale social networking platforms.
        * Proven ability to manage and optimize informational, educational (EdTech), and entertainment platforms, ensuring high user retention and seamless content delivery.
        """)
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.subheader("TOO MAGIC ENGINEERING")
            st.markdown("**Python Developer** | *June 2024 - July 2024*")
            st.write("""
            * Developed specialized software for estimate automation in Python.
            * Streamlined and optimized routine calculation tasks into maintainable backend code.
            """)
            
        with st.container(border=True):
            st.subheader("TURANDOT")
            st.markdown("**Software Developer** | *July 2023 - Jan 2024*")
            st.write("""
            * Designed and implemented robust software solutions utilizing C++ with Qt5.
            * Integrated custom-built software into existing CRM ecosystems.
            """)
            
    with col2:
        with st.container(border=True):
            st.subheader("TOO ZHIBER.KZ")
            st.markdown("**Backend Developer** | *Feb 2024 - Mar 2024*")
            st.write("""
            * Ensured high availability and seamless server-side functionality.
            * Maintained robust backend architectures and handled server-side logic, optimizing DB queries.
            """)

        with st.container(border=True):
            st.subheader("Lief & Co.")
            st.markdown("**Flutter Developer** | *June 2023 - Jan 2024*")
            st.write("""
            * Built cross-platform mobile apps from scratch using Flutter. 
            * Managed front-end architecture and complex API integrations.
            """)

# --- РАЗДЕЛ 3: ОБРАЗОВАНИЕ ---
with tab_edu:
    st.write("")
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        with st.container(border=True):
            st.subheader("Auezov South Kazakhstan University")
            st.markdown("**Bachelor's Degree in IT and Applied Mathematics**")
            st.caption("2024 - Present")
            st.write("Focusing on software engineering, AI research, and applied math.")
            
        with st.container(border=True):
            st.subheader("Miras College")
            st.markdown("**Vocational/Technical Degree: Software Technician**")
            st.caption("2020 - 2024")
            st.write("Core fundamentals of computing and software development.")

    with col2:
        with st.container(border=True):
            st.subheader("Languages")
            st.write("**English** (C1 Advanced)")
            st.progress(0.85)
            
            st.write("**Russian** (C2 Proficient)")
            st.progress(0.95)
            
            st.write("**Kazakh** (Native)")
            st.progress(1.0)
            
        st.image("https://illustrations.popsy.co/amber/student-going-to-school.svg", width=200)

# --- РАЗДЕЛ 4: СТЕК ТЕХНОЛОГИЙ ---
with tab_skills:
    st.write("")
    st.write("Core technologies and tools utilized in development:")
    st.write("")
    
    # Логотипы в карточках с анимацией
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        with st.container(border=True):
            st.image("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg", width=50)
            st.markdown("**Python**")
    with c2:
        with st.container(border=True):
            st.image("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cplusplus/cplusplus-original.svg", width=50)
            st.markdown("**C++**")
    with c3:
        with st.container(border=True):
            st.image("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg", width=50)
            st.markdown("**JavaScript**")
    with c4:
        with st.container(border=True):
            st.image("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flutter/flutter-original.svg", width=50)
            st.markdown("**Flutter**")
        
    c5, c6, c7, c8 = st.columns(4)
    with c5:
        with st.container(border=True):
            st.image("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/nodejs/nodejs-original.svg", width=50)
            st.markdown("**Node.js**")
    with c6:
        with st.container(border=True):
            st.image("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-original.svg", width=50)
            st.markdown("**SQL / MySQL**")
    with c7:
        with st.container(border=True):
            st.image("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linux/linux-original.svg", width=50)
            st.markdown("**Linux**")
    with c8:
        with st.container(border=True):
            st.image("https://illustrations.popsy.co/amber/robot.svg", width=50)
            st.markdown("**AI Dev**")
