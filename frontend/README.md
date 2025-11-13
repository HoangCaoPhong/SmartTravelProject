# Smart 1-Day Trip Planner - Frontend

## 🎯 Mô tả

Frontend cho ứng dụng Smart Travel - hệ thống lập kế hoạch du lịch thông minh 1 ngày.

## ✨ Tính năng

- ✅ **Custom Navigation** - Sử dụng Streamlit buttons thay vì streamlit-option-menu
- ✅ **Modern UI** - Gradient background với card design hiện đại  
- ✅ **Tạo danh sách gợi ý** - Gợi ý địa điểm dựa trên sở thích
- ✅ **Tìm đường đi** - Tính toán route tối ưu
- ✅ **Nhận diện ảnh** - Nhận diện địa điểm từ ảnh (đang phát triển)
- ✅ **Lên lịch trình** - Tạo lịch trình du lịch 1 ngày
- ✅ **User Authentication** - Đăng ký/Đăng nhập với JSON database

## 🚀 Cách chạy

### 1. Di chuyển vào thư mục frontend
```powershell
cd frontend
```

### 2. Cài đặt dependencies (nếu chưa)
```powershell
pip install -r ../requirements.txt
```

### 3. Chạy ứng dụng
```powershell
python -m streamlit run app.py
```

### 4. Mở trình duyệt
```
http://localhost:8501
```

## 📁 Cấu trúc

```
frontend/
├── app.py              # Main application file
├── style.css           # Custom CSS styles
├── database.json       # JSON database (auto-created)
├── flowchart/          # Flowchart documentation
└── README.md           # This file
```

## 🎨 Thay đổi gần đây

### Navigation System
- ❌ Removed: `streamlit-option-menu` dependency
- ✅ Added: Custom button-based navigation
- ✅ Improved: Hover effects và active states

### Button Styling
- ✅ Fixed: Buttons với nền đen + chữ đen
- ✅ Updated: Tất cả buttons giờ có chữ trắng rõ ràng
- ✅ Enhanced: Hover effects với gradient transitions

## 🔧 Cấu hình

### Menu Options (Chưa đăng nhập)
- Trang chủ
- Giới thiệu  
- Chức năng
- Lên lịch trình
- Sign in / Sign up

### Menu Options (Đã đăng nhập)
- Trang chủ
- Giới thiệu
- Chức năng
- Lên lịch trình
- Hồ sơ

## 📝 Database Schema (JSON)

```json
{
  "users": {
    "email@example.com": "password"
  },
  "user_data": {
    "email@example.com": {
      "schedules": [...]
    }
  }
}
```

## 🎯 To-Do

- [ ] Tích hợp API nhận diện ảnh
- [ ] Thêm Google Maps integration
- [ ] Export lịch trình ra PDF
- [ ] Thêm tính năng chia sẻ lịch trình

## 👥 Credits

Smart Travel Team - 2025
