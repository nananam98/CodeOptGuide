## Behavioral Pattern

### 1. Observer Pattern
#### 1.1 Định nghĩa
Observer pattern cho phép một đối tượng thông báo cho nhiều đối tượng khác khi có thay đổi. Pattern này hữu ích trong các hệ thống mà một sự kiện thay đổi có thể ảnh hưởng đến nhiều đối tượng khác nhau.

#### 1.2 Ví dụ
Khi giá cổ phiếu thay đổi, tất cả các hệ thống giám sát giá đều cần được cập nhật.
```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

class ConcreteObserver:
    def update(self):
        print("Observer has been notified!")

subject = Subject()
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject.attach(observer1)
subject.attach(observer2)
subject.notify()

```
### 2. Strategy Pattern
#### 2.1 Định nghĩa
Strategy pattern cho phép bạn thay thế thuật toán được sử dụng bên trong một lớp mà không làm thay đổi cách thức hoạt động bên ngoài của lớp đó. Điều này giúp dễ dàng thay đổi cách giải quyết một vấn đề mà không phải sửa đổi nhiều mã nguồn.

#### 2.2 Ví dụ
Bạn có thể có nhiều chiến lược tính toán chi phí giao hàng khác nhau (theo cân nặng, theo khoảng cách). Tùy vào yêu cầu của khách hàng mà bạn có thể thay đổi chiến lược trong runtime.

```python
class Strategy:
    def execute(self):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self):
        print("Strategy A is used")

class ConcreteStrategyB(Strategy):
    def execute(self):
        print("Strategy B is used")

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self):
        self._strategy.execute()

context = Context(ConcreteStrategyA())
context.execute_strategy()  # Strategy A is used

context.set_strategy(ConcreteStrategyB())
context.execute_strategy()  # Strategy B is used

```