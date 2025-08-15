import cv2 as cv
import sys 

img = cv.imread('3142.jpg')
cv.imshow('display image', img)
cv.imwrite('copy.jpg', img)

stream = cv.VideoCapture(0)

if not stream.isOpened():
    print('wtf something went wrong bro')
    exit()

fps = stream.get(cv.CAP_PROP_FPS)
width = int(stream.get(3))
height = int(stream.get(4))

output = cv.VideoWriter('assets/4_stream.mp4', 
                        cv.VideoWriter_fourcc('m', 'p', '4', 'v'),
                        fps=fps, frameSize=(width, height))


while(True):
    ret, frame = stream.read()
    if not ret:
        print('Brah again sth wrong wtf')
        break 
    
    frame = cv.resize(frame, (width, height))
    output.write(frame)
    cv.imshow('Webcam!', frame)
    if cv.waitKey(1) == ord('q'):
        break

stream.release()
cv.destroyAllWindows()