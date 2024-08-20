## Tính trừu tượng (Abstraction)

### 1. Định nghĩa
- Tính trừu tượng trong lập trình hướng đối tượng (OOP) là quá trình ẩn đi những chi tiết phức tạp của một hệ thống và chỉ hiển thị cho người dùng những thông tin cần thiết. Nó giúp đơn giản hóa việc tương tác với các đối tượng, cho phép người dùng làm việc với các khái niệm trừu tượng mà không cần quan tâm đến cách chúng được cài đặt chi tiết bên trong.

- Trừu tượng thường được thể hiện thông qua các lớp trừu tượng (abstract classes) và các phương thức trừu tượng (abstract methods). Các lớp trừu tượng không thể được tạo đối tượng trực tiếp mà chỉ được kế thừa bởi các lớp con. Phương thức trừu tượng là những phương thức mà lớp cha khai báo nhưng không cung cấp cài đặt, các lớp con phải ghi đè và cài đặt lại chúng. phương thức của lớp cha để thay đổi hành vi.

### 2. Ví dụ về tính trừu tượng
#### 2.1 Lớp trừu tượng và phương thức trừu tượng
Hãy tưởng tượng rằng chúng ta muốn xây dựng một hệ thống quản lý các loại động vật khác nhau. Chúng ta có một lớp trừu tượng `Animal` chứa các phương thức trừu tượng như `sound()` và `move()`. Các lớp con như `Dog` và `Bird` sẽ kế thừa từ lớp `Animal` và cài đặt cụ thể các phương thức này.
```python
from abc import ABC, abstractmethod

class Animal(ABC):  # Lớp trừu tượng kế thừa từ ABC (Abstract Base Class)
    
    @abstractmethod
    def sound(self):
        pass  # Phương thức trừu tượng, không cài đặt trong lớp cha
    
    @abstractmethod
    def move(self):
        pass  # Phương thức trừu tượng, không cài đặt trong lớp cha
```
Lớp `Animal` không thể tạo đối tượng trực tiếp vì nó chứa các phương thức trừu tượng. Các lớp con phải cài đặt lại phương thức `sound()` và `move()`.

#### 2.2 Cài đặt các lớp con
Bây giờ, chúng ta cài đặt các lớp con như `Dog` và `Bird` kế thừa từ `Animal` và cung cấp chi tiết cụ thể cho các phương thức trừu tượng.
```python
class Dog(Animal):
    def sound(self):
        return "Woof! Woof!"
    
    def move(self):
        return "The dog runs on four legs."
    
class Bird(Animal):
    def sound(self):
        return "Tweet! Tweet!"
    
    def move(self):
        return "The bird flies with its wings."
```
Trong các lớp con, chúng ta định nghĩa chi tiết cho phương thức `sound()` và `move()` dựa trên đặc điểm của từng loài động vật.

#### 2.3 Sử dụng các đối tượng từ các lớp con
Chúng ta không thể tạo đối tượng trực tiếp từ lớp trừu tượng `Animal`, nhưng có thể tạo các đối tượng từ lớp con `Dog` và `Bird`.
```python
dog = Dog()
bird = Bird()

print(dog.sound())  # Kết quả: Woof! Woof!
print(dog.move())  # Kết quả: The dog runs on four legs.

print(bird.sound())  # Kết quả: Tweet! Tweet!
print(bird.move())  # Kết quả: The bird flies with its wings.

```
Giải thích:
- Lớp `Animal`: Đây là một lớp trừu tượng chỉ cung cấp các phương thức trừu tượng mà không có cài đặt chi tiết. Các lớp con như `Dog` và `Bird` phải cung cấp cài đặt cho các phương thức này.

- Phương thức trừu tượng: Trong các lớp con, chúng ta cài đặt lại các phương thức trừu tượng `sound()` và `move()` để phản ánh hành vi cụ thể của từng loài động vật.

### 3. Ví dụ thực tế
Hãy xem xét một hệ thống thanh toán. Chúng ta có thể tạo một lớp trừu tượng `Payment` với các phương thức trừu tượng như `authorize()` và `process()`. Các lớp con như `CreditCardPayment` và `PayPalPayment` sẽ cài đặt cụ thể các phương thức này dựa trên cách xử lý thanh toán khác nhau.
```python
from abc import ABC, abstractmethod

class Payment(ABC):
    
    @abstractmethod
    def authorize(self):
        pass
    
    @abstractmethod
    def process(self):
        pass

class CreditCardPayment(Payment):
    def authorize(self):
        return "Authorizing credit card payment..."
    
    def process(self):
        return "Processing credit card payment..."

class PayPalPayment(Payment):
    def authorize(self):
        return "Authorizing PayPal payment..."
    
    def process(self):
        return "Processing PayPal payment..."

```
Khi chúng ta triển khai hệ thống thanh toán, mỗi loại thanh toán sẽ có cách cài đặt khác nhau, nhưng đều tuân theo cùng một giao diện chung từ lớp `Payment`.
```python
def process_payment(payment: Payment):
    print(payment.authorize())
    print(payment.process())

credit_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

process_payment(credit_payment)
process_payment(paypal_payment)

```
Giải thích:
- Lớp trừu tượng `Payment`: Định nghĩa giao diện chung cho các loại thanh toán với các phương thức trừu tượng `authorize()` và `process()`. Lớp con `CreditCardPayment` và `PayPalPayment`: Cài đặt chi tiết cho các phương thức trừu tượng, mỗi lớp con thực hiện cách thức xử lý thanh toán riêng.

- Hàm `process_payment()`: Nhận đối tượng `Payment` bất kỳ và gọi các phương thức `authorize()` và `process()` mà không cần quan tâm đến loại thanh toán cụ thể.

### 4. Lợi ích của tính trừu tượng
- Giảm độ phức tạp: Bằng cách ẩn đi các chi tiết cài đặt bên trong và chỉ cung cấp giao diện công khai (public interface), trừu tượng giúp giảm độ phức tạp của hệ thống và giúp người dùng tập trung vào việc sử dụng mà không cần hiểu cách nó hoạt động bên trong.

- Tăng tính bảo trì: Khi các chi tiết cài đặt bị ẩn đi, bạn có thể thay đổi hoặc cải thiện chúng mà không ảnh hưởng đến mã sử dụng lớp đó, giúp hệ thống dễ bảo trì hơn.

- Tăng tính linh hoạt: Các lớp con có thể cài đặt các phương thức trừu tượng theo cách riêng, tạo ra các hành vi khác nhau mà vẫn tuân theo cùng một giao diện. Điều này giúp tăng tính linh hoạt khi mở rộng hệ thống.

- Tăng tính tái sử dụng mã: Các lớp trừu tượng cung cấp một khung sườn chung mà các lớp con có thể kế thừa và tùy chỉnh, giúp tái sử dụng mã và giảm thiểu trùng lặp.