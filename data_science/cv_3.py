import cv2

video = cv2.VideoCapture(r'C:\Users\ZAID\Videos\mantissa.xyz_loop_064.mp4')

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