import numpy as np
import cv2
import os
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc


webcam = cv2.VideoCapture(0)


video = VideoWriter('webcam.avi', VideoWriter_fourcc(*'MP42'), 25.0, (640, 480))


while True:
    # get the frame from the webcam
    stream_ok, frame = webcam.read()

    # if webcam stream is ok
    if stream_ok:
        cv2.imshow('Webcam', frame)

        video.write(frame)


    if cv2.waitKey(1) & 0xFF == 27: break


cv2.destroyAllWindows()
webcam.release()
video.release()



cam = cv2.VideoCapture("webcam.avi")

try:


    if not os.path.exists('data'):
        os.makedirs('data')


except OSError:
    print('Error: Creating directory of data')

currentframe = 1

while (True):

    ret, frame = cam.read()

    if ret:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        cropped_name='./data/cropped' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(name, frame)
        img = cv2.imread(name)
        cropped_image = img[0:640, 239:240]

        cv2.imwrite(cropped_name, cropped_image)

        currentframe += 1
    else:
        break

cam.release()
cv2.destroyAllWindows()

final_image = cv2.imread('data/cropped1.jpg')
for i in range (2,currentframe):
    path= 'data/cropped'+ str(i) + ".jpg"
    temporary=cv2.imread(path)
    final_image = np.concatenate((final_image, temporary), axis=1)

cv2.imwrite('PhotoFinish.jpg', final_image)
cv2.imshow('Photofinish',final_image)

cv2.waitKey(10000)