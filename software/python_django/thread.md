## Single Threaded, Multi Threaded and Multi Processing

### 1. Giới thiệu
Thread: Là đơn vị nhỏ nhất của xử lý trong một ứng dụng. Mỗi thread có thể thực hiện một công việc cụ thể và chia sẻ tài nguyên với các thread khác trong cùng một quá trình.

### 2. Lập trình đơn luồng (Single-threaded)
#### 2.1 Định nghĩa
Chương trình chạy với một luồng duy nhất, tất cả các tác vụ được thực hiện tuần tự.

#### 2.2 Ưu điểm
- Dễ dàng triển khai và quản lý.
- Không cần quan tâm đến vấn đề đồng bộ hóa dữ liệu giữa các luồng.

#### 2.3 Nhược điểm
- Không tận dụng được khả năng của CPU đa nhân.
- Khi gặp tác vụ nặng (I/O-bound hoặc CPU-bound), chương trình có thể trở nên chậm chạp.

### 3. Lập trình đa luồng (Multi-threaded)
#### 3.1 Định nghĩa
Chương trình chạy với nhiều luồng cùng lúc, cho phép thực hiện nhiều tác vụ đồng thời.

#### 3.2 Ưu điểm
- Tận dụng tốt hơn khả năng của CPU đa nhân.
- Cải thiện hiệu suất đối với các tác vụ I/O-bound.

#### 3.3 Nhược điểm
- Phức tạp hơn trong việc triển khai và quản lý.
- Cần quan tâm đến vấn đề đồng bộ hóa dữ liệu giữa các luồng (sử dụng lock, semaphore...).

### 4. Python và Global Interpreter Lock (GIL)
- GIL: Là một mutex trong Python, đảm bảo rằng chỉ một thread có thể thực thi mã Python tại một thời điểm.
- Với các tác vụ CPU-bound, GIL có thể làm giảm hiệu suất của lập trình đa luồng.
- Với các tác vụ I/O-bound, lập trình đa luồng vẫn có thể cải thiện hiệu suất vì thread có thể chuyển đổi trong lúc chờ I/O.

### 5. Khi nào sử dụng?
Như đã trình bày ở trên, với sự ảnh hưởng của Golbal Interpreter Lock (GIL), chúng ta cần phân tích để sử dụng multi-threaded đúng ngữ cảnh

#### 5.1 Hiệu quả của Multi-threading trong Python với GIL
- Tác vụ CPU-bound: Là những tác vụ tiêu tốn nhiều tài nguyên CPU, như tính toán phức tạp, xử lý dữ liệu lớn, mã hóa/giải mã.  
Trong trường hợp này, GIL làm giảm hiệu quả của multi-threading vì nó chỉ cho phép một thread thực thi mã Python tại một thời điểm. Điều này có nghĩa là bạn không thể tận dụng được toàn bộ khả năng của CPU đa nhân.
- Tác vụ I/O-bound: Là những tác vụ liên quan đến việc chờ đợi I/O (như đọc/ghi file, truy vấn cơ sở dữ liệu, gửi/nhận dữ liệu mạng).  
Với các tác vụ này, thời gian chờ I/O chiếm phần lớn thời gian thực hiện, do đó, các thread khác có thể chuyển đổi và tiếp tục thực hiện các tác vụ khác trong khi một thread đang chờ I/O. Điều này giúp cải thiện hiệu suất của chương trình.

### 6. Giải pháp thay thế cho các tác vụ CPU-bound
#### 6.1 Multi-processing
Multi-processing là một kỹ thuật lập trình trong đó một chương trình được phân chia thành nhiều process (quá trình) chạy song song. Mỗi process có không gian bộ nhớ riêng và không bị ảnh hưởng bởi GIL, cho phép tận dụng tối đa CPU đa nhân.

- Tận dụng CPU đa nhân: Vì mỗi process có GIL riêng, chúng có thể chạy song song trên các nhân CPU khác nhau.
- An toàn hơn về mặt đồng bộ hóa: Mỗi process có không gian bộ nhớ riêng, giảm thiểu rủi ro xung đột dữ liệu so với threading.
- Chi phí tạo process cao: Việc tạo một process mới tốn nhiều tài nguyên hơn so với tạo một thread.
- Giao tiếp giữa các process phức tạp: Việc chia sẻ dữ liệu giữa các process cần thông qua cơ chế IPC (Inter-Process Communication), có thể phức tạp hơn so với chia sẻ dữ liệu giữa các thread.

#### 6.2 Asyncio
Asyncio là một module trong Python hỗ trợ lập trình bất đồng bộ (asynchronous programming) bằng cách sử dụng `coroutines`. Asyncio rất hiệu quả cho các tác vụ I/O-bound vì nó cho phép một tác vụ khác chạy trong khi chờ một tác vụ I/O hoàn thành mà không cần tạo thread hoặc process mới.

- Hiệu quả cho tác vụ I/O-bound: Asyncio cho phép xử lý nhiều tác vụ I/O-bound đồng thời mà không cần tốn tài nguyên cho thread hoặc process.
- Nhẹ nhàng hơn so với threading và processing: Không cần chi phí tạo và quản lý thread/process.
- Không tận dụng được CPU đa nhân cho tác vụ CPU-bound: Asyncio không vượt qua được GIL, nên không phù hợp cho các tác vụ CPU-bound nặng.
- Độ phức tạp cao hơn: Lập trình bất đồng bộ có thể khó hiểu và khó debug hơn so với lập trình đồng bộ.

| Đặc điểm                | Single-threaded                    | Multi-threaded                       | Multi-processing                     | Asyncio                               |
|-------------------------|------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
| **Khả năng đồng thời**  | Không                              | Có, nhưng bị giới hạn bởi GIL        | Có                                   | Có, bằng cách sử dụng async/await     |
| **Tận dụng CPU đa nhân**| Không                              | Không hiệu quả với CPU-bound (GIL)   | Có, mỗi process có GIL riêng         | Không                                 |
| **Phù hợp với tác vụ**  | Đơn giản, tuần tự                  | I/O-bound, tác vụ cần nhiều chờ I/O  | CPU-bound nặng                       | I/O-bound                             |
| **Chi phí tạo và quản lý**| Thấp                              | Trung bình                           | Cao                                  | Thấp                                  |
| **Đồng bộ hóa dữ liệu** | Không cần                           | Cần (lock, semaphore)                | Không cần (có không gian bộ nhớ riêng)| Không cần                             |
| **Độ phức tạp**         | Thấp                               | Trung bình                           | Cao                                  | Trung bình đến cao                    |
| **Giao tiếp dữ liệu**   | Trực tiếp                          | Trực tiếp, nhưng cần đồng bộ hóa     | Phức tạp (IPC)                       | Trực tiếp, sử dụng await/gather       |
| **Phù hợp với ứng dụng**| Ứng dụng đơn giản                  | Ứng dụng có nhiều tác vụ I/O         | Ứng dụng cần xử lý song song thực sự | Ứng dụng mạng, web, xử lý nhiều I/O   |

Giả sử 1 tiến trình chạy trên lý thuyết mất 2 giây, biểu đồ sau đây thể hiện kết quả.  
![thread](https://raw.githubusercontent.com/nananam98/CodeOptGuide/main/data/thread.png)

Giả sử tất cả các phương pháp cùng gọi 1 api 100 lần, biểu đồ sau đấy thể hiện kết quả.  
![thread_api](https://raw.githubusercontent.com/nananam98/CodeOptGuide/main/data/thread_api.png)