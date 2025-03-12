# Bank Transaction Using Face Recognition

**Objective**: This project aimed to develop a secure and efficient banking transaction system using facial recognition to authenticate users. The goal was to enhance security by ensuring only the authorized user can perform a transaction, eliminating the need for traditional passwords or PINs.

**Technologies Used**:
- **Python**: Programming language used for developing the system.
- **OpenCV**: Used for real-time facial detection and recognition.
- **Deep Learning**: Employed for face recognition, utilizing a Convolutional Neural Network (CNN) model for feature extraction.
- **SQLite**: Database used to store user details and transaction records.
- **Flask**: Web framework used to create the interface and interact with the backend.
- **SMTP (Simple Mail Transfer Protocol)**: Used for sending transaction confirmation emails to the user.

**Key Features**:
- **Face Authentication**: Users' faces are captured using a webcam, and their identity is verified against a pre-stored database of registered faces using deep learning models.
- **Real-Time Face Detection**: The system uses OpenCV’s Haar Cascade Classifier to detect and track facial features such as eyes and mouth, ensuring the accuracy of facial recognition.
- **Transaction Confirmation**: Upon successful authentication, the user can perform banking transactions. A confirmation email is sent automatically to the registered email address.
- **Secure Database**: User details and transaction records are stored securely in an SQLite database, ensuring privacy and ease of access.
- **User-Friendly Interface**: The web interface allows users to easily interact with the system, facilitating a smooth transaction process.

**Outcome**: The facial recognition system successfully authenticated users and processed banking transactions with high accuracy. By integrating deep learning for face recognition, the system added an extra layer of security to the banking process, reducing the risks associated with unauthorized transactions. The system demonstrated a user-friendly interface and effective performance in real-world conditions.

**Published Paper**: The project was published in **IEEE Xplore**. You can read the paper and access further details about the system and its implementation [here](https://ieeexplore.ieee.org/document/10060800).

**Detailed Description**:
- **Face Detection**: The system captures a video feed using a webcam and applies face detection techniques to locate the user’s face in real-time. The **Haar Cascade Classifier** identifies facial features such as eyes, nose, and mouth.
  
- **Face Recognition**: Once the face is detected, it is compared to a database of registered faces using deep learning models. If a match is found, the transaction proceeds. The CNN model used for face recognition was trained on a dataset of user images to improve accuracy.

- **Transaction Workflow**: 
    - **Step 1**: The user logs into the system via a simple web interface.
    - **Step 2**: The system captures the user's face and matches it against the pre-registered images.
    - **Step 3**: Upon successful identification, the user is allowed to enter transaction details (such as amount and recipient).
    - **Step 4**: After completing the transaction, a confirmation email is sent to the user's email address via SMTP.

- **Security Considerations**: The system ensures that only the registered user's face can authenticate and perform transactions. It also stores sensitive data, such as transaction details, securely in the SQLite database. The system is resistant to simple spoofing methods (like photos) due to the deep learning model's ability to recognize faces with high accuracy.

 **Publications**
 
 **IEEE Conference Publication**
 
 **Title:** Bank Transaction using Face Recognition
 
 **Conference:** IEEE Xplore at IIHC’22
 **Link:** https://ieeexplore.ieee.org/document/10060800
