import cv2
import numpy as np
import urllib.request
import matplotlib.pyplot as plt

# Download the YOLOv4-tf model files from the official repository
cfg_url = "https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg"
weights_url = "https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights"
cfg_path = "yolov4-tiny.cfg"
weights_path = "yolov4-tiny.weights"
urllib.request.urlretrieve(cfg_url, cfg_path)
urllib.request.urlretrieve(weights_url, weights_path)

# Load the YOLOv4-tf model
net = cv2.dnn_DetectionModel(cfg_path, weights_path)
net.setInputSize(416, 416)
net.setInputScale(1.0 / 255)
net.setInputSwapRB(True)
class_names_path = r"C:\Users\Aman\Downloads\task\tensorflow-yolov4-tflite\data\classes\coco.names"
with open(class_names_path, "r") as f:
    class_names = f.read().strip().split("\n")

# Set the confidence threshold and non-maximum suppression threshold
conf_threshold = 0.5
nms_threshold = 0.3

def detect_objects(image):
    classes, confidences, boxes = net.detect(image, confThreshold=conf_threshold, nmsThreshold=nms_threshold)

    if len(classes) > 0:
        for class_id, confidence, box in zip(classes.flatten(), confidences.flatten(), boxes):
            label = f"{class_names[class_id]}: {confidence:.2f}"
            color = (0, 255, 0)
            x, y, w, h = box
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    return image


video_stream = cv2.VideoCapture(0)

while True:
    ret, frame = video_stream.read()
    if not ret:
        break

    frame = detect_objects(frame)

    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.show()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_stream.release()
cv2.destroyAllWindows()