## Map - Reduce trong python

### 1. Map
#### 1.1 Định nghĩa
`map()` là một hàm tích hợp trong Python, nó cho phép bạn áp dụng một hàm nhất định lên tất cả các phần tử của một danh sách (hoặc iterable khác) mà không cần sử dụng vòng lặp.
#### 1.2 Cú pháp
```python
map(function, iterable)
```
- function: Hàm bạn muốn áp dụng cho mỗi phần tử trong iterable.
- iterable: Bất kỳ đối tượng nào có thể lặp được (như danh sách, tuple, v.v.)
#### 1.3 Ví dụ
Giả sử bạn có một danh sách số và muốn tính bình phương của mỗi số.
```python
numbers = [1, 2, 3, 4, 5]

# Sử dụng map để áp dụng hàm tính bình phương lên mỗi số
squared_numbers = map(lambda x: x ** 2, numbers)

# Chuyển kết quả từ map thành danh sách
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
```

### 2. Reduce
#### 2.1 Định nghĩa
`reduce()` không tích hợp sẵn trong Python 3 mà nằm trong module functools. Nó được sử dụng để áp dụng một hàm vào một cặp phần tử từ iterable (bắt đầu với 2 phần tử đầu tiên) và tiếp tục áp dụng hàm đó lên kết quả và phần tử tiếp theo cho đến khi chỉ còn một giá trị duy nhất.
#### 2.2 Cú pháp
```python
from functools import reduce
reduce(function, iterable)
```
- function: Hàm cần áp dụng. Hàm này phải nhận hai đối số.
- iterable: Danh sách hoặc iterable khác mà bạn muốn giảm.
#### 2.3 Ví dụ
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sử dụng reduce để tính tổng các phần tử
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

print(sum_of_numbers)  # Output: 15
```

### 3. Kết hợp Map - Reduce
Bạn có thể kết hợp `map()` và `reduce()` để tạo ra những thao tác phức tạp hơn.  
Ví dụ, tính tổng bình phương của các số trong một danh sách.
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sử dụng map để tính bình phương của các số
squared_numbers = map(lambda x: x ** 2, numbers)

# Sử dụng reduce để tính tổng các bình phương
sum_of_squares = reduce(lambda x, y: x + y, squared_numbers)

print(sum_of_squares)  # Output: 55
```
### 4. So sánh Map - Reduce - For/While
#### 4.1 Cách hoạt động
- Map: Áp dụng một hàm cho từng phần tử của iterable và trả về một iterable mới với các kết quả đã được xử lý.
- Reduce: Áp dụng một hàm để gộp các phần tử của iterable lại thành một giá trị duy nhất, thông qua việc kết hợp dần dần từng cặp phần tử.
- For/While: Dùng để lặp qua từng phần tử của iterable hoặc thực hiện một số thao tác lặp lại cho đến khi điều kiện thỏa mãn.
#### 4.2 Hiệu năng
- Map: Có thể nhanh hơn một chút so với vòng lặp for thông thường vì nó tối ưu hóa việc áp dụng hàm trên từng phần tử (tác vụ đơn giản).
- Reduce: Có thể tương đối nhanh nếu chỉ cần gộp các phần tử theo một cách đơn giản.
- For/While: Hiệu năng của vòng lặp `for` hoặc `while` có thể tương đương hoặc kém hơn đôi chút so với `map()`/`reduce()` do các bước lặp tường minh và thiếu tối ưu hóa.
#### 4.3 Khi nào sử dụng
- Map: Thích hợp khi bạn cần áp dụng một hàm cho mọi phần tử của một iterable và không muốn hoặc không cần quan tâm đến từng bước lặp một cách cụ thể.
- Reduce: Thích hợp khi bạn cần gộp các phần tử của một iterable lại thành một giá trị duy nhất, như tính tổng, tính tích, hoặc nối các chuỗi.
- For/While: Thích hợp cho bất kỳ tình huống nào, đặc biệt là khi bạn cần nhiều bước lặp khác nhau hoặc thực hiện các tác vụ phức tạp.

