

import  cv2

def video():
    cap=cv2.VideoCapture('video.mp4')
    
    
    if (cap.isOpened()== False):
        print("error ")
    while (cap.isOpened()):
        ret, frame=cap.read()
        if ret == True:
            cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.imshow('frame', frame)
            
            if cv2.waitKey(25)==ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

           
    