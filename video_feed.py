import cv2
from main import lane_pipeline #importing the function from the other file
cap = cv2.VideoCapture(0) #capturing video from the camera
while True:
    ret, frame = cap.read() #geting the frame 
    new_img = lane_pipeline(frame, show_roi = False, show_lane = True, display_curve = True) #getting the image with lane overlays drawn
    cv2.imshow(new_img) #displaying the image with the overlays
cap.release()
cv2.destroyAllWindows()
#https://stackoverflow.com/questions/37774354/opencv-python-real-time-image-frame-processing