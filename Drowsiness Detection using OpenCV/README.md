# Drowsiness Detection with OpenCV

**Objective**:  
The project aimed to build an automated real-time driver drowsiness detection system that can analyze the driver’s facial expressions and identify signs of fatigue. The system triggers an alert if the driver shows symptoms of drowsiness, helping to reduce road accidents and improve driver safety.

**Technologies Used**:
- **Python**: Core programming language used for implementing the detection algorithm and processing video input.
- **OpenCV**: Utilized for facial detection, tracking eye movements, and extracting key facial features such as eyes and mouth to monitor blinking and yawning.
- **Deep Learning**: A Convolutional Neural Network (CNN) was applied to analyze facial features and identify drowsiness based on behavior patterns like blink rate and yawning frequency.

**Key Features**:
- **Real-time drowsiness detection**: The system continuously captures video of the driver, processing frames in real-time to assess drowsiness.
- **Facial feature extraction**: Using OpenCV, the system detects key facial landmarks such as eyes, mouth, and eyebrows. It tracks blinking patterns and yawning frequency as primary indicators of drowsiness.
- **Alert mechanism**: Once the system identifies potential signs of fatigue, it sends an immediate alert to the driver to raise awareness and encourage them to take a break.
- **Robustness**: The system is designed to work in various lighting conditions and angles, ensuring that it works well in real-world driving environments.

**Outcome**:  
The drowsiness detection system achieved an impressive **97% accuracy** in detecting drowsy drivers across various tests. This high level of accuracy helps to effectively mitigate the risks associated with driver fatigue and prevent accidents caused by drowsiness.

**Published Paper**:  
The project was formally documented and published in **IEEE Xplore**, making it accessible to the wider academic and research community. You can read the paper detailing the methodology, algorithms, and testing procedures [here](https://ieeexplore.ieee.org/document/9532758).

**Technical Details**:
- **Facial Detection with OpenCV**: The system uses OpenCV to detect and track facial features. Specifically, it identifies the eyes and mouth to monitor for signs of drowsiness. The technology uses pre-trained Haar cascade classifiers for detecting the face and eyes in real-time video.
- **Drowsiness Detection Algorithm**: The system calculates the blink rate and monitors yawning frequency. Based on the rate at which the driver blinks and yawns, the system determines if the driver may be fatigued.
- **Real-World Testing**: The system was tested in real-world scenarios where a driver was filmed while driving. The system worked on live video streams, accurately identifying drowsiness behavior in various conditions.
- **Alert System**: When signs of drowsiness were detected, the system would trigger an alert, such as a sound or visual cue, to notify the driver. This helps mitigate the risks of falling asleep at the wheel.

**Challenges Overcome**:
- **Lighting Variations**: The system adapts to different lighting conditions, such as bright sunlight and low-light environments, ensuring its reliability in day and night driving.
- **Angles and Head Position**: The model is robust to variations in head position, allowing it to detect drowsiness even when the driver’s face is not directly facing the camera.
- **Real-Time Processing**: The algorithm is optimized for real-time performance, making it feasible for in-vehicle deployment where timely alerts are crucial.

**Future Work**:
- **Integration with Car Systems**: Future work could involve integrating this system directly into the car's infotainment or safety systems for immediate feedback to the driver.
- **Multi-Factor Drowsiness Detection**: Additional factors such as head position, vehicle speed, and road conditions could be integrated to provide a more comprehensive drowsiness detection model.

This project highlights the use of AI and computer vision to create a safer driving experience, utilizing deep learning and real-time processing to detect and alert drivers at risk of drowsiness.
