## Tính đóng gói (Encapsulation)

### 1. Định nghĩa
- Tính đóng gói là một trong bốn tính chất cơ bản của lập trình hướng đối tượng (OOP). Nó được sử dụng để bảo vệ dữ liệu khỏi sự truy cập và thay đổi trái phép bằng cách giới hạn quyền truy cập vào các thuộc tính của đối tượng. Thông thường, các thuộc tính của một đối tượng sẽ được đặt là "private" (riêng tư), và chỉ có thể được truy cập hoặc sửa đổi thông qua các phương thức "public" (công khai) mà đối tượng đó cung cấp.

- Đóng gói có thể được xem như việc "gói" dữ liệu và phương thức lại với nhau thành một đơn vị và kiểm soát quyền truy cập vào dữ liệu thông qua các phương thức đặc biệt. Điều này giúp đảm bảo rằng dữ liệu bên trong đối tượng không bị thay đổi một cách ngẫu nhiên và đảm bảo tính toàn vẹn của đối tượng.

### 2. Các thành phần của tính đóng gói
- Private (Riêng tư): Thuộc tính hoặc phương thức được khai báo là private chỉ có thể truy cập và sửa đổi bên trong lớp (class) chứa nó.
- Public (Công khai): Phương thức hoặc thuộc tính được khai báo là public có thể truy cập từ bên ngoài lớp. Thông qua các phương thức công khai này, chúng ta có thể kiểm soát cách mà dữ liệu được truy cập hoặc thay đổi.
- Getter và Setter: Đây là các phương thức công khai được sử dụng để lấy giá trị của một thuộc tính (getter) và thay đổi giá trị của thuộc tính đó (setter). Điều này giúp bảo vệ các thuộc tính khỏi sự thay đổi trái phép hoặc không đúng cách.

### 3. Ví dụ cụ thể về tính đóng gói
Hãy xem xét một ví dụ cụ thể với lớp BankAccount (tài khoản ngân hàng):
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Số tiền gửi phải lớn hơn 0")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Số tiền rút không hợp lệ hoặc không đủ số dư")

    def get_balance(self):
        return self.__balance  # Public method to access private data
```
Giải thích:
- `self.__balance`: Thuộc tính balance được khai báo là private bằng cách thêm hai dấu gạch dưới (__) trước tên biến. Điều này có nghĩa là thuộc tính này chỉ có thể được truy cập từ bên trong lớp BankAccount.
- `deposit()` và `withdraw()`: Đây là các phương thức công khai được sử dụng để thêm hoặc trừ tiền vào tài khoản. Các phương thức này kiểm tra điều kiện trước khi thay đổi số dư, bảo đảm rằng việc thay đổi chỉ diễn ra nếu nó hợp lệ (ví dụ: không thể gửi số tiền âm).
- `get_balance()`: Đây là phương thức công khai (public) để trả về giá trị của balance. Phương thức này cho phép người dùng lấy giá trị số dư mà không thể thay đổi trực tiếp giá trị này.

### 4. Lợi ích của tính đóng gói
- Bảo vệ dữ liệu: Đóng gói giúp bảo vệ dữ liệu bên trong lớp khỏi việc thay đổi hoặc truy cập trái phép. Điều này làm giảm rủi ro lỗi do người dùng hoặc lập trình viên có thể vô tình làm hỏng dữ liệu.

- Duy trì tính toàn vẹn của đối tượng: Các thuộc tính chỉ có thể được thay đổi thông qua các phương thức được định nghĩa sẵn, điều này giúp bảo đảm rằng chỉ những thao tác hợp lệ mới có thể ảnh hưởng đến đối tượng.

- Tăng tính linh hoạt: Nếu một lớp có các thuộc tính và phương thức đóng gói tốt, nó sẽ dễ dàng hơn khi thay đổi hay mở rộng mà không cần phải thay đổi mã sử dụng lớp đó.

- Dễ bảo trì và gỡ lỗi: Khi chỉ có phương thức công khai có thể thay đổi dữ liệu, việc xác định lỗi và điều chỉnh mã sẽ trở nên dễ dàng hơn. Bạn có thể kiểm soát tốt hơn những phần của lớp chịu trách nhiệm thay đổi dữ liệu.