## Tính kế thừa (Inheritance)

### 1. Định nghĩa
- Tính kế thừa là một trong bốn tính chất cơ bản của lập trình hướng đối tượng (OOP), cho phép một lớp (class) mới có thể sử dụng lại các thuộc tính và phương thức của một lớp đã có mà không cần viết lại mã. Lớp mới được gọi là lớp con (subclass) hoặc lớp dẫn xuất (derived class), trong khi lớp đã có được gọi là lớp cha (parent class) hoặc lớp cơ sở (base class).

- Lớp con kế thừa tất cả các thuộc tính và phương thức của lớp cha, đồng thời có thể bổ sung thêm các thuộc tính, phương thức mới hoặc ghi đè (override) các phương thức của lớp cha để thay đổi hành vi.

### 2. Các thành phần của tính kế thừa
- Lớp cha (Parent Class): Đây là lớp cơ sở mà các lớp khác có thể kế thừa.

- Lớp con (Child Class): Lớp kế thừa từ lớp cha, sử dụng lại các phương thức và thuộc tính của lớp cha và có thể mở rộng chúng.

- Ghi đè phương thức (Method Overriding): Lớp con có thể định nghĩa lại phương thức đã có trong lớp cha để thay đổi hoặc mở rộng hành vi của phương thức đó.

### 3. Ví dụ cụ thể về tính kế thừa
Hãy xem xét ví dụ về một hệ thống phương tiện giao thông:
```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make  # Thương hiệu xe
        self.model = model  # Mẫu xe
    
    def start_engine(self):
        return "The engine is starting."
    
    def stop_engine(self):
        return "The engine is stopping."
```
Lớp `Vehicle` định nghĩa các thuộc tính như make (thương hiệu) và model (mẫu xe), và các phương thức như `start_engine()` và `stop_engine()`.

Lớp con: Car
```python
class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)  # Gọi đến constructor của lớp cha
        self.doors = doors  # Số cửa
    
    def open_doors(self):
        return f"Opening {self.doors} doors."
```
Lớp Car kế thừa từ lớp `Vehicle`. Nó sử dụng lại các thuộc tính và phương thức của `Vehicle`, đồng thời bổ sung thêm thuộc tính mới doors và phương thức mới `open_doors()`.

Lớp con: `Motorcycle`
```python
class Motorcycle(Vehicle):
    def __init__(self, make, model, has_sidecar):
        super().__init__(make, model)  # Gọi đến constructor của lớp cha
        self.has_sidecar = has_sidecar  # Xe có sidecar hay không
    
    def has_sidecar(self):
        return "This motorcycle has a sidecar." if self.has_sidecar else "This motorcycle does not have a sidecar."
```
Lớp `Motorcycle` cũng kế thừa từ `Vehicle` và bổ sung thêm thuộc tính `has_sidecar` và phương thức mới `has_sidecar()`.

Sử dụng các lớp con
```python
# Tạo đối tượng Car và Motorcycle
car = Car("Toyota", "Camry", 4)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", False)

# Sử dụng các phương thức của lớp cha và lớp con
print(car.start_engine())  # Kế thừa từ lớp Vehicle
print(car.open_doors())  # Phương thức mới trong lớp Car

print(motorcycle.start_engine())  # Kế thừa từ lớp Vehicle
print(motorcycle.has_sidecar())  # Phương thức mới trong lớp Motorcycle
```

Giải thích:
- Lớp Vehicle: Đây là lớp cha với các thuộc tính và phương thức chung cho tất cả các loại phương tiện (ví dụ: bắt đầu và dừng động cơ).

- Lớp Car và lớp Motorcycle: Đây là các lớp con kế thừa từ Vehicle. Chúng sử dụng lại các phương thức của Vehicle như start_engine() và stop_engine(). Đồng thời, mỗi lớp con mở rộng lớp cha bằng cách thêm các thuộc tính và phương thức cụ thể như doors cho lớp Car và has_sidecar cho lớp Motorcycle.

- super(): Hàm super() trong constructor của lớp con được sử dụng để gọi đến constructor của lớp cha, giúp lớp con có thể khởi tạo các thuộc tính của lớp cha mà không cần viết lại mã.

### 4. Ghi đè phương thức (Method Overriding)
Lớp con có thể ghi đè phương thức của lớp cha để thay đổi hành vi. Ví dụ, trong lớp `Car`, chúng ta có thể ghi đè phương thức `start_engine()` để thay đổi cách thức hoạt động của nó.
```python
class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors
    
    def start_engine(self):
        return "The car engine is starting with a roar."
```
Bây giờ khi bạn gọi phương thức start_engine() của đối tượng Car, kết quả sẽ là "The car engine is starting with a roar." thay vì hành vi mặc định từ lớp cha.

### 5. Lợi ích của tính kế thừa
- Tái sử dụng mã (Code Reusability): Lớp con có thể kế thừa các thuộc tính và phương thức của lớp cha mà không cần viết lại mã, giúp giảm thiểu việc trùng lặp mã và dễ dàng duy trì hơn.

- Tính mở rộng (Extensibility): Kế thừa cho phép mở rộng chức năng của một lớp mà không cần thay đổi mã gốc, giúp xây dựng hệ thống linh hoạt và dễ mở rộng.

- Tổ chức và phân cấp (Organization and Hierarchy): Tính kế thừa giúp tổ chức mã theo cấu trúc phân cấp, cho phép dễ dàng hiểu được mối quan hệ giữa các lớp và phân chia trách nhiệm giữa các thành phần của hệ thống.

- Tính nhất quán (Consistency): Việc sử dụng các phương thức chung của lớp cha đảm bảo tính nhất quán trong cách thức hoạt động của các đối tượng thuộc các lớp con khác nhau.

