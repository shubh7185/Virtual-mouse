import cv2
import numpy as np
import time
import autopy
import HandTracking as ht

# Variables Declaration
pTime = 0               # Used to calculate frame rate
width = 640             # Width of Camera
height = 480            # Height of Camera
frameR = 100            # Frame Rate
smoothening = 8         # Smoothening Factor
prev_x, prev_y = 0, 0   # Previous coordinates
curr_x, curr_y = 0, 0   # Current coordinates

cap = cv2.VideoCapture(0)   # Getting video feed from the webcam
cap.set(3, width)           # Adjusting size
cap.set(4, height)

detector = ht.handDetector(maxHands=1)                  # Detecting one hand at max
screen_width, screen_height = autopy.screen.size()      # Getting the screen size

# Initialize previous frame
prev_frame = None

while True:
    success, img = cap.read()
    img = detector.findHands(img)                       # Finding the hand
    lmlist, bbox = detector.findPosition(img)           # Getting position of hand

    # Read frame from webcam for motion detection
    ret, frame = cap.read()

    if len(lmlist)!=0:
        x1, y1 = lmlist[8][1:]
        x2, y2 = lmlist[12][1:]

        fingers = detector.fingersUp()      # Checking if fingers are upwards
        cv2.rectangle(img, (frameR, frameR), (width - frameR, height - frameR), (255, 0, 255), 2)   # Creating boundary box
        if fingers[1] == 1 and fingers[2] == 0:     # If fore finger is up and middle finger is down
            x3 = np.interp(x1, (frameR,width-frameR), (0,screen_width))
            y3 = np.interp(y1, (frameR, height-frameR), (0, screen_height))

            curr_x = prev_x + (x3 - prev_x)/smoothening
            curr_y = prev_y + (y3 - prev_y) / smoothening

            autopy.mouse.move(screen_width - curr_x, curr_y)    # Moving the cursor
            cv2.circle(img, (x1, y1), 7, (255, 0, 255), cv2.FILLED)
            prev_x, prev_y = curr_x, curr_y

        if fingers[1] == 1 and fingers[2] == 1:     # If fore finger & middle finger both are up
            length, img, lineInfo = detector.findDistance(8, 12, img)

            if length < 40:     # If both fingers are really close to each other
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()    # Perform Click

    # Convert frame to grayscale for motion detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    # If previous frame exists
    if prev_frame is not None:
        # Compute absolute difference between current frame and previous frame
        frame_delta = cv2.absdiff(prev_frame, gray)
        
        # Threshold the delta image to find regions of significant change
        thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
        
        # Dilate the thresholded image to fill in holes
        thresh = cv2.dilate(thresh, None, iterations=2)
        
        # Find contours of the objects
        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Iterate through detected contours
        for contour in contours:
            # If the contour area is too small, ignore it
            if cv2.contourArea(contour) < 1000:
                continue
            
            # Draw a bounding box around the detected object
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Show the frames
    cv2.imshow("Image", img)
    
    # Store current frame as previous frame for next iteration
    prev_frame = gray
    
    # Calculate and display frame rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    
    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
