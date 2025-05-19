# Development Of Yolo Machine Learning Model And Real-time Streaming Operational Parameters Of CO2 Micro Algae Capture Pilot

<div style="text-align: center;">
  <img src="https://github.com/nguyen187/realtime-co2-algae-monitoring/blob/main/img/Overview_algae.png" width="800">
</div>


Xây dựng hệ thống truyền phát dữ liệu thời gian thực trên nền tảng điện toán đám mây Azure và ứng dụng học máy
và học sâu để tự động hóa quá trình theo dõi. Triển khai hai hệ thống truyền phát dữ
liệu thời gian thực bao gồm: hệ thống theo dõi và dự đoán nồng độ hóa chất AAA dựa trên tín
hiệu điện đo từ thiết bị Raman, sử dụng các công cụ lưu trữ và xử lý dữ liệu thời gian thực mạnh
mẽ trên hệ thống điện toán đám mây Azure; và hệ thống phát hiện bọt khí CO2, dự đoán trạng
thái sục khí hiện tại trong nuôi vi tảo, mọi dữ liệu sẽ được xử lý và trực quan hóa theo thời gian
thực.


## 1.  Kiểm soát bột khí  CO2 theo thời gian thực trên cloud

<div style="text-align: center;">
  <img src="https://github.com/nguyen187/realtime-co2-algae-monitoring/blob/main/img/yolo_component.png" width="800">
</div>


- Nồng độ và trạng thái của bọt khí CO2 ảnh hưởng trực tiếp đến hiệu suất chất lượng sản phẩm
- Giám sát bột khí CO2 là tiêu chí quan trọng trong quá trình sản xuất sản phẩm AAA 
 
<div style="text-align: center;">
  <img src="https://github.com/nguyen187/realtime-co2-algae-monitoring/blob/main/img/H1.png" width="800">
</div>


Hệ thống giám xác bao gồm:
- Camera của smart phone xử dụng để ghi nhận hình ảnh của bột khí
- Xây dựng mô hình Yolo sử dụng để tự động hóa việc giám xác nồng độ và trạng thái bột khí từ camera
- Xây dựng digital platform bao gồm Camera/Yolo model/Kafka/ Telegraf/InfluxDB/Grafana sử dụng để giám xác bột khí CO2 theo thời gian thực trên cloud
## 2. Kiểm soát nồng độ sản phẩm theo thời gian thực


<div style="text-align: center;">
  <img src="https://github.com/nguyen187/realtime-co2-algae-monitoring/blob/main/img/H2.png" width="800">
</div>



- Nồng độ sản phẩm (AAA) cần được giám xác thông qua thiết bị phân tích Raman theo gian thực trong suất quá trình sản xuất.
- Một mô hình máy học dùng để chuyển đổi tính hiệu phổ số Raman sang nồng độ sản phẩm.
 
Hệ thống giám xác bao gồm:
- Xây dựng mô hình máy học sử dụng để tự động hóa việc giám xác nồng độ sản phẩm từ dữ liệu số Raman
- Xây dựng digital platform bao gồm azure event hub, Databricks, Azure Machine Learning, Delta Lake, Azure Data Storage, Power BI sử dụng để giám xác bột nồng độ sản phẩm theo thời gian thực trên cloud 

## 3. Bộ dữ liệu:

Cài đặt thiết bị: 
- Ống thủy tinh trong suốt hình trụ: kích thước 10x40.
- Máy bơm: công suất 3.5w.
- Ống nhựa và các van dùng để điều chỉnh tốc độ.

Bộ dữ liệu:
- Bộ dữ liệu hơn 700 ảnh chụp bọt khí với kích thước 640x640 với hệ thống thiết bị được xây dựng như hình bên chia đều ở 3 trạng thái: yếu, bình thường và mạnh.
<div style="text-align: center;">
  <img src="https://github.com/nguyen187/realtime-co2-algae-monitoring/blob/main/img/dataset.png" width="800">
</div>



## 3. Kết quả huấn luyện mô hình:

<div style="text-align: center;">
  <img src="https://github.com/nguyen187/realtime-co2-algae-monitoring/blob/main/img/result.png" width="800">
</div>

<div style="text-align: center;">
  <img src="https://github.com/nguyen187/realtime-co2-algae-monitoring/blob/main/img/train_batch1.jpg" width="800">
</div>


## 4. Monitoring Application:
<div style="text-align: center;">
  <img src="https://github.com/nguyen187/realtime-co2-algae-monitoring/blob/main/img/application_yolo.png" width="800">
</div>


## Contact
For any questions or support, please reach out via thanhnguyen187201@gmail.com.
