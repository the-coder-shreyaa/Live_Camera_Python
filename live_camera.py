import cv2
import cv2.data
import os
classifier =cv2.CascadeClassifier(cv2.data.haarcascades +  "/" +"haarcascade_frontalface_default.xml")
#data_path=cv2.data.haarcascades + "/"+ model_name
#modal=cv2.CascadeClassifier(data_path)

cam = cv2.VideoCapture(0)
#cv2.waitKey(0)
while True:
    status,frame=cam.read()
    if not status:
        print("camera is not working:")
        break
    faces= classifier.detectMultiScale(frame,1.3,5)
    print(faces)
    
    for face in faces:
        x1=face[0]
        y1=face[1]
        x2=x1+face[2]
        y2=y1+face[3]
        cv2.rectangle(frame,[x1,y1],[x2,y2],[255,0,0],2)
    cv2.imshow("Face",frame)
    if cv2.waitKey(1) == ord ("q"):
        break
cam.release()
cv2.destroyAllWindows()
        

