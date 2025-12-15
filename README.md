# 🚗 Ultra-Accuracy Driver Drowsiness Detection System

An advanced **real-time driver drowsiness detection system** using:  

**YOLOv5 + SORT Tracking + Temporal Smoothing + EMA Bounding Boxes + Robust Alarm Logic**

Designed for **high accuracy, low false alarms**, and **real-world deployment readiness**.

---

## 📌 Features

✅ Real-time face & drowsiness detection  
✅ YOLOv5 custom-trained model  
✅ SORT multi-object tracking  
✅ Temporal confidence smoothing  
✅ EMA bounding box stabilization  
✅ Sustained-frame alarm logic (no false alerts)  
✅ Multi-person support  
✅ Works directly on webcam feed  
✅ Clean Jupyter Notebook implementation  

---

## 🧠 System Architecture

The system follows a modular real-time pipeline for **accuracy, stability, and low false alarms**.

### 🔄 Workflow Diagram


### 🧩 Component Details

**1️⃣ Webcam Input**  
- Captures real-time video frames via OpenCV  
- Supports live monitoring in real-world environments  

**2️⃣ YOLOv5 Detection Model**  
- Custom-trained YOLOv5 detects: `Awake` / `Drowsy`  
- High confidence threshold reduces noisy detections  

**3️⃣ SORT Tracker**  
- Maintains unique ID per detected face  
- Enables multi-driver tracking  
- Ensures temporal consistency across frames  

**4️⃣ EMA Bounding Box Smoothing**  
- Applies Exponential Moving Average to bounding boxes  
- Eliminates flickering, improves clarity  

**5️⃣ Temporal Confidence Smoothing**  
- Sliding window of recent frames  
- Computes average drowsiness confidence per driver  
- Prevents instant false classifications  

**6️⃣ Sustained Frame Alarm Logic**  
- Alarm triggers only if drowsiness persists for consecutive frames  
- Combines confidence threshold + consecutive-frame validation  

**7️⃣ Alarm System**  
- Real-time beep using `winsound`  
- Runs on a separate thread to avoid FPS drop  
- Automatically resets when driver becomes alert  

**8️⃣ Real-Time Visualization**  
- Displays smoothed bounding boxes + driver ID + status  
- Color-coded: 🟢 Awake, 🔴 Drowsy  

---

## 🧪 Dataset Used

- **Images**: Collected from your own webcam dataset  
- **Classes**: `Awake` and `Drowsy`  
- **Dataset Structure**:

## 🎯 Installation & Setup

1. Clone YOLOv5 repo:

```bash
git clone https://github.com/ultralytics/yolov5.git
cd yolov5

pip install -r requirements.txt

pip install opencv-python torch numpy sort-python

jupyter notebook Driver_Drowsiness_Detection.ipynb
