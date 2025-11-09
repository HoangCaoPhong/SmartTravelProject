import streamlit as st
from streamlit_option_menu import option_menu
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.utils.auth import render_login_page
from src.pages.page_dashboard import render_dashboard
from src.pages.page_discover import render_discover_page
from src.pages.page_home import render_home_page, render_about_page, render_features_page
from src.pages.page_recognize import render_recognition_page
from src.pages.page_profile import render_profile_page
from src.utils.db_utils import init_db
from src.utils.constants import PAGE_TITLE, PAGE_LAYOUT, PRIMARY_COLOR, BACKGROUND_COLOR

# --- Cấu hình Trang & Theme ---
st.set_page_config(
    page_title=PAGE_TITLE,
    layout=PAGE_LAYOUT,
)

# Apply custom CSS
css_path = os.path.join(os.path.dirname(__file__), "static", "css", "style.css")
with open(css_path, encoding='utf-8') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Additional CSS to force white background and remove black bars
st.markdown("""
    <style>
        /* Force white background everywhere */
        .stApp, .main, body, html {
            background-color: #FFFFFF !important;
        }
        
        /* Remove black decoration bars */
        [data-testid="stDecoration"] {
            display: none !important;
        }
        
        /* Force white for app view container */
        [data-testid="stAppViewContainer"] {
            background-color: #FFFFFF !important;
        }
        
        /* Target the parent container of option-menu to remove black bars */
        .element-container:has(div.menu),
        div[data-testid="column"]:has(div.menu),
        div[data-testid="stVerticalBlock"]:has(div.menu) {
            background-color: #FFFFFF !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        
        /* Force streamlit-option-menu parent background white */
        .element-container {
            background-color: #FFFFFF !important;
        }
        
        /* Override any remaining black backgrounds */
        * {
            scrollbar-color: #888 #f1f1f1;
        }
        
        /* Ensure no dark theme classes apply */
        [data-theme="dark"] {
            display: none !important;
        }
        
        /* Force menu wrapper background */
        .menu, .menu * {
            background-color: transparent !important;
        }
        
        .menu .container-xxl {
            background-color: #E8F1FA !important;
        }
        
        /* Navigation full width fix */
        .main .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# Ensure database is initialized on startup
init_db()

# --- Khởi tạo Session State ---
# Note: Streamlit session state is cleared on page refresh
# This is normal behavior - users need to re-login after refresh
# To persist login, we would need a proper backend with JWT tokens

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = ""
if 'user_id' not in st.session_state:
    st.session_state['user_id'] = None

# --- A. LOGIC ĐIỀU HƯỚNG (PHẦN CHÍNH) ---

if not st.session_state['logged_in']:
    # ---- 1. GIAO DIỆN CHƯA ĐĂNG NHẬP (NAV NGANG CÔNG KHAI) ----
    selected = option_menu(
        menu_title=None,
        options=["Home", "About", "Tính năng", "Đăng nhập"],
        icons=["house", "info-circle", "star", "box-arrow-in-right"],
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#E8F1FA", "width": "100%"},
            "nav-link": {"color": "#000000", "font-weight": "500"},
            "nav-link-selected": {"background-color": PRIMARY_COLOR, "color": "#FFFFFF"},
        }
    )
    
    if selected == "Home":
        render_home_page()
    elif selected == "About":
        render_about_page()
    elif selected == "Tính năng":
        render_features_page()
    elif selected == "Đăng nhập":
        render_login_page()

else:
    # ---- 2. GIAO DIỆN ĐÃ ĐĂNG NHẬP (NAV NGANG THÀNH VIÊN) ----
    selected = option_menu(
        menu_title=PAGE_TITLE,
        options=["Dashboard", "Khám phá", "Nhận diện", "Hồ sơ", "Đăng xuất"],
        icons=["speedometer2", "search", "image", "person-circle", "box-arrow-left"],
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#E8F1FA", "width": "100%"},
            "nav-link": {"color": "#000000", "font-weight": "500"},
            "nav-link-selected": {"background-color": PRIMARY_COLOR, "color": "#FFFFFF"},
            "menu-title": {"color": "#000000", "font-weight": "600"},
        }
    )

    if selected == "Dashboard":
        render_dashboard(st.session_state.get('username', ''))
    elif selected == "Khám phá":
        render_discover_page()
    elif selected == "Nhận diện":
        render_recognition_page()
    elif selected == "Hồ sơ":
        render_profile_page()
    elif selected == "Đăng xuất":
        st.session_state.clear()
        st.session_state['logged_in'] = False
        st.rerun()
