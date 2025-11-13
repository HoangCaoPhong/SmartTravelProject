"""Trang Chức năng với 4 nút lựa chọn"""
import streamlit as st
from datetime import time
import db_utils
from utils import time_to_minutes, minutes_to_str


def page_chuc_nang():
    """Hiển thị nội dung trang chức năng với 4 nút lựa chọn."""
    st.markdown("<div class='section-title'>Chức năng</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-subtitle'>Chọn chức năng bạn muốn sử dụng.</div>",
        unsafe_allow_html=True,
    )
    
    # Initialize selected function in session state
    if 'selected_function' not in st.session_state:
        st.session_state['selected_function'] = "Tìm kiếm nhanh"
    
    # ===== BỐ CỤC 4 NÚT CHỌN CHỨC NĂNG =====
    st.markdown("### Chọn chức năng")
    
    # Hàng 1: Tìm kiếm nhanh (full width)
    if st.button("🔍 Tìm kiếm nhanh", use_container_width=True, key="btn_tim_kiem_nhanh"):
        st.session_state['selected_function'] = "Tìm kiếm nhanh"
        st.rerun()
    
    # Hàng 2: 3 chức năng con
    col_btn2, col_btn3, col_btn4 = st.columns(3)
    with col_btn2:
        if st.button("🧩 Tạo danh sách gợi ý", use_container_width=True, key="btn_goi_y"):
            st.session_state['selected_function'] = "Tạo danh sách gợi ý"
            st.rerun()
    with col_btn3:
        if st.button("🚗 Tìm đường đi", use_container_width=True, key="btn_tim_duong"):
            st.session_state['selected_function'] = "Tìm đường đi"
            st.rerun()
    with col_btn4:
        if st.button("📷 Nhận diện vị trí ảnh", use_container_width=True, key="btn_nhan_dien"):
            st.session_state['selected_function'] = "Nhận diện vị trí ảnh"
            st.rerun()
    
    st.markdown("---")
    
    # ===== HIỂN THỊ NỘI DUNG THEO LỰA CHỌN =====
    selected = st.session_state['selected_function']
    st.info(f"✨ Đang hiển thị: **{selected}**")
    
    # 1. TÌM KIẾM NHANH
    if selected == "Tìm kiếm nhanh":
        render_tim_kiem_nhanh()
    
    # 2. TẠO DANH SÁCH GỢI Ý
    elif selected == "Tạo danh sách gợi ý":
        render_tao_danh_sach_goi_y()
    
    # 3. TÌM ĐƯỜNG ĐI
    elif selected == "Tìm đường đi":
        render_tim_duong_di()
    
    # 4. NHẬN DIỆN VỊ TRÍ ẢNH
    elif selected == "Nhận diện vị trí ảnh":
        render_nhan_dien_anh()