| **Tiêu chí**             | **`map()`**                                   | **`reduce()`**                               | **Vòng lặp `for`/`while`**                      |
|--------------------------|-----------------------------------------------|----------------------------------------------|------------------------------------------------|
| **Cách hoạt động**        | Áp dụng hàm lên từng phần tử của iterable     | Gộp dần các phần tử lại thành một giá trị    | Lặp qua từng phần tử, có thể thực hiện nhiều thao tác |
| **Mục đích**              | Chuyển đổi các phần tử trong iterable         | Gộp các phần tử thành một giá trị duy nhất   | Linh hoạt, có thể thực hiện bất kỳ thao tác nào trên phần tử |
| **Đầu ra**                | Iterable mới với các giá trị đã xử lý         | Một giá trị duy nhất                         | Iterable mới hoặc không có kết quả cụ thể       |
| **Số lượng đối số của hàm**| Một đối số                                    | Hai đối số                                  | Tuỳ thuộc vào nhu cầu, có thể không dùng hàm    |
| **Tính đọc được**         | Tốt cho các hàm đơn giản, khó đọc hơn với hàm phức tạp | Kém đọc hơn khi hàm phức tạp                 | Dễ hiểu, minh bạch                              |
| **Hiệu năng**             | Tối ưu hơn chút so với vòng lặp cho các thao tác đơn giản | Hiệu suất tốt cho tác vụ gộp đơn giản         | Hiệu năng tương đương hoặc kém hơn tùy thuộc vào thao tác |
| **Tính linh hoạt**        | Hạn chế, chỉ áp dụng một hàm lên từng phần tử | Hạn chế, chỉ gộp các phần tử                 | Rất linh hoạt, có thể thực hiện nhiều thao tác trong mỗi vòng lặp |
| **Tình huống sử dụng**    | Khi cần áp dụng cùng một hàm cho tất cả phần tử | Khi cần gộp các phần tử lại với nhau         | Thích hợp cho mọi tình huống, đặc biệt là các tác vụ phức tạp |
| **Ví dụ**                 | `map(lambda x: x*2, [1, 2, 3])`              | `reduce(lambda x, y: x+y, [1, 2, 3])`       | `for x in [1, 2, 3]: ...` hoặc `while condition:` |

### 5. Code so sánh tốc độ xử lý và bộ nhớ tiêu thụ
```python
import time
import tracemalloc
from functools import reduce
import matplotlib.pyplot as plt

# Hàm so sánh thời gian và bộ nhớ cho các phương pháp khác nhau
def compare_methods(iterable, repetitions=5):
    # Kết quả lưu thời gian và bộ nhớ sử dụng trung bình
    results = {
        'map': {'time': 0, 'memory': 0},
        'reduce': {'time': 0, 'memory': 0},
        'for_loop': {'time': 0, 'memory': 0}
    }

    for _ in range(repetitions):
        # Test map() với tổng các phần tử sau khi nhân đôi
        tracemalloc.start()
        start_time = time.time()
        map_result = sum(map(lambda x: x * 2, iterable))
        end_time = time.time()
        memory_map, _ = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        results['map']['time'] += (end_time - start_time) / repetitions
        results['map']['memory'] += memory_map / repetitions

        # Test reduce() với tổng các phần tử sau khi nhân đôi
        tracemalloc.start()
        start_time = time.time()
        reduce_result = reduce(lambda x, y: x + (y * 2), iterable, 0)
        end_time = time.time()
        memory_reduce, _ = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        results['reduce']['time'] += (end_time - start_time) / repetitions
        results['reduce']['memory'] += memory_reduce / repetitions

        # Test for loop với tổng các phần tử sau khi nhân đôi
        tracemalloc.start()
        start_time = time.time()
        loop_result = 0
        for x in iterable:
            loop_result += x * 2
        end_time = time.time()
        memory_loop, _ = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        results['for_loop']['time'] += (end_time - start_time) / repetitions
        results['for_loop']['memory'] += memory_loop / repetitions

    return results

# Hàm để vẽ biểu đồ so sánh
def visualize_results(results):
    methods = list(results.keys())
    times = [results[method]['time'] for method in methods]
    memories = [results[method]['memory'] for method in methods]

    # Tạo hai biểu đồ cột cho thời gian và bộ nhớ
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Vẽ biểu đồ thời gian
    ax1.bar(methods, times, color='lightblue')
    ax1.set_title('Thời gian chạy của các phương pháp')
    ax1.set_ylabel('Thời gian (giây)')

    # Vẽ biểu đồ bộ nhớ
    ax2.bar(methods, memories, color='lightgreen')
    ax2.set_title('Bộ nhớ sử dụng của các phương pháp')
    ax2.set_ylabel('Bộ nhớ (bytes)')

    # Hiển thị biểu đồ
    plt.tight_layout()
    plt.show()

# Thử nghiệm với danh sách lớn và nhiều lần lặp
if __name__ == "__main__":
    test_data = list(range(100000))  # Sử dụng dữ liệu lớn hơn nếu cần
    repetitions = 10  # Số lần lặp lại mỗi phương pháp để tính trung bình
    comparison = compare_methods(test_data, repetitions)

    # In kết quả
    for method, metrics in comparison.items():
        print(f"{method} - Time: {metrics['time']}s, Memory: {metrics['memory']} bytes")

    # Vẽ biểu đồ trực quan hóa
    visualize_results(comparison)
```

![Biểu đồ so sánh](https://raw.githubusercontent.com/nananam98/CodeOptGuide/main/data/map_reduce.png)