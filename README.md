# Bài tập lớn môn Trí tuệ nhân tạo

## Chủ đề: Dự báo lượng mưa với dữ liệu trạm AWS và dữ liệu khí tượng ERA5

## Link báo cáo:
https://docs.google.com/document/d/1N4J3xOO6KkViWtYyUUc5QMprKPI1SdukEyWATJVS1J0

### Danh sách thành viên và phân công công việc

- Nguyễn Hùng Dũng (Nhóm trưởng):
  - Nghiên cứu, cài đặt, thử nghiệm và tối ưu mô hình Convolutional LSTM.
  - Thống kê kết quả thử nghiệm và viết báo cáo cho phần mô hình ConvLSTM.
  - Vẽ bản đồ mưa, viết báo cáo phần kết luận.
- Ngô Thành Minh:
  - Nghiên cứu, cài đặt, thử nghiệm và tối ưu mô hình LSTM cho dữ liệu ở dạng bảng.
  - Thống kê kết quả thử nghiệm và viết báo cáo cho phần mô hình LSTM.
- Nguyễn Hữu Phú:
  - Nghiên cứu, tìm hiểu 2 loại dữ liệu mưa trạm và dữ liệu khí tượng.
  - Hỗ trợ thống kê kết quả thực nghiệm.
  - Viết báo cáo phần mô tả bài toán và dữ liệu.
- Nguyễn Ngọc Tùng:
  - Đọc và xử lý dữ liệu, đưa dữ liệu dạng ảnh về dạng bảng.
  - Trực quan hóa dữ liệu mưa trạm.
- Diệp Xuân Linh:
  - Đọc và xử lý dữ liệu, đưa dữ liệu dạng ảnh về dạng bảng.
  - Viết báo cáo phần đọc dữ liệu, xử lý và thống kê dữ liệu

### Các file trong dự án

- read_img.py: Đọc dữ liệu dạng ảnh thàng bảng
- read_img_handing_null.py: Đọc dữ liệu dạng ảnh thàng bảng và fill dữ liệu null cho những điểm ảnh thiếu dữ liệu
- merge_data.py: Kết hợp các thuộc tính dữ liệu thành một bảng duy nhất
- renderChart.py: Trực quan hóa dữ liệu mưa AWS
- rainfall-lstm.ipynb: Notebook cài đặt mô hình LSTM phiên bản 1
- lstm-rainfaill-ai.ipynb: Notebook cài đặt mô hình LSTM phiên bản 2
- convlstm-predict-rainfall.ipynb: Notebook cài đặt mô hình ConvLSTM phiên bản 1
- convlstm-predict-3.ipynb: Notebook cài đặt mô hình ConvLSTM phiên bản 2
