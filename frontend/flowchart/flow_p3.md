```mermaid
graph TD
   
    P3_START("User vào trang Chức năng")

    P3_START --> P3_NAV[Hiển thị Giao diện có 3 Tabs]

    
    subgraph "Tab 1: Gợi ý"
        direction TB
        
        P3_NAV -- Mặc định --> T1_ShowList[Hiển thị danh sách các gợi ý]
        T1_ShowList --> T1_Click{User bấm vào 1 địa điểm gợi ý}
        T1_Click --> T1_ShowDetail[Hiển thị chi tiết địa điểm đó]
    end

    subgraph "Tab 2: Tìm đường"
        direction TB
        P3_NAV -- Bấm Tab Tìm đường --> T2_ShowForm[Hiển thị Form nhập điểm đi / điểm đến]
        T2_ShowForm --> T2_Input{User nhập điểm A, điểm B}
        T2_Input --> T2_Submit{User bấm nút Tìm đường}
        T2_Submit --> T2_Processing(Hệ thống tính toán lộ trình...)
        T2_Processing --> T2_ShowMap[Hiển thị Lộ trình & Bản đồ]
    end

    
    subgraph "Tab 3: Nhận diện"
        direction TB
        
       
        P3_NAV -- Bấm Tab Nhận diện --> T3_ShowButtons[Hiển thị nút Upload ảnh / Mở Camera]
        T3_ShowButtons -- Bấm Upload --> T3_Upload{User chọn ảnh từ thư viện}
        T3_ShowButtons -- Bấm Camera --> T3_Capture{User chụp ảnh mới}
        T3_Upload --> T3_Process(Hệ thống xử lý ảnh)
        T3_Capture --> T3_Process(Hệ thống xử lý ảnh)
        T3_Process --> T3_ShowResult[Hiển thị kết quả: Tên địa điểm]
        T3_ShowResult --> T3_Save{User có thể bấm Lưu vào lịch trình}
    end

    classDef class_start fill:#4CAF50,color:#fff,stroke:#333
    %% Hành động của User (input/click)
    classDef class_user_action fill:#FFC107,color:#333,stroke:#333
    %% Hệ thống xử lý (processing)
    classDef class_process fill:#AED6F1,color:#333,stroke:#333
    %% Hiển thị giao diện / thông tin (display)
    classDef class_display fill:#f0f0f0,color:#333,stroke:#ccc
    

    class P3_START class_start
    class P3_NAV,T1_ShowList,T1_ShowDetail,T2_ShowForm,T2_ShowMap,T3_ShowButtons,T3_ShowResult class_display
    class T1_Click,T2_Input,T2_Submit,T3_Upload,T3_Capture,T3_Save class_user_action
    class T2_Processing,T3_Process class_process
