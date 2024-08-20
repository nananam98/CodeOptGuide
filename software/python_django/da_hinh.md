## Tính đa hình (Polymorphism)

### 1. Định nghĩa
- Tính đa hình là một trong những tính chất cơ bản của lập trình hướng đối tượng (OOP), cho phép các đối tượng thuộc các lớp khác nhau có thể được xử lý theo cùng một cách thông qua một giao diện chung, mặc dù các đối tượng này có thể có các hành vi khác nhau.

- Nói một cách đơn giản, đa hình cho phép một phương thức có thể có nhiều cách thực thi khác nhau, tùy thuộc vào đối tượng thực thi nó. Điều này giúp tăng tính linh hoạt và mở rộng của chương trình, cho phép bạn xử lý nhiều loại đối tượng khác nhau một cách thống nhất.

### 2. Hai loại đa hình chính trong OOP
#### 2.1 Đa hình qua phương thức ghi đè (Method Overriding):
Xảy ra khi lớp con cung cấp một triển khai khác cho một phương thức đã được định nghĩa trong lớp cha. Điều này cho phép lớp con cung cấp hành vi cụ thể cho phương thức đó.

#### 2.2 Đa hình qua phương thức nạp chồng (Method Overloading):
Xảy ra khi một lớp có nhiều phương thức cùng tên nhưng khác nhau về tham số (số lượng hoặc kiểu dữ liệu của tham số). Tuy nhiên, phương thức này không phổ biến trong Python, Javascript vì Python không hỗ trợ nạp chồng phương thức và Javascript cũng không hỗ trợ một cách chính thức như trong các ngôn ngữ khác như Java hoặc C++.

Ví dụ trong Java
```java
class Calculator {
    // Phương thức cộng hai số nguyên
    public int add(int a, int b) {
        return a + b;
    }

    // Phương thức cộng hai số thập phân
    public double add(double a, double b) {
        return a + b;
    }

    // Phương thức cộng ba số nguyên
    public int add(int a, int b, int c) {
        return a + b + c;
    }
}

public class Main {
    public static void main(String[] args) {
        Calculator calc = new Calculator();

        // Gọi phương thức add với các tham số khác nhau
        System.out.println(calc.add(10, 20)); // Output: 30 (cộng hai số nguyên)
        System.out.println(calc.add(5.5, 4.5)); // Output: 10.0 (cộng hai số thập phân)
        System.out.println(calc.add(1, 2, 3)); // Output: 6 (cộng ba số nguyên)
    }
}

```
Giải thích:
Phương thức add được nạp chồng với ba phiên bản khác nhau:
- Một phương thức nhận hai số nguyên (int).
- Một phương thức nhận hai số thập phân (double).
- Một phương thức nhận ba số nguyên (int).
- Khi gọi phương thức add, Java sẽ tự động chọn phiên bản phù hợp dựa trên kiểu dữ liệu và số lượng tham số bạn truyền vào.

Ví dụ trong C++
```cpp
#include <iostream>
using namespace std;

class Calculator {
public:
    // Phương thức cộng hai số nguyên
    int add(int a, int b) {
        return a + b;
    }

    // Phương thức cộng hai số thập phân
    double add(double a, double b) {
        return a + b;
    }

    // Phương thức cộng ba số nguyên
    int add(int a, int b, int c) {
        return a + b + c;
    }
};

int main() {
    Calculator calc;

    // Gọi phương thức add với các tham số khác nhau
    cout << calc.add(10, 20) << endl;       // Output: 30 (cộng hai số nguyên)
    cout << calc.add(5.5, 4.5) << endl;     // Output: 10.0 (cộng hai số thập phân)
    cout << calc.add(1, 2, 3) << endl;      // Output: 6 (cộng ba số nguyên)

    return 0;
}
```
Giải thích:
Tương tự như Java, trong C++ chúng ta có ba phương thức add được nạp chồng:
- Một phương thức cộng hai số nguyên (int).
- Một phương thức cộng hai số thập phân (double).
- Một phương thức cộng ba số nguyên (int).
- Khi gọi hàm add, C++ sẽ lựa chọn đúng phiên bản hàm phù hợp với các tham số mà bạn truyền vào.

### 3. Lợi ích của tính đa hình
- Tăng tính linh hoạt và mở rộng: Tính đa hình cho phép thêm các lớp mới mà không cần phải thay đổi mã hiện tại. Bạn có thể thêm các lớp con mới mà hệ thống vẫn hoạt động mà không cần thay đổi các phương thức hoặc hàm sử dụng các đối tượng đó.

- Giảm trùng lặp mã: Đa hình cho phép sử dụng một phương thức chung cho nhiều đối tượng khác nhau, giúp giảm thiểu việc viết lại mã và tăng tính tái sử dụng.

- Khả năng mở rộng tự nhiên: Khi hệ thống cần mở rộng với các loại đối tượng mới, các lớp mới có thể dễ dàng tích hợp vào hệ thống mà không cần viết lại mã cũ, nhờ vào khả năng xử lý đối tượng theo kiểu chung.