import sys
import time
import cv2
import random
from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision
from robot.motor import Robot  # Import Robot from the motor module

# Configuration variables
MODEL_NAME = 'converted_edgetpu/model_edgetpu.tflite'
MAX_RESULTS = 3
SCORE_THRESHOLD = 0.0
NUM_THREADS = 4
ENABLE_EDGETPU = True
CAMERA_ID = 0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Initialize the robot
robot = Robot()

# print(1)


def run():
    # Initialize the image classification model
    base_options = core.BaseOptions(file_name=MODEL_NAME, use_coral=ENABLE_EDGETPU, num_threads=NUM_THREADS)
    classification_options = processor.ClassificationOptions(max_results=MAX_RESULTS, score_threshold=SCORE_THRESHOLD)
    options = vision.ImageClassifierOptions(base_options=base_options, classification_options=classification_options)
    classifier = vision.ImageClassifier.create_from_options(options)

    random_direction = None
    
    # Values like F,R,L
    direction = "F"

    # Start capturing video input from the camera
    cap = cv2.VideoCapture(CAMERA_ID)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    # Continuously capture images from the camera and run inference
    while cap.isOpened():
        # print(3)
        success, image = cap.read()
        if not success:
            sys.exit('ERROR: Unable to read from webcam. Please verify your webcam settings.')

        image = cv2.flip(image, 1)

        # Convert the image from BGR to RGB as required by the TFLite model.
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        tensor_image = vision.TensorImage.create_from_array(rgb_image)
        categories = classifier.classify(tensor_image)

        print(categories)
        # Control the robot based on classification results
        for idx, category in enumerate(categories.classifications[0].categories):
            class_index = category.index
            print(class_index)
            if class_index == 1:  # Blocked
                random_direction = None
                if direction != "F":
                    direction = "F"
                    robot.forward()
            elif class_index == 0:  # Free
                if random_direction is None:
                    random_direction = random.choice(["left", "right"])
                if random_direction == "left":
                    if direction != "L":
                        direction = "L"
                        robot.left()
                else:
                    if direction != "R":
                        direction = "R"
                        robot.right()
            break
        
        # Stop the program if the ESC key is pressed.
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    # cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        # print(2)
        run()
    except Exception as e:
        print("An Error occured: ", str(e))
    finally:
        # Clean up GPIO pins on program exit
        robot.cleanup() 
