import cv2, pandas, time, datetime


cap=cv2.VideoCapture(0)
while True:
    state, frame=cap.read()

    cv2.imshow('frame',frame)

    key=cv2.waitKey(1)
    if key==ord('q'):
        break
cap.release()
cv2.destroyAllWindows



