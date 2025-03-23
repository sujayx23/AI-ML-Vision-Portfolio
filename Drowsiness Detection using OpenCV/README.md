# 🚗💤 Real-Time Drowsiness Detection System using OpenCV

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-brightgreen)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-CNN-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📖 Overview
The **Real-Time Drowsiness Detection System** is an AI-powered application designed to enhance driver safety by monitoring facial expressions and detecting signs of fatigue. By analyzing the driver's **blink rate, yawning frequency, and facial features**, the system can promptly trigger alerts, reducing the risk of road accidents due to drowsiness. 

🎯 **Objective:**  
- Detect drowsiness in drivers using computer vision and deep learning techniques.
- Provide real-time alerts to improve road safety.

## 🧰 Technologies Used
- **Python:** Core language for algorithm implementation and video processing.
- **OpenCV:** Facial detection, tracking eye movements, and extracting key facial features (eyes, mouth).
- **Deep Learning (CNN):** Analysis of facial features to identify drowsiness based on blinking rate and yawning frequency.

---

## ✨ Key Features
- ✅ **Real-time Drowsiness Detection:** Continuously captures and analyzes live video streams to detect fatigue.
- 👁️ **Facial Feature Extraction:** Identifies eyes, mouth, and eyebrows to monitor blinking patterns and yawning frequency.
- 🔔 **Alert Mechanism:** Triggers immediate alerts when signs of drowsiness are detected.
- 💡 **Robustness:** Works efficiently under various lighting conditions and different head positions.
- 📈 **Accuracy:** Achieved 97% accuracy in detecting drowsy drivers across multiple real-world scenarios.

---

## 📌 Outcome
- Successfully detected drowsiness in real-time with **97% accuracy**.
- Enhanced robustness for different lighting conditions and angles.
- Documented and published in **IEEE Xplore at ICESC’21**. [Read the Paper](https://ieeexplore.ieee.org/document/9532758)

---

## 🔍 Technical Details
### Facial Detection with OpenCV
- Utilizes **pre-trained Haar Cascade classifiers** to detect the face and eyes from real-time video streams.
- Tracks facial landmarks to monitor blinking and yawning behavior.

### Drowsiness Detection Algorithm
- Calculates **blink rate and yawning frequency** to determine driver fatigue.
- Works effectively in real-world scenarios by analyzing continuous video streams.

### Real-World Testing
- Tested on live video feeds to ensure accurate performance.
- Achieved high accuracy even under **varied lighting conditions** and **head positions**.

### Alert System
- Provides both **audio and visual alerts** when signs of drowsiness are detected.
- Designed for immediate intervention to improve driver safety.

---

## 🚀 Challenges Overcome
- **Lighting Variations:** Adapted to bright sunlight and low-light environments.
- **Head Angles:** Accurate detection even when the face is not directly facing the camera.
- **Real-Time Processing:** Optimized for live performance, ensuring timely alerts.

---

## 🔮 Future Work
- 🔗 **Integration with Car Systems:** Embedding the model into car infotainment or safety systems for immediate driver feedback.
- 📊 **Multi-Factor Drowsiness Detection:** Incorporating head position, vehicle speed, and road conditions for comprehensive monitoring.

---

## 📁 Repository Structure
