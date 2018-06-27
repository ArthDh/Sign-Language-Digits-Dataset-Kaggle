import numpy as np
import cv2

# TODO:
# Pass dataset through mask
# find convex hull
# Add background variation


# Constants for finding range of skin color in YCrCb
min_YCrCb = np.array([0, 133, 77], np.uint8)
max_YCrCb = np.array([255, 173, 127], np.uint8)

cv2.namedWindow('Camera Output')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    temp = frame.copy()
    grayscaled = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
    # Convert image to YCrCb
    imageYCrCb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)

    # Find region with skin tone in YCrCb image
    skinRegion = cv2.inRange(imageYCrCb, min_YCrCb, max_YCrCb)

    # Do contour detection on skin region
    image, contours, _ = cv2.findContours(skinRegion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contour on the source image
    for i, c in enumerate(contours):
        area = cv2.contourArea(c)
        if area > 1000:
            cv2.drawContours(grayscaled, contours, i, (0, 0, 0), thickness=cv2.FILLED)

    ret, threshold = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)
    # Display the source image
    fin = cv2.cvtColor(threshold, cv2.COLOR_GRAY2BGR)
    cv2.imshow('Camera Output', fin)

    # Check for user input to close program
    keyPressed = cv2.waitKey(1)  # wait 1 milisecond in each iteration of while loop

cv2.destroyAllWindows()
cv2.release()
