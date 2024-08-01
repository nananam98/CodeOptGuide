
# Lập trình thủ tục và hướng đối tượng

## 1. Lập trình thủ tục (Procedural Programing)
### 1.1 Định nghĩa
Lập trình thủ tục là một phương pháp lập trình tập trung vào các hàm hoặc thủ tục để thực hiện các nhiệm vụ cụ thể. Các hàm này được gọi trong một trình tự để hoàn thành công việc. Đây là cách lập trình rất phổ biến và dễ hiểu, đặc biệt là cho các nhiệm vụ đơn giản hoặc các chương trình nhỏ.

### 1.2 Đặc điểm chính
- Hàm: Các phần mã được chia thành các hàm thực hiện các tác vụ cụ thể.
- Trình tự: Các hàm được gọi theo một trình tự cụ thể.
- Dữ liệu toàn cục và cục bộ: Dữ liệu có thể được khai báo toàn cục (global) hoặc cục bộ (local) trong hàm.

### 1.3. Quy ước đặt tên
- Biến: Sử dụng tên biến theo cú pháp snake_case. Ví dụ: `tong_so`, `danh_sach_so`.
- Hàm: Sử dụng tên hàm theo cú pháp snake_case. Ví dụ: `tinh_tong`, `doc_file`.

### 1.4. Điểm mạnh
- Đơn giản và Dễ Hiểu: Các chương trình được chia nhỏ thành các hàm đơn giản và dễ quản lý.
- Hiệu Suất Cao: Ít tài nguyên hơn do không cần quản lý các đối tượng và mối quan hệ giữa chúng.
- Phù Hợp với Nhiệm Vụ Đơn Giản: Thích hợp cho các tác vụ hoặc chương trình nhỏ, không phức tạp.
- Trực Quan: Dễ dàng theo dõi luồng thực hiện của chương trình từ trên xuống dưới.

### 1.5. Điểm yếu
- Khó Bảo Trì: Khi chương trình trở nên lớn và phức tạp, việc bảo trì và mở rộng sẽ trở nên khó khăn.
- Thiếu Tính Tái Sử Dụng: Các hàm thường không dễ dàng tái sử dụng do không có cấu trúc mô-đun rõ ràng.
- Quản Lý Dữ Liệu Kém: Biến toàn cục có thể dẫn đến lỗi không mong muốn và khó theo dõi.
- Thiếu Tính Trừu Tượng: Không có cách để mô hình hóa các khái niệm phức tạp bằng các đối tượng và mối quan hệ giữa chúng.

### 1.6. Ví dụ
```python
# Lập trình thủ tục

# Hàm tính tổng
def tinh_tong(danh_sach):
    tong = 0
    for so in danh_sach:
        tong += so
    return tong

# Hàm chính
def main():
    danh_sach_so = [1, 2, 3, 4, 5]
    ket_qua = tinh_tong(danh_sach_so)
    print(f"Tổng của danh sách là: {ket_qua}")

# Gọi hàm chính
main()
```
Trong ví dụ này, `tinh_tong` là một hàm được gọi trong hàm chính `main` để tính tổng của danh sách số.

## 2. Lập trình hướng đối tượng (Object Oriented Programing)
### 2.1 Định nghĩa
Lập trình hướng đối tượng là một phương pháp lập trình tập trung vào các đối tượng, là sự kết hợp của dữ liệu và các phương thức (hàm) thao tác trên dữ liệu đó. Nó rất hiệu quả cho các dự án lớn và phức tạp vì tính mô-đun và khả năng tái sử dụng cao.

### 2.2 Đặc điểm chính
- Đối tượng và Lớp (Object and Class): Đối tượng (Object) là thực thể, trong khi lớp (Class) là khuôn mẫu cho các đối tượng.
- Tính kế thừa: Lớp con có thể kế thừa các thuộc tính và phương thức của lớp cha.
- Tính đóng gói: Dữ liệu và phương thức được bao gói trong đối tượng, hạn chế truy cập trực tiếp từ bên ngoài.
- Tính đa hình: Cùng một phương thức có thể có các hành vi khác nhau dựa trên đối tượng gọi nó.
- Tính trừu tượng: Mô hình hoá các mối quan hệ đối tượng

### 2.3 Quy ước đặt tên
- Lớp: Sử dụng tên lớp theo cú pháp PascalCase. Ví dụ: `DanhSachSo`, `XeHoi`.
- Phương thức: Sử dụng tên phương thức theo cú pháp snake_case. Ví dụ: `tinh_tong`, `chay`.

