## Structural pattern

### 1. Adapter Pattern
#### 1.1 Định nghĩa
Adapter pattern cho phép các đối tượng với giao diện không tương thích có thể làm việc cùng nhau. Pattern này thường được sử dụng khi bạn cần tích hợp mã mới vào một hệ thống cũ mà không thể sửa đổi lớp cũ.
#### 1.2 Ví dụ
Bạn có một thiết bị sử dụng ổ cắm chuẩn Châu Âu và bạn muốn sử dụng nó với ổ cắm của Mỹ. Thay vì thay đổi thiết bị, bạn sử dụng một adapter để tương thích với ổ cắm mới.
```python
class EuropeanPlug:
    def provide_power(self):
        return "220V"

class USPlug:
    def provide_power(self):
        return "110V"

class Adapter:
    def __init__(self, plug):
        self.plug = plug

    def provide_power(self):
        if isinstance(self.plug, EuropeanPlug):
            return "110V converted from 220V"
        return self.plug.provide_power()

european_plug = EuropeanPlug()
adapter = Adapter(european_plug)
print(adapter.provide_power())  # 110V converted from 220V

```
### 2. Decorator Pattern
#### 2.1 Định nghĩa
Decorator pattern cho phép bạn thêm các tính năng mới vào một đối tượng hiện có mà không thay đổi lớp ban đầu. Điều này rất hữu ích khi bạn cần mở rộng hành vi của một đối tượng mà không cần kế thừa hoặc sửa đổi lớp ban đầu.
#### 2.2 Ví dụ
Bạn có một đối tượng `Coffee` và muốn thêm các thành phần như sữa hoặc đường mà không thay đổi mã nguồn gốc của đối tượng đó.
```python
class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 1

coffee = Coffee()
coffee_with_milk = MilkDecorator(coffee)
print(coffee_with_milk.cost())  # 6

```