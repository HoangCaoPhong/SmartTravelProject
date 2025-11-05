import streamlit as st


def render_home_page():
    """Render home page with features overview."""
    st.title("Chào mừng đến với SmartTravelProject ✈️")

    st.write("Khám phá thế giới với SmartTravelProject - người bạn đồng hành thông minh cho mọi chuyến đi!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://via.placeholder.com/150/0000FF/FFFFFF?text=Search", caption="Tìm kiếm địa điểm")
        st.subheader("Tìm kiếm thông minh")
        st.write("Dễ dàng tìm kiếm hàng ngàn địa điểm du lịch, nhà hàng, khách sạn.")

    with col2:
        st.image("https://via.placeholder.com/150/FF0000/FFFFFF?text=AI+Detect", caption="Nhận diện địa điểm")
        st.subheader("Nhận diện AI")
        st.write("Tải ảnh lên và để AI của chúng tôi nhận diện địa điểm cho bạn.")

    with col3:
        st.image("https://via.placeholder.com/150/00FF00/FFFFFF?text=Plan+Trip", caption="Lên kế hoạch chuyến đi")
        st.subheader("Lên kế hoạch")
        st.write("Lưu lại những địa điểm yêu thích và tạo bộ sưu tập cho chuyến đi của bạn.")


def render_about_page():
    """Render about page."""
    st.header("Giới thiệu về SmartTravelProject")
    st.write("""
    SmartTravelProject là ứng dụng du lịch thông minh được phát triển để giúp bạn:
    
    - **Khám phá** những địa điểm mới tuyệt vời
    - **Nhận diện** các điểm đến từ ảnh
    - **Quản lý** các chuyến đi của bạn
    - **Lưu trữ** những địa điểm yêu thích
    
    Với công nghệ AI tiên tiến, chúng tôi mang đến trải nghiệm du lịch tốt nhất.
    """)


def render_features_page():
    """Render features page."""
    st.header("Các tính năng chính")
    
    st.subheader("🔍 Tìm kiếm thông minh")
    st.write("Tìm kiếm địa điểm với các bộ lọc nâng cao (giá, loại hình, v.v.)")
    
    st.subheader("📸 Nhận diện ảnh")
    st.write("Tải ảnh lên và nhận diện địa điểm tự động bằng AI")
    
    st.subheader("💾 Lưu bộ sưu tập")
    st.write("Tạo và quản lý các bộ sưu tập địa điểm yêu thích")
    
    st.subheader("🗺️ Chỉ đường")
    st.write("Xem bản đồ và nhận hướng dẫn chỉ đường tới địa điểm")
