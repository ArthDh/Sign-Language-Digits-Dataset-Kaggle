import numpy as np
import cv2

# TODO:
# Pass dataset through mask
# find convex hull
# Add background variation


class ImageGen:

    # Constants for finding range of skin color in YCrCb
    min_YCrCb = np.array([0, 133, 77], np.uint8)
    max_YCrCb = np.array([255, 173, 127], np.uint8)
    foreground_imgs = []
    background_imgs = []

    def __init__(self, foreground_imgs, background_imgs, n_imgs):
        self.foreground_imgs = foreground_imgs
        self.background_imgs = background_imgs
        self.n_imgs = n_imgs
        self.countoured_images = []

    def draw_countours():
        for img in self.foreground_imgs:
            contoured_image = img.copy()
            # Convert image to YCrCb
            imageYCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
            # Find region with skin tone in YCrCb image
            skinRegion = cv2.inRange(imageYCrCb, min_YCrCb, max_YCrCb)
            # Do contour detection on skin region
            img, contours, _ = cv2.findContours(skinRegion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            # Draw the contour on the source image
            for i, c in enumerate(contours):
                area = cv2.contourArea(c)
                if area > 1000:
                    cv2.drawContours(contoured_image, contours, i, (0, 0, 0))

            self.countoured_images.append(contoured_image)

    def mask_background():

    def add_background():
        pass

    def generate_images():
        pass
