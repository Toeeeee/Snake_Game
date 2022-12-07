# **Các giao thức trong mạng Internet**

## **Giao thức HTTP**


**1. Giới thiệu chung về HTTP**

- Hypertext Transfer Protocol (Giao thức truyền siêu văn bản) là giao thức căn bản sử dụng trong việc trao đổi thông tin giữa máy khách và máy chủ web.
- Giao thức tầng ứng dụng của Web.
- Mô hình **client/server**
    - Client: Trình duyệt (brower) yêu cầu, nhận (sử dụng giao thức HTTP) và hiển thị các đối tượng Web.
    - Server: Máy chủ Web gửi (sử dụng giao thức HTTP) các đối tượng đáp ứng theo yêu cầu.
    

![markdown](http://3.bp.blogspot.com/-5LzAAr6VSWU/U51ZfCEka-I/AAAAAAAAAFg/yYxPUkzbok8/s1600/11.PNG) 
*Hình 1: Mô hình client/server*
- HTTP sử dụng TCP
    - Client khởi tạo kết nối TCP tới server port **80**
    - Server chấp nhận kết nối TCP từ client 
    - Thông điệp HTTP được trao đổi giữa trình duyệt (HTTP client) và máy chủ Web (HTTP server)
    
**2. Kết nối HTTP**
- Có 2 loại kết nối **HTTP**:
    + Kết nối không bền vững 
    + Kết nối bền vững

2.1 Kết nối không bền vững

