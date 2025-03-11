# import the necessary packages
import sys
from playsound import playsound
from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import imutils
import time
import face_recognition
import cv2

def eye_aspect_ratio(eye):
    # compute the euclidean distances between the two sets of
    # vertical eye landmarks (x, y)-coordinates
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    # compute the euclidean distance between the horizontal
    # eye landmark (x, y)-coordinates
    C = dist.euclidean(eye[0], eye[3])

    # compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)

    # return the eye aspect ratio
    return ear

def play_alarm():
    playsound("Alert1.mp3")
  
#initializing the variables
count=0
ear_ratio=0.25
timing=60

# start the video stream thread
print("[INFO] starting video stream thread...")
# vs = FileVideoStream(args["video"]).start()
# fileStream = True
vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
fileStream = False
time.sleep(1.0)

# loop over frames from the video stream
while True:
    
    # if this is a file video stream, then we need to check if
    # there any more frames left in the buffer to process
    if fileStream and not vs.more():
        break

    # grab the frame from the threaded video file stream, resize
    # it, and convert it to grayscale
    # channels)
    frame = vs.read()
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #getting face landmarks
    face_mark=face_recognition.face_landmarks(frame)
    for i in face_mark:
        
            left_eye=i["left_eye"]
            right_eye=i["right_eye"]
            left_eye_points=np.array(left_eye)
            right_eye_points=np.array(right_eye)
            cv2.polylines(frame,[left_eye_points],True,(100,250,0),1)
            cv2.polylines(frame,[right_eye_points],True,(100,250,0),1)

            #calculating ear ratio
            left_ear=eye_aspect_ratio(left_eye)
            right_ear=eye_aspect_ratio(right_eye)
            ear=(left_ear+right_ear)/2
            

    #checking ear
            if(ear<ear_ratio):
                    
                    count+=1
                    if(count>=timing):
                            play_alarm()
                            cv2.putText(frame,"ALERT",(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,250),2)
            else:
                
                    count=0
    cv2.putText(frame,"EAR: %.2f"%ear,(310,20),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,250),2)
    # show the frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
 
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
sys.exit()
