# 📋 CHANGELOG - Frontend Refactoring

## Version 2.0 - November 13, 2025

### ✨ Major Changes

#### 1. 🗄️ Database Migration: JSON → SQLite
- ✅ Migrated from `database.json` to SQLite (`smarttravel_frontend.db`)
- ✅ Created proper schema với relationships
- ✅ Auto-migration từ JSON (nếu có)
- ✅ Tự động backup JSON file cũ

#### 2. 🎨 UI/UX Improvements  
- ✅ **Fixed Navigation Colors**: Đổi từ trắng → đen để thấy rõ trên nền trắng
- ✅ **Fixed Button Text**: Sửa lỗi `<p>` tags trong buttons
- ✅ **Custom Navigation**: Removed streamlit-option-menu, dùng custom buttons
- ✅ **Better Hover Effects**: Smooth transitions và color changes

#### 3. 📦 Project Structure Cleanup
- ✅ Tối giản hóa: Chỉ giữ `frontend/` folder
- ✅ Marked for removal: `src/`, `static/`, `SmartTravel.py` (files cũ không dùng)
- ✅ Updated `.gitignore` cho Python project

#### 4. 🔧 Code Improvements
- ✅ Modular database utilities (`db_utils.py`)
- ✅ Better error handling
- ✅ Session state management
- ✅ Removed deprecated dependencies

### 🗑️ Removed

- ❌ `streamlit-option-menu` package
- ❌ JSON database logic (migrated to SQLite)
- ❌ Legacy session state với dict

### ➕ Added

- ✅ `frontend/db_utils.py` - SQLite database utilities
- ✅ SQLite database với proper indexing
- ✅ Auto-migration tool
- ✅ Better CSS for navigation
- ✅ frontend/README.md

### 🔄 Modified

- 📝 `frontend/app.py` - Complete database refactor
- 🎨 `frontend/style.css` - Fixed button colors
- 📋 `requirements.txt` - Removed streamlit-option-menu
- 📖 `README.md` - Updated documentation

### 🐛 Bug Fixes

- ✅ Navigation text màu trắng trên nền trắng
- ✅ Buttons hiển thị `<p>Sign in</p>` thay vì "Sign in"  
- ✅ Session không persistent sau F5
- ✅ Database performance issues với JSON

### 📊 Performance Improvements

- ⚡ SQLite indexing trên email và user_id
- ⚡ Faster query với proper SQL statements
- ⚡ Reduced memory usage (no loading entire JSON)

### 🚀 How to Test

```powershell
# 1. Di chuyển vào frontend
cd frontend

# 2. Chạy app
python -m streamlit run app.py

# 3. Mở browser
# http://localhost:8501

# 4. Test features:
# - Sign up tài khoản mới
# - Sign in
# - Tạo lịch trình
# - Lưu lịch trình
# - Xem hồ sơ
# - Xóa lịch trình
# - Đăng xuất
```

### 📝 Migration Notes

Nếu bạn đã có `database.json` từ phiên bản cũ:
1. App sẽ tự động migrate sang SQLite
2. File JSON cũ sẽ được rename thành `database.json.backup`
3. Tất cả users và schedules sẽ được preserve

### ⚠️ Breaking Changes

- **Database API changed**: Không còn dùng dict-based session state
- **Navigation changed**: Custom buttons thay vì option_menu
- **Import changed**: `import db_utils` required

### 🔜 Next Steps

1. **Cleanup old files** (optional):
   ```powershell
   Remove-Item -Recurse src, static
   Remove-Item SmartTravel.py
   ```

2. **Add password hashing**:
   - Install bcrypt
   - Hash passwords before storing

3. **Add more features**:
   - Google Maps integration
   - PDF export
   - Share schedule

### 👥 Contributors

- Hoang Cao Phong - Project Manager & AI Engineer
- Development Team

---

**Build**: v2.0.0  
**Date**: November 13, 2025  
**Status**: ✅ Stable
