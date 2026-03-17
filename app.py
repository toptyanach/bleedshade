import streamlit as st

st.set_page_config(page_title="Resume | Assem Abdrashit", page_icon="✨", layout="wide")

# CSS для светлого, чистого и "вайбового" оформления
st.markdown("""
<style>
    /* Глобальные настройки цвета для светлой темы */
    .stApp {
        background-color: #F8F9FA;
        color: #212529;
    }
    
    /* Скрытие дефолтных меню Streamlit */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Базовые стили */
    h1, h2, h3, h4, p, span, li {
        font-family: 'Inter', 'Helvetica Neue', sans-serif;
    }
    
    /* Левая колонка (сайдбар внутри страницы) */
    .left-panel {
        background-color: #FFFFFF;
        padding: 2.5rem 2rem;
        border-radius: 24px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.03);
        height: 100%;
        border: 1px solid #F1F3F5;
    }
    
    .profile-img-container {
        display: flex;
        justify-content: center;
        margin-bottom: 2rem;
    }
    
    .profile-img {
        width: 240px;
        height: 240px;
        border-radius: 50%;
        object-fit: cover;
        border: 5px solid #FFFFFF;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    .profile-img:hover {
        transform: scale(1.02);
    }
    
    .contact-item {
        font-size: 0.95rem;
        color: #495057;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 10px;
        font-weight: 500;
    }
    
    .section-header {
        font-size: 1.1rem;
        font-weight: 800;
        color: #212529;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-top: 2.5rem;
        margin-bottom: 1.2rem;
        border-bottom: 2px solid #F1F3F5;
        padding-bottom: 0.5rem;
    }
    
    .sub-text {
        font-size: 0.85rem;
        color: #868E96;
        margin-bottom: 0.2rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-weight: 600;
    }
    
    .bold-text {
        font-weight: 700;
        color: #343A40;
        font-size: 1.05rem;
    }
    
    .pill {
        display: inline-block;
        background-color: #F8F9FA;
        color: #495057;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 4px 4px 4px 0;
        border: 1px solid #E9ECEF;
        transition: all 0.2s ease;
    }
    .pill:hover {
        background-color: #212529;
        color: #FFFFFF;
        border-color: #212529;
    }
    
    /* Правая колонка (Основной контент) */
    .right-panel {
        padding: 1rem 1rem 1rem 3rem;
    }
    
    .name-title {
        font-size: 4.5rem;
        font-weight: 900;
        color: #212529;
        line-height: 1;
        letter-spacing: -2px;
        margin-bottom: 0.5rem;
    }
    
    .role-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #868E96;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-top: 0;
        margin-bottom: 3rem;
    }
    
    .profile-text {
        font-size: 1.15rem;
        line-height: 1.7;
        color: #495057;
        background-color: #FFFFFF;
        padding: 2rem;
        border-radius: 20px;
        border-left: 4px solid #212529;
        box-shadow: 0 10px 40px rgba(0,0,0,0.03);
        margin-bottom: 3.5rem;
        font-weight: 500;
    }
    
    .exp-card {
        background-color: #FFFFFF;
        padding: 2.5rem;
        border-radius: 24px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.02);
        margin-bottom: 2rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 1px solid #F8F9FA;
    }
    .exp-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.06);
    }
    
    .exp-company {
        font-size: 1.5rem;
        font-weight: 900;
        color: #212529;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
    }
    
    .exp-role-date {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1.5rem;
        border-bottom: 1px solid #F1F3F5;
        padding-bottom: 1rem;
    }
    
    .exp-role {
        font-size: 1.15rem;
        color: #495057;
        font-weight: 700;
    }
    
    .exp-date {
        font-size: 0.85rem;
        color: #ADB5BD;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    
    .exp-bullets {
        margin: 0;
        padding-left: 1.2rem;
        color: #495057;
        line-height: 1.7;
        font-size: 1.05rem;
    }
    .exp-bullets li {
        margin-bottom: 0.8rem;
    }
    
    /* Адаптивность для мобилок */
    @media (max-width: 768px) {
        .right-panel { padding: 1rem 0; }
        .exp-role-date {
            flex-direction: column;
            align-items: flex-start;
            gap: 5px;
        }
        .name-title { font-size: 3rem; }
    }
</style>
""", unsafe_allow_html=True)

# 🔗 ТВОЯ ФОТКА (Вставь сюда прямую ссылку на свое фото)
# Сейчас тут стоит эстетичный черно-белый плейсхолдер с Unsplash
PROFILE_PIC_URL = "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=600&q=80"

