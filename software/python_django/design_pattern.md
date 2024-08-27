## Design Pattern

### 1. Định nghĩa
Design pattern là các giải pháp thiết kế phổ biến và đã được kiểm chứng cho các vấn đề phát sinh trong quá trình phát triển phần mềm. Các pattern này là những "mẫu thiết kế" giúp lập trình viên giải quyết các vấn đề thường gặp một cách có tổ chức và hiệu quả hơn.

### 2. Đặc điểm của design pattern
- Không phải là code cụ thể: Design pattern không phải là mã nguồn, mà là các giải pháp trừu tượng có thể được điều chỉnh để áp dụng vào nhiều tình huống khác nhau trong các dự án khác nhau.
- Tính tái sử dụng: Design pattern được thiết kế để tái sử dụng trong các tình huống khác nhau. Khi đã hiểu rõ pattern, bạn có thể áp dụng nó vào nhiều dự án mà không cần phải phát minh lại cách giải quyết.
- Làm tăng tính mô-đun và bảo trì: Các pattern giúp mã nguồn trở nên dễ đọc, bảo trì và nâng cấp hơn bằng cách chuẩn hóa cách giải quyết vấn đề. Khi tất cả lập trình viên trong nhóm sử dụng cùng một design pattern, việc bảo trì và mở rộng dự án trở nên dễ dàng hơn.

### 3. Lợi ích của design pattern
Design pattern thường được chia thành ba nhóm chính:
#### 3.1 Creational Patterns (Nhóm khởi tạo):
- Tập trung vào việc khởi tạo đối tượng một cách linh hoạt và hiệu quả.
- Ví dụ: Singleton, Factory, Builder, Prototype.
#### 3.2 Structural Patterns (Nhóm cấu trúc):
- Tập trung vào cách tổ chức các lớp và đối tượng để xây dựng các cấu trúc lớn hơn và phức tạp hơn.
- Ví dụ: Adapter, Decorator, Facade, Composite.
#### 3.3 Behavioral Patterns (Nhóm hành vi):
- Tập trung vào giao tiếp và tương tác giữa các đối tượng.
- Ví dụ: Observer, Strategy, Command, State.

### 4. Các loại design pattern
| **Loại Pattern**       | **Tên Pattern**        | **Mục Tiêu**                                                          |
|------------------------|------------------------|------------------------------------------------------------------------|
| **Creational Patterns** | Singleton              | Đảm bảo chỉ có một instance của class.                                 |
|                        | Factory                | Tạo đối tượng mà không cần biết class cụ thể.                           |
|                        | Builder                | Tạo đối tượng phức tạp theo từng bước.                                 |
| **Structural Patterns** | Adapter                | Cho phép các class với giao diện khác nhau làm việc cùng nhau.         |
|                        | Decorator              | Thêm tính năng mới vào đối tượng hiện tại mà không thay đổi cấu trúc.   |
| **Behavioral Patterns** | Observer               | Thông báo cho các đối tượng khác khi có thay đổi trạng thái.           |
|                        | Strategy               | Thay đổi thuật toán trong runtime mà không ảnh hưởng đến lớp cơ bản.    |