# HUMAN-IDENTIFIER
#🚶‍♂️ YOLOv8 Human Identification and Object Detection

📌 Overview

This project demonstrates a real-time object detection model using YOLOv8 with a focus on identifying humans in video streams. The model efficiently detects multiple objects and annotates them with bounding boxes, confidence scores, and class names. This basic implementation is built using OpenCV, cvzone, and the YOLOv8 model to process frames from video input and provide human/object identification.

🌟 Features

• Human Detection: Identify and label humans in videos.
•	Multi-Class Object Detection: Detects multiple objects like cars, bicycles, animals, and more.
•	Real-Time Performance: Process video streams frame-by-frame.
•	Confidence Scores: Display the model’s confidence alongside each detected object.
•	Bounding Boxes with Annotations: Draw accurate boxes around objects for better visualization.


🛠️ Tech Stack

•	Python 3.x
•	OpenCV
•	cvzone
•	Ultralytics YOLOv8
•	YOLOv8n Weights

📂 Project Structure
📦 YOLOv8-Human-Identification
├── people.mp4             # Sample video for testing
├── yolov8n.pt             # Pre-trained YOLOv8 model weights
├── detect.py              # Main code for object detection
├── requirements.txt       # Dependencies
└── README.md              # Documentation


🔧 Installation and Setup

  1.	Clone the Repository
   git clone https://github.com/PRAVEENKUMAR-003/HUMAN-IDENTIFIER
   cd yolov8-human-identification

  2.	Install Dependencies
    pip install -r requirements.txt

  3.	Download YOLOv8 Weights
    Place the yolov8n.pt model file inside the project folder. You can download it from Ultralytics.

🚀 Usage

  1.	Run Detection on Sample Video
      python detect.py
  2.	Code Overview
      Here’s how the core logic works:
        •	Capture frames from the video using cv2.VideoCapture.
        •	Run object detection on each frame using YOLOv8’s stream mode.
        •	Draw bounding boxes and annotate detected objects with class names and confidence scores using cvzone.
  
  📈 Results and Visualization
        •	Bounding Boxes: Each detected object is enclosed in a rectangle.
        •	Confidence Levels: Displayed next to the detected object class.
        •	Real-Time Video Stream: Process video frames continuously until stopped.

  🤖 Future Improvements
        •	Add tracking for detected humans across multiple frames.
        •	Use GPU acceleration to improve real-time performance.
        •	Integrate custom datasets to enhance model performance for specific use cases.
        •	Build a web interface to run detections from a browser

  🤝 Contributing
        Contributions are welcome! Fork the repository, create a new branch, and open a pull request with your enhancements.
  
  🛡️ License
        This project is licensed under the MIT License – feel free to use it for personal or commercial applications.

