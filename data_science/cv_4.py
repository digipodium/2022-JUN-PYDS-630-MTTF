import cv2

video = cv2.VideoCapture(0) # 0 = webcam
while video.isOpened():
    status, img = video.read()
    if status:

        cv2.imshow('video', img)
        
        if cv2.waitKey(1) == 27: # 27 = esc key
            break
    else:
        print('video ended')
        break

video.release()
cv2.destroyAllWindows()