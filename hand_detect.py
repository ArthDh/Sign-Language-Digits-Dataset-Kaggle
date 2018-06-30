import numpy as np
import cv2

# TODO:
# Pass dataset through mask - completed
# find convex hull - completed
# Add background variation


# Constants for finding range of skin color in YCrCb
min_YCrCb = np.array([0, 133, 77], np.uint8)
max_YCrCb = np.array([255, 173, 127], np.uint8)


frame = cv2.imread('')
temp = frame.copy()
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
        cv2.drawContours(temp, contours, i, (0, 0, 0))

# Display the source image
cv2.imshow('test', temp)

# Check for user input to close program
keyPressed = cv2.waitKey(1)  # wait 1 milisecond in each iteration of while loop
cv2.waitKey(0)
cv2.destroyAllWindows()
