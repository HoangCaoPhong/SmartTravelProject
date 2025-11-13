"""Trang Giới thiệu"""
import streamlit as st


def page_gioi_thieu():
    """Hiển thị nội dung trang giới thiệu."""
    st.markdown("<div class='section-title'>Giới thiệu đề tài</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-subtitle'>Tổng quan ngắn gọn về hệ thống du lịch thông minh tối ưu hóa lịch trình trong 1 ngày.</div>",
        unsafe_allow_html=True,
    )
    st.write("Thông tin các thành viên")
