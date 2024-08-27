## Creational pattern

### 1. Singleton Pattern
#### 1.1 Định nghĩa
Singleton pattern đảm bảo rằng chỉ có một instance duy nhất của một class được tạo ra trong suốt vòng đời của ứng dụng. Điều này thường được sử dụng cho các tài nguyên hệ thống như database connections, logging, hoặc các config systems, nơi mà chỉ cần một đối tượng là đủ.
#### 1.2 Ví dụ
Hãy tưởng tượng bạn có một ứng dụng chỉ cần một kết nối duy nhất tới cơ sở dữ liệu. Nếu nhiều kết nối được tạo ra, sẽ tốn nhiều tài nguyên hơn và có thể gây xung đột dữ liệu.
```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # True, vì chỉ có một instance được tạo ra

```
### 2. Factory Pattern
#### 2.1 Định nghĩa
Factory pattern được dùng để tạo ra đối tượng mà không cần phải chỉ định lớp chính xác của đối tượng đó. Điều này rất hữu ích khi bạn có một tập hợp các đối tượng cần được tạo ra dựa trên các điều kiện khác nhau. Nó giúp giảm sự phụ thuộc vào các lớp cụ thể.
#### 2.2 Ví dụ
Bạn cần tạo ra các đối tượng `Dog` hoặc `Cat` tùy thuộc vào đầu vào của người dùng mà không cần biết trước loại động vật nào.
```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()

animal = AnimalFactory.create_animal("dog")
print(animal.speak())  # Woof!

```
### 3. Builder Pattern
#### 3.1 Định nghĩa
Builder pattern cho phép bạn tạo ra các đối tượng phức tạp bằng cách chia nhỏ quá trình khởi tạo thành các bước riêng biệt. Điều này đặc biệt hữu ích khi đối tượng có nhiều thuộc tính và chúng cần được thiết lập theo một trình tự cụ thể.

#### 3.2 Ví dụ
Bạn có thể dùng Builder để tạo ra một chiếc burger với nhiều thành phần tùy chọn như rau, cà chua, phô mai, mà không phải tạo ra hàng tá constructors với nhiều tham số khác nhau.
```python
class Burger:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def __str__(self):
        return f"Burger with: {', '.join(self.ingredients)}"

class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def add_lettuce(self):
        self.burger.add_ingredient("Lettuce")
        return self

    def add_tomato(self):
        self.burger.add_ingredient("Tomato")
        return self

    def add_cheese(self):
        self.burger.add_ingredient("Cheese")
        return self

    def build(self):
        return self.burger

burger = BurgerBuilder().add_lettuce().add_tomato().add_cheese().build()
print(burger)  # Burger with: Lettuce, Tomato, Cheese

```