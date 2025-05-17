from ultralytics import YOLO

# Bước 1: Tải mô hình YOLOv8 từ tệp .pt
model = YOLO('./models/model.pt')

# Bước 2: Xuất mô hình sang định dạng ONNX
model.export(format='onnx', opset=12, dynamic=True)