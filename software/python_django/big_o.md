## Độ phức tạp của giải thuật

### 1. Big O
#### 1.1 Phân loại độ phức tạp (thường gặp)
- O(1) - Constant Time: Thời gian thực thi không thay đổi, bất kể kích thước đầu vào.
- O(log n) - Logarithmic Time: Thời gian thực thi tăng theo logarithm của kích thước đầu vào.
- O(n) - Linear Time: Thời gian thực thi tăng tỷ lệ thuận với kích thước đầu vào.
- O(n log n) - Log-linear Time: Phổ biến trong các giải thuật sắp xếp hiệu quả.
- O(n^2) - Quadratic Time: Thời gian thực thi tăng theo bình phương của kích thước đầu vào.
- O(2^n) - Exponential Time: Thời gian thực thi tăng theo hàm mũ của kích thước đầu vào.
- O(n!) - Factorial Time: Thời gian thực thi tăng theo giai thừa của kích thước đầu vào.

#### 1.2 Các bước xác định độ phức tạp
- Bước 1: Xác định các phép tính cơ bản
Đầu tiên, hãy xem xét các phép toán hoặc hoạt động cơ bản mà giải thuật thực hiện như gán giá trị, so sánh, vòng lặp, v.v.

- Bước 2: Phân tích từng phần của giải thuật
Xem xét từng bước hoặc khối lệnh của giải thuật và đánh giá tần suất thực hiện các phép toán trong mỗi phần.

- Bước 3: Tính tổng số phép tính
Dựa trên phân tích ở bước 2, tổng hợp tất cả các phép tính cơ bản để có một biểu thức biểu diễn thời gian hoặc không gian sử dụng.

- Bước 4: Tối giản biểu thức
Loại bỏ các hạng tử ít quan trọng (thường là các hạng tử có cấp thấp hơn khi đầu vào lớn) và chỉ giữ lại các hạng tử có ảnh hưởng lớn nhất đến độ phức tạp.

- Bước 5: Biểu diễn dưới dạng Big-O
Biểu thức cuối cùng sẽ được biểu diễn dưới dạng ký hiệu Big-O để mô tả độ phức tạp thời gian hoặc không gian của giải thuật.

#### 1.3 Ví dụ minh hoạ
Tìm phần tử lớn nhất trong mảng
```python
def find_max(arr):
    max_value = arr[0]  # O(1)
    for num in arr:      # O(n)
        if num > max_value:  # O(1)
            max_value = num  # O(1)
    return max_value     # O(1)

```

### 2. Bài toán cụ thể
#### 2.1 Yêu cầu bài toán
Tìm tất cả các biến thể của sản phẩm dựa trên các thuộc tính (không giới hạn thuộc tính) như khối lượng, màu sắc, và cách đóng gói,...
Đây là bài toán thực tế gặp trong dự án LHE, khi mà các product được chia thành nhiều formula và mỗi formula là 1 biến thể của việc kết hợp từng phần tử của thuộc tính lại với nhau.

#### 2.2 Cách giải quyết
Thông thường, khi gặp bài toán này cách dễ nhất để giải quyết là dùng các vòng for lồng nhau liên tục, ví dụ:
```python
# Dữ liệu mẫu
weights = [f"{i}kg" for i in range(1, 21)]  # 20 khối lượng
colors = [f"Màu {i}" for i in range(1, 11)]  # 10 màu sắc
packagings = [f"Loại {i}" for i in range(1, 6)]  # 5 cách đóng gói
materials = [f"Chất liệu {i}" for i in range(1, 4)]  # 3 loại chất liệu
origins = [f"Xuất xứ {i}" for i in range(1, 4)]  # 3 xuất xứ


# Phương pháp Sử dụng các vòng for lồng nhau
def generate_variations_loop():
    variations = []
    for weight in weights:
        for color in colors:
            for packaging in packagings:
                for material in materials:
                    for origin in origins:
                        variation = (weight, color, packaging, material, origin)
                        variations.append(variation)
    return variations
```
Phương pháp này có độ phức tạp là O(n), vì số lượng vòng lặp tỷ lệ thuận với số lượng các biến thể được tạo ra (trong ví dụ trên sẽ tạo ra 9000 biến thể khác nhau)

Tới đây, tạm thời chúng ta có thể chấp nhận vì độ phức tạp dừng ở mức tuyến tính O(n). Tuy nhiên sẽ gặp khó khăn nếu số lượng thuộc tính không cố định (yêu cầu bài toán), và để sử lý vấn đề này có thể sẽ khiến thuật toán phức tạp hơn nữa. Vì vậy hoàn toàn có thể biến đổi và tối ưu tiếp để giảm thời gian và không gian cần sử dụng, đáp ứng được tiêu chí số lượng thuộc tính không có định mà không làm thay đổi độ phức tạp của thuật toán.

Ý tưởng ở đây là sẽ tận dụng kiểu dữ liệu `tuple`, có không gian cần sử dụng ít hơn `list`. Sau đó sẽ zip các phần tử theo từng cặp, lưu trữ chúng tạm thời trong cache.
```python
import functools

# Tập hợp các thuộc tính
attributes = [weights, colors, packagings, materials, origins]

# Sử dụng bộ nhớ cache để lưu kết quả trung gian
@functools.lru_cache(maxsize=None)
def combine_two_attributes_cached(attr1, attr2):
    return [(x + (y,)) for x in attr1 for y in attr2]

# Phương pháp tối ưu: Kết hợp zip với lru_cache và generator
def combine_all_attributes_optimized(attributes):
    # Bắt đầu với thuộc tính đầu tiên dưới dạng tuple để tối ưu bộ nhớ
    combined_result = tuple([(item,) for item in attributes[0]])
    
    # Lần lượt kết hợp với các thuộc tính tiếp theo, sử dụng generator để tối ưu bộ nhớ
    for attr in attributes[1:]:
        combined_result = combine_two_attributes_cached(tuple(combined_result), tuple(attr))
    
    return combined_result
```

Đây là biểu đồ so sánh 2 phương pháp trên
![big_o_1](https://raw.githubusercontent.com/nananam98/CodeOptGuide/main/data/big_o_1.png)

![big_o_2](https://raw.githubusercontent.com/nananam98/CodeOptGuide/main/data/big_o_2.png)