### 2.4 Điểm mạnh
- Tái Sử Dụng Mã Cao: Các lớp và đối tượng có thể dễ dàng tái sử dụng trong các phần khác của chương trình hoặc trong các dự án khác.
- Bảo Trì và Mở Rộng Dễ Dàng: Chương trình được chia nhỏ thành các đối tượng có thể dễ dàng bảo trì và mở rộng.
- Quản Lý Dữ Liệu Tốt: Tính đóng gói giúp bảo vệ và quản lý dữ liệu hiệu quả hơn.
- Tính Trừu Tượng: Dễ dàng mô hình hóa các khái niệm phức tạp và các mối quan hệ giữa chúng.
- Tính Đa Hình và Kế Thừa: Giúp giảm thiểu sự trùng lặp mã và tạo ra các hệ thống linh hoạt hơn.

### 2.5 Điểm yếu
- Phức Tạp Hơn: Cấu trúc chương trình phức tạp hơn và cần nhiều tài nguyên hơn để quản lý các đối tượng.
- Hiệu Suất Thấp Hơn: Đòi hỏi nhiều tài nguyên hơn do quản lý các đối tượng và mối quan hệ giữa chúng.
- Khó Học Hơn: Cần thời gian và nỗ lực để hiểu và áp dụng đúng các nguyên lý của lập trình hướng đối tượng.
- Quá Tải Cho Các Nhiệm Vụ Đơn Giản: Không thích hợp cho các chương trình nhỏ hoặc đơn giản do cấu trúc phức tạp.

### 2.6 Các hàm đặc biệt
- `__init__`: Hàm khởi tạo, được gọi khi một đối tượng mới của lớp được tạo ra.
- `__getitem__`, `__setitem__`, `__delitem__`: Các hàm cho phép truy cập, gán và xóa phần tử của đối tượng như một danh sách hoặc từ điển.
- `__call__`: Cho phép đối tượng hoạt động như một hàm.

