import cv2, pandas, time, datetime
first_frame=None
status_list=[None, None]
times=[]
df=pandas.DataFrame(columns=['Start','End'])

cap=cv2.VideoCapture(0)
while True:
    state, frame=cap.read()
    status=0
    grey_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    grey_frame=cv2.GaussianBlur(grey_frame,(21,21),0)
    if first_frame is None:
        first_frame=grey_frame
        continue
    delta_frame=cv2.absdiff(first_frame, grey_frame)
    thresh_delta=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_delta=cv2.dilate(thresh_delta, None, iterations=0)
    cnts=cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour):
            continue
        x,y,w,h=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x+y),(x+w,y+h),(0,255,0),3)
    cv2.imshow('frame',frame)
    cv2.imshow('capturing',grey_frame)
    cv2.imshow('delta',delta_frame)
    cv2.thresh('thresh',thresh_delta)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
cap.release()
cv2.destroyAllWindows



