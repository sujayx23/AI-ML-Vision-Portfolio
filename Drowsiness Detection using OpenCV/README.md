# 🚗💤 Real-Time Drowsiness Detection System using OpenCV

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-brightgreen)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-CNN-red)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Accuracy](https://img.shields.io/badge/Accuracy-97%25-green)

---

## 📖 Overview
The **Real-Time Drowsiness Detection System** is an AI-powered application designed to enhance driver safety by continuously monitoring facial expressions and detecting signs of fatigue. This system aims to **reduce road accidents and improve driver safety** by triggering alerts when drowsiness is detected.

### 🎯 Objective
- Prevent accidents caused by drowsiness by providing **real-time alerts**.
- Monitor driver behavior through **blink rate, yawning frequency, and facial expressions**.

---

## 💡 Motivation
With thousands of accidents occurring every year due to driver fatigue, this project aims to reduce road accidents by providing a reliable, cost-effective, and easy-to-implement drowsiness detection system.

---

## 🛠️ Technologies Used
- **Python:** Core programming language for the implementation.
- **OpenCV:** Used for facial detection, tracking eye movements, and extracting key facial features.
- **Deep Learning (CNN):** Applied to analyze facial features like eye aspect ratio (EAR) to detect drowsiness.
- **Dlib Library:** Utilized for facial landmark detection.

---

## ✨ Key Features
- ✅ **Real-time Drowsiness Detection:** Continuously captures and processes video to detect drowsiness instantly.
- 👁️ **Facial Feature Extraction:** Detects and monitors blinking and yawning patterns using eye aspect ratio (EAR).
- 🔔 **Alert Mechanism:** Triggers alarms when drowsiness is detected.
- 🌙 **Lighting Adaptability:** Works effectively under various lighting conditions (bright light & low light).
- 🔄 **Head Position Tolerance:** Detects drowsiness even when the driver’s face is not perfectly aligned with the camera.

---

## 📊 Results
- Achieved an impressive **97% accuracy** in detecting drowsy drivers across various test scenarios.
- Successfully handled **different lighting conditions** and **various head positions**.
- Published Paper: [Read on IEEE Xplore](https://ieeexplore.ieee.org/document/9532758)

---

## 🔍 Working
1. **Capture Video Input:** Continuously captures video frames from a camera.
2. **Face Detection:** Uses OpenCV and Dlib to detect the driver’s face and key facial landmarks.
3. **Eye Aspect Ratio (EAR):** Measures the distance between the eyes to detect blinking patterns.
4. **Yawning Detection:** Tracks the mouth opening ratio to detect potential drowsiness.
5. **Triggering Alerts:** Issues an alarm when drowsiness is detected (EAR below 0.25 for 6 seconds).

---

## 📁 Repository Structure
