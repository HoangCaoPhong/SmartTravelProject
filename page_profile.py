
import streamlit as st

def render_profile_page():
    st.header("Hồ sơ của bạn")

    tab1, tab2 = st.tabs(["Bộ sưu tập", "Tài khoản"])

    with tab1:
        st.subheader("Bộ sưu tập của bạn")
        st.write("// Hiển thị và quản lý collections và saved_places từ SQLite")

    with tab2:
        st.subheader("Thông tin tài khoản")
        username = st.session_state.get('username', 'Người dùng')
        st.write(f"Tên người dùng: **{username}**")