def render_tim_kiem_nhanh():
    """Render phần Tìm kiếm nhanh - Tạo lịch trình 1 ngày"""
    st.markdown("### 🔍 Tìm kiếm nhanh")
    st.markdown(
        "<p class='feature-muted'>Tạo lịch trình 1 ngày nhanh chóng với các điểm đến yêu thích.</p>",
        unsafe_allow_html=True,
    )
    
    col_form, col_result = st.columns([1.1, 1], gap="large")
    
    with col_form:
        st.markdown("#### 📝 Nhập thông tin chuyến đi")
        with st.form("quick_search_form"):
            start_location = st.text_input("Điểm xuất phát", value="Quận 1, TP.HCM")
            destinations_text = st.text_area(
                "Danh sách điểm muốn đến (mỗi dòng một địa điểm)",
                value="Nhà thờ Đức Bà\nPhố đi bộ Nguyễn Huệ\nLandmark 81",
                height=120,
            )
            food_text = st.text_area(
                "Danh sách món ăn muốn thử (mỗi dòng một món)",
                value="Phở bò\nBánh mì thịt\nTrà sữa",
                height=100,
            )
            c1, c2 = st.columns(2)
            with c1:
                start_time = st.time_input("Giờ bắt đầu", value=time(8, 0))
            with c2:
                end_time = st.time_input("Giờ kết thúc", value=time(20, 0))
            budget = st.number_input(
                "Ngân sách tối đa (VND)",
                min_value=0,
                value=800000,
                step=50000,
            )
            submitted = st.form_submit_button("🔍 Tạo lịch trình")

        if not submitted:
            st.caption("⏳ Nhập xong và bấm **Tạo lịch trình** để xem kết quả.")

    with col_result:
        st.markdown("#### 📆 Kết quả lịch trình")
        if not submitted:
            st.info("Kết quả sẽ hiển thị ở đây sau khi bạn bấm nút.")
        else:
            dest_lines = [line.strip() for line in destinations_text.splitlines() if line.strip()]
            food_lines = [line.strip() for line in food_text.splitlines() if line.strip()]

            if not dest_lines:
                st.error("Vui lòng nhập ít nhất 1 điểm đến.")
            else:
                start_min = time_to_minutes(start_time)
                end_min = time_to_minutes(end_time)
                if end_min <= start_min:
                    st.warning("Giờ kết thúc phải lớn hơn giờ bắt đầu. Dùng mặc định 08:00 – 20:00.")
                    start_min = 8 * 60
                    end_min = 20 * 60

                total_minutes = end_min - start_min
                block = max(total_minutes // len(dest_lines), 30)
                current = start_min

                st.write(f"**Điểm xuất phát:** {start_location}")
                st.write(f"**Thời gian:** {minutes_to_str(start_min)} – {minutes_to_str(end_min)}")
                st.write(f"**Ngân sách:** {budget:,} VND")
                st.markdown("---")

                schedule_data = {
                    "destinations": dest_lines,
                    "start_time": minutes_to_str(start_min),
                    "end_time": minutes_to_str(end_min),
                    "budget": budget,
                    "timeline": [],
                }

                for i, place in enumerate(dest_lines, start=1):
                    arrive = current
                    depart = min(current + block, end_min)
                    current = depart
                    schedule_data["timeline"].append({
                        "place": place,
                        "arrive": minutes_to_str(arrive),
                        "depart": minutes_to_str(depart),
                    })
                    with st.expander(
                        f"📍 {i}. {place} ({minutes_to_str(arrive)} – {minutes_to_str(depart)})"
                    ):
                        st.write(f"**Thời gian:** {minutes_to_str(arrive)} – {minutes_to_str(depart)}")
                        st.write("**Hoạt động:** Tham quan, chụp ảnh, nghỉ ngơi.")
                        st.write(f"**Chi phí gợi ý:** {budget // len(dest_lines):,} VND")

                if food_lines:
                    st.markdown("---")
                    st.write("**🍜 Món ăn gợi ý**")
                    for food in food_lines:
                        st.write(f"- {food}")

                st.session_state["latest_schedule"] = schedule_data

                # Nút lưu (nếu đã đăng nhập)
                if st.session_state.get("current_user"):
                    st.markdown("---")
                    col_save, col_space = st.columns([1, 2])
                    with col_save:
                        if st.button("💾 Lưu lịch trình"):
                            user_id = st.session_state.get("user_id")
                            if user_id:
                                success = db_utils.add_schedule(
                                    user_id,
                                    ', '.join(dest_lines),
                                    budget,
                                    minutes_to_str(start_min),
                                    minutes_to_str(end_min),
                                    schedule_data,
                                )
                                if success:
                                    st.success("✅ Lịch trình đã được lưu!")
                                else:
                                    st.error("❌ Có lỗi khi lưu lịch trình.")
                else:
                    st.info("💡 Đăng nhập để lưu lịch trình vào hồ sơ.")


def render_tao_danh_sach_goi_y():
    """Render phần Tạo danh sách gợi ý"""
    st.markdown("### 🧩 Tạo danh sách gợi ý")
    st.markdown(
        "<p class='feature-muted'>Nhập sở thích, hệ thống sẽ gợi ý danh sách địa điểm phù hợp.</p>",
        unsafe_allow_html=True,
    )
    col_left, col_right = st.columns([1.2, 1])
    with col_left:
        interests = st.text_area(
            "Sở thích / loại địa điểm (ví dụ: bảo tàng, quán cà phê, biển...)",
            height=100,
        )
        budget_suggest = st.number_input(
            "Ngân sách dự kiến (VND)",
            min_value=0,
            value=500000,
            step=50000,
        )
        city = st.text_input("Thành phố / khu vực", value="TP.HCM")
        if st.button("Tạo danh sách gợi ý"):
            st.success("Đây là nơi hiển thị danh sách gợi ý địa điểm.")
    with col_right:
        st.markdown("#### 💡 Gợi ý")
        st.write("- Ưu tiên địa điểm gần nhau")
        st.write("- Cân đối tham quan, ăn uống, thư giãn")
        st.write("- Kết hợp điểm 'must-try' trong khu vực")


def render_tim_duong_di():
    """Render phần Tìm đường đi"""
    st.markdown("### 🚗 Tìm đường đi")
    st.markdown(
        "<p class='feature-muted'>Tìm đường đi tối ưu giữa các địa điểm.</p>",
        unsafe_allow_html=True,
    )
    with st.form("route_form"):
        start_point = st.text_input("Điểm bắt đầu", value="Quận 1")
        end_point = st.text_input("Điểm kết thúc", value="Nhà thờ Đức Bà")
        col1, col2 = st.columns(2)
        with col1:
            mode = st.selectbox(
                "Phương tiện",
                ["Xe máy", "Ô tô", "Đi bộ", "Phương tiện công cộng"],
            )
        with col2:
            max_time = st.number_input(
                "Thời gian tối đa (phút)",
                min_value=10,
                value=45,
                step=5,
            )
        c1, c2, c3 = st.columns([2, 1, 2])
        with c2:
            find_route = st.form_submit_button("Tìm đường!")
    
    if find_route:
        st.markdown("---")
        st.markdown("#### 📍 Kết quả")
        st.write(f"- **Từ:** {start_point}")
        st.write(f"- **Đến:** {end_point}")
        st.write(f"- **Phương tiện:** {mode}")
        st.write(f"- **Thời gian ước tính:** ~{max_time} phút")
        st.info("💡 Phiên bản đầy đủ có thể tích hợp API bản đồ (Google Maps, OpenStreetMap).")


def render_nhan_dien_anh():
    """Render phần Nhận diện vị trí ảnh"""
    st.markdown("### 📷 Nhận diện vị trí ảnh")
    st.markdown(
        "<p class='feature-muted'>Tải lên ảnh địa điểm, hệ thống sẽ nhận diện loại địa điểm.</p>",
        unsafe_allow_html=True,
    )
    img = st.file_uploader("Tải ảnh địa điểm (JPG/PNG)", type=["jpg", "jpeg", "png"])
    if img is not None:
        st.image(img, use_container_width=True)
        st.success("💡 Hệ thống có thể trả về nhãn: 'biển', 'núi', 'cafe', 'trung tâm thương mại'...")
    else:
        st.caption("📷 Chưa có ảnh nào được chọn.")
