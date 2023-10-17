from ultralytics import YOLO

#load model
model = YOLO("yolov8n.yaml")#v8n (nano)

#use model
results = model.train(data="config.yaml",epochs=3)
