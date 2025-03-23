# 💳🔒 Bank Transaction Using Face Recognition

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-brightgreen)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-CNN-red)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Security](https://img.shields.io/badge/Security-High-critical)

---

## 📖 Overview
The **Bank Transaction Using Face Recognition System** is a secure and efficient application designed to enhance banking security by utilizing **facial recognition for user authentication**. This system replaces traditional authentication methods like passwords and PINs with advanced **biometric verification**.

### 🎯 Objective
- Provide a secure method for authenticating users during banking transactions.
- Enhance user experience by replacing PINs and passwords with **facial recognition**.
- Improve transaction security using **Deep Learning and Real-Time Face Detection**.

---

## 💡 Motivation
Traditional banking methods using PINs and passwords are vulnerable to theft and misuse. By implementing a **face recognition-based authentication system**, this project aims to enhance security and ensure only the authorized user can perform transactions.

---

## 🛠️ Technologies Used
- **Python:** Core language for backend implementation and video processing.
- **OpenCV:** Real-time facial detection and recognition using Haar Cascade Classifier.
- **Deep Learning (CNN):** Feature extraction for identifying registered faces accurately.
- **SQLite:** Database for securely storing user details and transaction records.
- **Flask:** Web framework to provide a simple and efficient user interface.
- **SMTP:** Sending transaction confirmation emails.

---

## ✨ Key Features
- 👤 **Face Authentication:** Uses CNN models to compare live facial features with pre-registered data.
- 📸 **Real-Time Face Detection:** Utilizes OpenCV’s Haar Cascade Classifier for accurate facial recognition.
- 🔒 **Secure Database:** Stores user details and transaction history securely in SQLite.
- 📧 **Transaction Confirmation:** Sends an email to the registered user confirming each transaction.
- 💻 **User-Friendly Interface:** Provides a simple, intuitive web interface for easy transactions.

---

## 📌 Outcome
- Successfully authenticated users and processed banking transactions with **high accuracy**.
- Reduced the risk of unauthorized access by using biometric authentication.
- Provided a smooth transaction process with a user-friendly interface.
- Published Paper: [Read on IEEE Xplore](https://ieeexplore.ieee.org/document/10060800)

---

## 🔍 Working
### Face Detection
- Captures live video using the webcam and detects facial features using the **Haar Cascade Classifier**.
- Converts images to grayscale for faster processing and more accurate recognition.

### Face Recognition
- Matches the detected face against a pre-registered database using a **CNN model** trained for feature extraction.
- If authenticated, allows the user to proceed with the transaction.

### Transaction Workflow
1. The user logs in via a web interface.
2. The system captures the user’s face and matches it against the pre-registered dataset.
3. If authenticated, the user can proceed with the transaction by entering details such as amount and recipient.
4. A confirmation email is sent to the registered email address via **SMTP**.

---

## 📊 Results
- Achieved a high level of security with **98% accuracy** in face recognition.
- Improved user experience by eliminating the need for passwords or PINs.
- Published at **IEEE Xplore - IIHC’22**: [Read the Paper](https://ieeexplore.ieee.org/document/10060800)

---

## 🔮 Future Work
- 🔗 **Integration with Mobile Applications:** Allowing users to perform transactions through mobile devices.
- 🔒 **Enhanced Security:** Implementing anti-spoofing techniques to avoid unauthorized access via photos or videos.
- 🚀 **Multi-Modal Authentication:** Combining facial recognition with other biometric techniques like fingerprint recognition for even higher security.

---

## 📁 Repository Structure
