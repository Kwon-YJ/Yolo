# keras_yoloV3_fixed

* original : https://github.com/experiencor/keras-yolo3
## usage
* 1: conda create --name keras367 python="3.6.7"
* 2: https://pjreddie.com/media/files/yolov3.weights <- get weights
* 3: python yolo3_one_file_to_detect_them_all.py -w yolov3.weights -i dog.jpg

## What has changed?
* in yolo3_one_file_to_detect_them_all.py
    + +import sys
    + +img_file = 'dog_detected.jpg'
    + +img = cv2.imread(img_file)
    + +cv2.imshow('Result', img)
    + +cv2.waitKey()
    + +cv2.destroyAllWindows()
    + np.set_printoptions(threshold=np.nan) => np.set_printoptions(threshold=sys.maxsize)

* in requirements.txt
    + +pillow==7.2.0
    + +matplotlib==3.0.3
    + -tensorboard==1.15.0
    + Keras==2.3.1 => Keras==2.2.0
    + tensorflow==1.15.0 => tensorflow==1.6.0
