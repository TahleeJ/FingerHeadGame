import cv2
import numpy as num
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

left_ear_cascade = cv2.CascadeClassifier('haarcascade_mcs_leftear.xml')

right_ear_cascade = cv2.CascadeClassifier('haarcascade_mcs_rightear')

cap = cv2.VideoCapture(0)

directions = []

mid_x = 320
mid_y = 240

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        mid_x = faces[0][0] + faces[0][2]/2
        mid_y = faces[0][1] + faces[0][3]/2
        print((mid_x, mid_y))
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
            # region of image
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
            for (ex, ey, ew, eh) in eyes:
                # print('x: {}, ex: {}'.format(x, ex))
                cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)

    else:
    #     print("oh")
        if mid_x < 302 and mid_x*0.7 < mid_y and mid_x*(0-0.7) > mid_y:
            print("right")
        elif mid_x < 345 and mid_x*0.7 > mid_y and mid_x*(0-0.7) < mid_y:
            print("left")
        elif mid_y < 207:
            print("up")
        elif mid_y > 237:
            print("down")

    # If i were to further implement this. I would utilize the ear cascade




    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
