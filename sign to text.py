
import os
import time  # to use the break in images
import uuid  # to name image files
import cv2

images_path='Tensorflow\workspace\images\collected images'
labels=['hello','thanks','yes','no','sorry']
number_imgs=15

for label in labels:
    os.mkdir ('Tensorflow\workspace\images\collected images\\'+label)
    cap=cv2.VideoCapture(0)
    print('collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret,frame=cap.read()
        imgname=os.path.join(images_path,label,label + '.' + '{}.jpg'.format(str(uuid.uuid1()))) # for each image has unique name
        cv2.imwrite(imgname,frame) #to write image name in the directory
        cv2.imshow('frame',frame)   #to show it on the screen
        time.sleep(2)
                                              # cv2.waitKey(0) == ord('q')   #would have also worked
        if cv2.waitKey(0) & 0xFF == ord('q'): # when both will be true then it will break means if in infinite time we will press 'q' it will break the loop
            break                             # if wait key was 1 then it would wait for 1 ms for pressing of q that's why 0 was showing still images and 1 was showing a video
    cap.release() # for delay between different labels

    #for labelling
    # just install labelImg as (pip install labelImg ) and now for using it just write labelImg in cmd 