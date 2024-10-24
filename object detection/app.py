from ultralytics import YOLO
import cv2
import cvzone
import math
cap=cv2.VideoCapture("people.mp4")
model=YOLO('../Yolo-Weights/yolov8n.pt')
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]
while True:
    success,img=cap.read()
    results=model(img,stream=True)
    for i in results:
        boxes=i.boxes
        for j in boxes:
            #idhu bounding box kaaga
            x1,y1,x2,y2=j.xyxy[0]
            x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
            w,h=x2-x1,y2-y1
            #print(x1,y1,x2,y2)
            #cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
            #idhu confidence podradhuku
            cvzone.cornerRect(img,(x1,y1,w,h),)
            conf=math.ceil(j.conf[0]*100)/100
            #cvzone.putTextRect(img,f'{conf}',(max(0,x1),max(35,y1)))
            #idhu class Name kaga
            cls=int(j.cls[0])
            cvzone.putTextRect(img,f'{classNames[cls]} {conf}',(max(0,x1),max(35,y1)))
    cv2.imshow("cv",img)
    cv2.waitKey(0)