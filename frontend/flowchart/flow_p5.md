```mermaid
graph TD
    P6_START("User vào trang Sign in / Sign up")
    
    P6_START --> P6_ShowLogin[Hiển thị Form Đăng nhập]
    P6_ShowLogin -- Bấm Chưa có tài khoản? --> P6_ShowRegister[Hiển thị Form Đăng ký]
    P6_ShowRegister -- Bấm Đã có tài khoản? --> P6_ShowLogin

    subgraph "Luồng Đăng nhập"
        direction TB
        P6_InputLogin{User nhập Email & Mật khẩu}
        P6_ShowLogin --> P6_InputLogin
        P6_InputLogin --> P6_SubmitLogin{User bấm Đăng nhập}
        P6_SubmitLogin --> P6_CheckLogin{Kiểm tra thông tin?}
        P6_CheckLogin -- Thất bại --> P6_ErrorLogin[Báo lỗi: Sai thông tin]
        P6_ErrorLogin --> P6_ShowLogin
    end

    %% --- Luồng 2: Đăng ký ---
    subgraph "Luồng Đăng ký"
        direction TB
        P6_InputRegister{User nhập Email, Mật khẩu, Nhập lại Mật khẩu}
        P6_ShowRegister --> P6_InputRegister
        P6_InputRegister --> P6_SubmitRegister{User bấm Đăng ký}
        P6_SubmitRegister --> P6_CheckRegister{Thông tin hợp lệ?}
        P6_CheckRegister -- Không --> P6_ErrorRegister[Báo lỗi: Email tồn tại / Mật khẩu không khớp]
        P6_ErrorRegister --> P6_ShowRegister
    end
    
    %% --- Kết quả thành công (chung cho cả 2 luồng) ---
    P6_CheckLogin -- Thành công --> P6_SUCCESS[Đăng nhập thành công]
    P6_CheckRegister -- Có --> P6_CreateAccount(Tạo tài khoản mới)
    P6_CreateAccount --> P6_SUCCESS

    P6_SUCCESS --> P6_Redirect(Chuyển hướng về Trang chủ - Đã đăng nhập)

    %% --- ĐỊNH NGHĨA STYLE ---
    %% Bắt đầu
    classDef class_start fill:#4CAF50,color:#fff,stroke:#333
    %% Hành động của User (input/click)
    classDef class_user_action fill:#FFC107,color:#333,stroke:#333
    %% Quyết định của hệ thống
    classDef class_decision fill:#FFC107,color:#333,stroke:#333
    %% Hệ thống xử lý (processing)
    classDef class_process fill:#AED6F1,color:#333,stroke:#333
    %% Hiển thị giao diện / thông tin (display)
    classDef class_display fill:#f0f0f0,color:#333,stroke:#ccc
    %% Hiển thị Lỗi (Error)
    classDef class_error fill:#F5B7B1,color:#333,stroke:#ccc
    %% Hiển thị Thành công (Success)
    classDef class_success fill:#A9DFBF,color:#333,stroke:#ccc

    %% --- ÁP DỤNG STYLE ---
    class P6_START class_start
    class P6_ShowLogin,P6_ShowRegister class_display
    class P6_InputLogin,P6_SubmitLogin,P6_InputRegister,P6_SubmitRegister class_user_action
    class P6_CheckLogin,P6_CheckRegister class_decision
    class P6_ErrorLogin,P6_ErrorRegister class_error
    class P6_CreateAccount,P6_Redirect class_process
    class P6_SUCCESS class_success
    