| Hàm đặc biệt          | Mô tả                                                                           | Hành vi mặc định nếu không định nghĩa                               |
|-----------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------|
| `__init__(self, ...)` | Hàm khởi tạo đối tượng, được gọi khi tạo một đối tượng mới.                      | Sử dụng phương thức khởi tạo mặc định không làm gì cả.              |
| `__str__(self)`       | Trả về chuỗi mô tả đối tượng khi sử dụng `str()` hoặc `print()`.                | Trả về chuỗi biểu diễn đối tượng kiểu `<MyClass object at 0x...>`. |
| `__repr__(self)`      | Trả về chuỗi mô tả chính xác hơn của đối tượng, thường dùng cho debug.          | Trả về chuỗi biểu diễn đối tượng kiểu `<MyClass object at 0x...>`. |
| `__len__(self)`       | Trả về độ dài của đối tượng khi sử dụng `len()`.                                | Gây ra lỗi `TypeError`.                                             |
| `__getitem__(self, key)` | Truy cập phần tử của đối tượng như một danh sách hoặc từ điển.                | Gây ra lỗi `TypeError`.                                             |
| `__setitem__(self, key, value)` | Gán giá trị cho phần tử của đối tượng.                                 | Gây ra lỗi `TypeError`.                                             |
| `__delitem__(self, key)` | Xóa phần tử của đối tượng.                                                    | Gây ra lỗi `TypeError`.                                             |
| `__iter__(self)`      | Trả về một iterator cho đối tượng.                                              | Gây ra lỗi `TypeError`.                                             |
| `__next__(self)`      | Lấy phần tử tiếp theo từ iterator.                                              | Gây ra lỗi `TypeError`.                                             |
| `__contains__(self, item)` | Kiểm tra xem phần tử có trong đối tượng hay không.                         | Gây ra lỗi `TypeError`.                                             |
| `__call__(self, *args, **kwargs)` | Cho phép đối tượng hoạt động như một hàm.                           | Gây ra lỗi `TypeError`.                                             |
| `__eq__(self, other)` | So sánh hai đối tượng xem chúng có bằng nhau không.                             | So sánh dựa trên vị trí trong bộ nhớ.                                |
| `__lt__(self, other)` | So sánh xem đối tượng có nhỏ hơn đối tượng khác không.                          | So sánh dựa trên vị trí trong bộ nhớ.                                |
| `__le__(self, other)` | So sánh xem đối tượng có nhỏ hơn hoặc bằng đối tượng khác không.                | So sánh dựa trên vị trí trong bộ nhớ.                                |
| `__gt__(self, other)` | So sánh xem đối tượng có lớn hơn đối tượng khác không.                          | So sánh dựa trên vị trí trong bộ nhớ.                                |
| `__ge__(self, other)` | So sánh xem đối tượng có lớn hơn hoặc bằng đối tượng khác không.                | So sánh dựa trên vị trí trong bộ nhớ.                                |
| `__add__(self, other)` | Cộng hai đối tượng.                                                            | Gây ra lỗi `TypeError`.                                             |
| `__sub__(self, other)` | Trừ hai đối tượng.                                                            | Gây ra lỗi `TypeError`.                                             |
| `__mul__(self, other)` | Nhân hai đối tượng.                                                           | Gây ra lỗi `TypeError`.                                             |
| `__truediv__(self, other)` | Chia hai đối tượng.                                                       | Gây ra lỗi `TypeError`.                                             |
| `__mod__(self, other)` | Tính toán phần dư của phép chia.                                              | Gây ra lỗi `TypeError`.                                             |
| `__pow__(self, other)` | Tính lũy thừa của đối tượng.                                                  | Gây ra lỗi `TypeError`.                                             |
| `__and__(self, other)` | Toán tử `&` (AND bitwise) giữa hai đối tượng.                                  | Gây ra lỗi `TypeError`.                                             |
| `__or__(self, other)`  | Toán tử `|` (OR bitwise) giữa hai đối tượng.                                   | Gây ra lỗi `TypeError`.                                             |
| `__xor__(self, other)` | Toán tử `^` (XOR bitwise) giữa hai đối tượng.                                  | Gây ra lỗi `TypeError`.                                             |
| `__invert__(self)`    | Toán tử `~` (NOT bitwise) trên đối tượng.                                       | Gây ra lỗi `TypeError`.                                             |
| `__iadd__(self, other)` | Toán tử `+=` (cộng vào đối tượng hiện tại).                                  | Gây ra lỗi `TypeError`.                                             |
| `__isub__(self, other)` | Toán tử `-=` (trừ từ đối tượng hiện tại).                                    | Gây ra lỗi `TypeError`.                                             |
| `__imul__(self, other)` | Toán tử `*=` (nhân vào đối tượng hiện tại).                                  | Gây ra lỗi `TypeError`.                                             |
| `__itruediv__(self, other)` | Toán tử `/=` (chia vào đối tượng hiện tại).                              | Gây ra lỗi `TypeError`.                                             |
| `__imod__(self, other)` | Toán tử `%=` (phép chia phần dư vào đối tượng hiện tại).                     | Gây ra lỗi `TypeError`.                                             |
| `__ipow__(self, other)` | Toán tử `**=` (lũy thừa vào đối tượng hiện tại).                             | Gây ra lỗi `TypeError`.                                             |
| `__iand__(self, other)` | Toán tử `&=` (AND bitwise vào đối tượng hiện tại).                           | Gây ra lỗi `TypeError`.                                             |
| `__ior__(self, other)` | Toán tử `|=` (OR bitwise vào đối tượng hiện tại).                             | Gây ra lỗi `TypeError`.                                             |
| `__ixor__(self, other)` | Toán tử `^=` (XOR bitwise vào đối tượng hiện tại).                           | Gây ra lỗi `TypeError`.                                             |
| `__neg__(self)`       | Toán tử `-` (phủ định) trên đối tượng.                                          | Gây ra lỗi `TypeError`.                                             |
| `__pos__(self)`       | Toán tử `+` (dương) trên đối tượng.                                             | Gây ra lỗi `TypeError`.                                             |
| `__abs__(self)`       | Toán tử `abs()` (giá trị tuyệt đối) trên đối tượng.                             | Gây ra lỗi `TypeError`.                                             |
| `__round__(self, n)`  | Toán tử `round()` (làm tròn) trên đối tượng.                                    | Gây ra lỗi `TypeError`.                                             |
| `__floor__(self)`     | Toán tử `math.floor()` (làm tròn xuống) trên đối tượng.                         | Gây ra lỗi `TypeError`.                                             |
| `__ceil__(self)`      | Toán tử `math.ceil()` (làm tròn lên) trên đối tượng.                            | Gây ra lỗi `TypeError`.                                             |
| `__trunc__(self)`     | Toán tử `math.trunc()` (cắt phần thập phân) trên đối tượng.                     | Gây ra lỗi `TypeError`.                                             |

### 2.7 Ví dụ
```python
# Lập trình hướng đối tượng

# Định nghĩa lớp
class DanhSachSo:
    def __init__(self, danh_sach):
        self.danh_sach = danh_sach

    def tinh_tong(self):
        return sum(self.danh_sach)

# Sử dụng lớp
def main():
    danh_sach_so = DanhSachSo([1, 2, 3, 4, 5])
    ket_qua = danh_sach_so.tinh_tong()
    print(f"Tổng của danh sách là: {ket_qua}")

# Gọi hàm chính
main()
```