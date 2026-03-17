import streamlit as st

# Настройки страницы
st.set_page_config(
    page_title="Resume | Assem Abdrashit",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- БОКОВОЕ МЕНЮ (НАВИГАЦИЯ) ---
with st.sidebar:
    # Векторный аватар (стильный робот/ai-разработчик)
    st.image("https://api.dicebear.com/7.x/bottts/svg?seed=Assem&backgroundColor=transparent", width=120)
    st.title("Assem Abdrashit")
    st.caption("WEB & AI DEVELOPER")
    
    st.divider()
    
    # КНОПКИ РАЗДЕЛОВ (Нативная навигация Streamlit)
    selected_section = st.radio(
        "Навигация",
        [
            "👤 Profile & About", 
            "💼 Work Experience", 
            "🎓 Education", 
            "🛠 Tech Stack"
        ],
        label_visibility="collapsed"
    )
    
    st.divider()
    
    # Контакты всегда на виду в боковой панели
    st.subheader("Contacts")
    st.write("📞 +7 (706) 663-83-14")
    st.write("✉️ top.tyanach@gmail.com")
    st.write("🔗 bleedshade.streamlit.app")

# --- ГЛАВНЫЙ ЭКРАН (МЕНЯЕТСЯ ОТ КНОПОК) ---

if selected_section == "👤 Profile & About":
    # Раздел 1: Профиль
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.title("Hello, I'm Assem 👋")
        st.subheader("Blending Math, Code, and AI.")
        st.write("")
        st.write("""
        I am an IT and Applied Math student passionate about Artificial Intelligence 
        and advanced technologies. I blend technical skills with creative problem-solving 
        through academic research and practical development.
        """)
        st.info("💡 Open to tech internships, freelance projects, and entry-level roles.", icon="🚀")
        
    with col2:
        # Векторная иллюстрация программиста
        st.image("https://illustrations.popsy.co/amber/freelancer.svg", use_container_width=True)


elif selected_section == "💼 Work Experience":
    # Раздел 2: Опыт работы (Карточки)
    st.title("Work Experience")
    
    with st.container(border=True):
        st.subheader("PROFI.RU")
        st.markdown("**Freelance Software Engineer** | *June 2023 - Present*")
        st.write("""
        * Comprehensive expertise in the operational mechanics of global internet entities, including high-traffic search engines, secure fintech payment gateways, and large-scale social networking platforms.
        * Proven ability to manage and optimize informational, educational (EdTech), and entertainment platforms, ensuring high user retention and seamless content delivery.
        """)
    
    with st.container(border=True):
        st.subheader("TOO MAGIC ENGINEERING")
        st.markdown("**Python Developer** | *June 2024 - July 2024*")
        st.write("""
        * Developed specialized software for estimate automation in Python.
        * Streamlined and optimized routine calculation tasks into maintainable backend code.
        """)

    with st.container(border=True):
        st.subheader("TOO ZHIBER.KZ")
        st.markdown("**Backend Developer** | *February 2024 - March 2024*")
        st.write("""
        * Ensured high availability and seamless server-side functionality by monitoring server health and optimizing database queries.
        * Maintained robust backend architectures and handled server-side logic.
        """)

    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.subheader("Lief & Co.")
            st.markdown("**Flutter Developer**")
            st.caption("June 2023 - Jan 2024")
            st.write("Built cross-platform mobile apps from scratch using Flutter. Managed front-end architecture and API integrations.")
    with col2:
        with st.container(border=True):
            st.subheader("TURANDOT")
            st.markdown("**Software Developer**")
            st.caption("July 2023 - Jan 2024")
            st.write("Designed and implemented robust software solutions utilizing C++ with Qt5, alongside JavaScript and Node.js.")


elif selected_section == "🎓 Education":
    # Раздел 3: Образование и Языки
    st.title("Education & Languages")
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.image("https://illustrations.popsy.co/amber/student-going-to-school.svg", width=250)
        
        with st.container(border=True):
            st.subheader("Bachelor Degree")
            st.markdown("**Auezov South Kazakhstan University (SKU)**")
            st.caption("2024 - present")
            st.write("IT and Applied Mathematics")
            
        with st.container(border=True):
            st.subheader("Vocational/Technical Degree")
            st.markdown("**Miras College**")
            st.caption("2020 - 2024")
            st.write("Software Technician")

    with col2:
        st.write("### Languages")
        st.write("")
        st.write("**English** (C1 Advanced)")
        st.progress(0.85)
        
        st.write("**Russian** (C2 Proficient)")
        st.progress(0.95)
        
        st.write("**Kazakh** (Native)")
        st.progress(1.0)


elif selected_section == "🛠 Tech Stack":
    # Раздел 4: Навыки с векторными (SVG) логотипами
    st.title("Expertise & Tech Stack")
    st.write("Technologies and tools I work with on a daily basis:")
    st.write("")
    
    # 1 ряд логотипов
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg", width=70)
        st.markdown("**Python**")
    with c2:
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cplusplus/cplusplus-original.svg", width=70)
        st.markdown("**C++**")
    with c3:
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg", width=70)
        st.markdown("**JavaScript**")
    with c4:
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flutter/flutter-original.svg", width=70)
        st.markdown("**Flutter**")
        
    st.write("")
    st.write("")
    
    # 2 ряд логотипов
    c5, c6, c7, c8 = st.columns(4)
    with c5:
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/nodejs/nodejs-original.svg", width=70)
        st.markdown("**Node.js**")
    with c6:
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-original.svg", width=70)
        st.markdown("**SQL / MySQL**")
    with c7:
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linux/linux-original.svg", width=70)
        st.markdown("**Linux**")
    with c8:
        # Векторная графика для AI
        st.image("https://illustrations.popsy.co/amber/robot.svg", width=70)
        st.markdown("**AI Research**")
