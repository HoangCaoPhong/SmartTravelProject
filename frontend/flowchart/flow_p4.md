```mermaid
graph TD
    %% Bắt đầu
    P4_START("User vào trang Lên lịch trình")
    
    P4_START --> P4_ShowForm[Hiển thị Form nhập liệu]
    P4_ShowForm --> P4_Input{User nhập: Sở thích, Ngân sách, Thời gian,...}
    P4_Input --> P4_Submit{User bấm Tạo lịch trình}
    
    %% Quyết định
    P4_Submit --> P4_Validate{Dữ liệu đã hợp lệ chưa?}
    
    P4_Validate -- Không --> P4_Error[Hiển thị thông báo lỗi]
    P4_Error --> P4_ShowForm
    
    %% Luồng xử lý
    P4_Validate -- Có --> P4_Processing(Gửi dữ liệu đến API/Thuật toán AI)
    P4_Processing --> P4_ShowLoading(Hiển thị trạng thái Đang xử lý...)
    P4_ShowLoading --> P4_ShowResult[Hiển thị Kết quả Lịch trình đã tạo]
    
    %% Hành động sau kết quả
    P4_ShowResult --> P4_Save{User bấm Lưu lịch trình}
    P4_Save --> P4_NotifySave[Thông báo lưu thành công]
    
    P4_ShowResult --> P4_Edit{User bấm Chỉnh sửa}
    P4_Edit --> P4_ShowForm

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
    class P4_START class_start
    class P4_Input, P4_Submit,P4_Save,P4_Editclass_user_action
    class P4_Validate class_decision
    class P4_Processing,P4_ShowLoading class_process
    class P4_ShowForm,P4_ShowResult class_display
    class P4_Error class_error
    class P4_NotifySave class_success
  