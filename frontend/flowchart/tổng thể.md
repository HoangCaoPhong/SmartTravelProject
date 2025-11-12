```mermaid
graph TD
 
    A(Bắt đầu Web) --> B{Người dùng đã Đăng nhập?}

    B -- Không --> D["MENU: Trang chủ / Giới thiệu / Chức năng / Lên lịch trình / Sign in / Sign up"]
    B -- Có --> C["MENU: Trang chủ / Giới thiệu / Chức năng / Lên lịch trình / Hồ sơ"]

  
    subgraph "Luồng khách (Chưa đăng nhập)"
        direction LR %% Xếp các node trong nhóm này từ Trái sang Phải
        
        D -- Chọn Trang chủ --> P1g("Trang chủ: Giới thiệu chung, Stats")
        D -- Chọn Giới thiệu --> P2g("Giới thiệu: Đề tài & Mục tiêu")
        D -- Chọn Chức năng --> P3g("Chức năng: Tabs (Gợi ý / Tìm đường / Nhận diện)")
        D -- Chọn Lên lịch trình --> P4g("Lên lịch trình: form nhập liệu & Kết quả")
        D -- "Chọn Sign in / Sign up" --> P6("Trang Đăng nhập / Đăng ký")
    end

-
    subgraph "Luồng thành viên (Đã đăng nhập)"
        direction LR %% Xếp các node trong nhóm này từ Trái sang Phải
        
        %% Đặt ID cho các node này là P1, P2... (hoặc P1m - m = member)
        C -- Chọn Trang chủ --> P1("Trang chủ: Giới thiệu chung, Stats")
        C -- Chọn Giới thiệu --> P2("Giới thiệu: Đề tài & Mục tiêu")
        C -- Chọn Chức năng --> P3("Chức năng: Tabs (Gợi ý / Tìm đường / Nhận diện)")
        C -- Chọn Lên lịch trình --> P4("Lên lịch trình: form nhập liệu & Kết quả")
        C -- Chọn Hồ sơ --> P5("Hồ sơ: Thông tin TK, Lịch trình đã lưu")
    end 



    classDef class_start fill:#4CAF50,color:#fff,stroke:#333,stroke-width:2px 

    classDef class_decision fill:#FFC107,color:#333,stroke:#333,stroke-width:2px 

    classDef class_menu fill:#2196F3,color:#fff,stroke:#333,stroke-width:2px 

    classDef class_page fill:#f0f0f0,color:#333,stroke:#ccc,stroke-width:1px 

    class A class_start
    class B class_decision
    class C,D class_menu
    
    class P1,P2,P3,P4,P5,P6 class_page
    class P1g,P2g,P3g,P4g class_page
 