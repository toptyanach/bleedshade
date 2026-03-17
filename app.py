import streamlit as st

# Настройки страницы
st.set_page_config(
    page_title="Resume | Assem Abdrashit",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Разделяем экран на две колонки нативными средствами Streamlit
left_col, right_col = st.columns([1, 2.5], gap="large")

with left_col:
    # --- КОНТАКТЫ ---
    st.subheader("Контакты")
    st.info("""
    **Телефон:** +7 (706) 663-83-14  
    **Email:** top.tyanach@gmail.com  
    **Web:** bleedshade.streamlit.app
    """)
    
    st.divider()

    # --- ОБРАЗОВАНИЕ ---
    st.subheader("Education")
    
    st.markdown("**Bachelor degree**")
    st.markdown("*Auezov South Kazakhstan University (SKU)*")
    st.caption("2024 - present")
    
    st.write("") # Небольшой отступ
    
    st.markdown("**Vocational/Technical Degree**")
    st.markdown("*Miras College*")
    st.caption("2020 - 2024")
    
    st.divider()

    # --- НАВЫКИ ---
    st.subheader("Expertise & Skills")
    # Используем форматирование кода для имитации "пилюль"
    st.markdown("""
    `Python` `C++` `SQL` `JavaScript` `Flutter` 
    `Node.js` `Applied Mathematics` `AI Research` 
    `System Administration` `API`
    """)
    
    st.divider()

    # --- ЯЗЫКИ ---
    st.subheader("Languages")
    st.markdown("""
    - **English:** C1 (Advanced)
    - **Russian:** C2 (Proficient)
    - **Kazakh:** Native
    """)

with right_col:
    # --- ШАПКА ---
    st.title("ASSEM ABDRASHIT")
    st.subheader("WEB & AI DEVELOPER")
    
    st.divider()

    # --- ОБО МНЕ ---
    st.header("Profile")
    st.write("""
    IT and Applied Math student passionate about AI and advanced tech. 
    Blending technical skills with creative problem-solving through 
    academic research and community management. Open to tech internships 
    and entry-level roles.
    """)
    
    st.divider()

    # --- ОПЫТ РАБОТЫ ---
    st.header("Work Experience")

    # Место 1
    st.subheader("PROFI.RU")
    st.markdown("**Freelance Software Engineer** | *June 2023 - Present*")
    st.write("""
    * Comprehensive expertise in the operational mechanics of global internet entities, including high-traffic search engines, secure fintech payment gateways, and large-scale social networking platforms.
    * Proven ability to manage and optimize informational, educational (EdTech), and entertainment platforms, ensuring high user retention and seamless content delivery across various digital mediums.
    """)
    
    st.write("") # Отступ
    
    # Место 2
    st.subheader("TOO MAGIC ENGINEERING")
    st.markdown("**Python Developer** | *June 2024 - July 2024*")
    st.write("""
    * Developed specialized software for estimate automation in Python.
    * Streamlined and optimized routine calculation tasks into maintainable backend code.
    """)

    st.write("")
    
    # Место 3
    st.subheader("TOO ZHIBER.KZ")
    st.markdown("**Backend Developer** | *February 2024 - March 2024*")
    st.write("""
    * Ensuring high availability and seamless server-side functionality by monitoring server health, optimizing database queries, and managing server configurations.
    * Proficient in maintaining robust backend architectures, handling server-side logic, and ensuring data integrity across complex web environments.
    """)

    st.write("")
    
    # Место 4
    st.subheader("Lief & Co.")
    st.markdown("**Flutter Developer** | *June 2023 - January 2024*")
    st.write("""
    * Built cross-platform mobile applications from scratch using Flutter.
    * Managed front-end architecture and API integrations.
    """)

    st.write("")
    
    # Место 5
    st.subheader("TURANDOT")
    st.markdown("**Software Developer** | *July 2023 - January 2024*")
    st.write("""
    * Designing and implementing robust software solutions utilizing C++ with the Qt5 framework, alongside JavaScript and Node.js for versatile, high-performance applications.
    * Successfully architecting and executing the seamless integration of custom-built software into existing CRM ecosystems, ensuring data synchronization and workflow optimization.
    """)