# Разделяем экран на 2 колонки: Сайдбар (1 часть) и Основной контент (2.2 части)
col1, col2 = st.columns([1, 2.2], gap="large")

with col1:
    st.markdown(f"""
    <div class="left-panel">
        <div class="profile-img-container">
            <img src="{PROFILE_PIC_URL}" class="profile-img" alt="Assem Abdrashit">
        </div>
        
        <div style="margin-top: 1rem;">
            <div class="contact-item">📞 +7 775 391 30 66</div>
            <div class="contact-item">✉️ top.tyanach@gmail.com</div>
            <div class="contact-item">🔗 bleedshade.streamlit.app</div>
        </div>
        
        <div class="section-header">Education</div>
        <div style="margin-bottom: 1.5rem;">
            <div class="bold-text">Bachelor degree</div>
            <div style="color: #495057; margin-top: 4px; margin-bottom: 4px;">Auezov South Kazakhstan<br>University (SKU)</div>
            <div class="sub-text">2024 - present</div>
        </div>
        <div>
            <div class="bold-text">Vocational/Technical Degree</div>
            <div style="color: #495057; margin-top: 4px; margin-bottom: 4px;">Miras College</div>
            <div class="sub-text">2020 - 2024</div>
        </div>
        
        <div class="section-header">Expertise</div>
        <div>
            <span class="pill">Applied Mathematics</span>
            <span class="pill">Information Technology</span>
            <span class="pill">AI Research</span>
            <span class="pill">Analytical Skills</span>
            <span class="pill">Community Management</span>
            <span class="pill">Team Collaboration</span>
            <span class="pill">Project Organization</span>
        </div>
        
        <div class="section-header">Language</div>
        <div>
            <span class="pill">English</span>
            <span class="pill">Russian</span>
            <span class="pill">Kazakh</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="right-panel">
        <h1 class="name-title">ASSEM<br>ABDRASHIT</h1>
        <div class="role-title">WEB DEVELOPER</div>
        
        <div class="section-header" style="margin-top: 0; border: none;">Profile</div>
        <div class="profile-text">
            IT and Applied Math student passionate about AI and advanced tech. 
            Blending technical skills with creative problem-solving through 
            academic research and community management. Open to tech internships 
            and entry-level roles.
        </div>
        
        <div class="section-header" style="border: none;">Work Experience</div>
        
        <!-- PROFI.RU -->
        <div class="exp-card">
            <div class="exp-company">PROFI.RU</div>
            <div class="exp-role-date">
                <span class="exp-role">Freelance Software Engineer</span>
                <span class="exp-date">June 2023 - Present</span>
            </div>
            <ul class="exp-bullets">
                <li>Comprehensive expertise in the operational mechanics of global internet entities, including high-traffic search engines, secure fintech payment gateways, and large-scale social networking platforms.</li>
                <li>Proven ability to manage and optimize informational, educational (EdTech), and entertainment platforms, ensuring high user retention and seamless content delivery across various digital mediums.</li>
            </ul>
        </div>
        
        <!-- ZHIBER.KZ -->
        <div class="exp-card">
            <div class="exp-company">TOO ZHIBER.KZ</div>
            <div class="exp-role-date">
                <span class="exp-role">Backend-developer</span>
                <span class="exp-date">February 2024 - March 2024</span>
            </div>
            <ul class="exp-bullets">
                <li>Ensuring high availability and seamless server-side functionality by monitoring server health, optimizing database queries, and managing server configurations.</li>
                <li>Proficient in maintaining robust backend architectures, handling server-side logic, and ensuring data integrity across complex web environments.</li>
            </ul>
        </div>
        
        <!-- TURANDOT -->
        <div class="exp-card">
            <div class="exp-company">TURANDOT</div>
            <div class="exp-role-date">
                <span class="exp-role">Software Developer</span>
                <span class="exp-date">July 2023 - January 2024</span>
            </div>
            <ul class="exp-bullets">
                <li>Designing and implementing robust software solutions utilizing C++ with the Qt5 framework, alongside JavaScript and Node.js for versatile, high-performance applications.</li>
                <li>Successfully architecting and executing the seamless integration of custom-built software into existing CRM ecosystems, ensuring data synchronization and workflow optimization.</li>
            </ul>
        </div>
        
    </div>
    """, unsafe_allow_html=True)
