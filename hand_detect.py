import numpy as np
import os
import cv2
import shutil

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

    def __init__(self, foreground_imgs, background_imgs, n_imgs, path):
        self.foreground_imgs = foreground_imgs  # Pass handsign(i)
        self.background_imgs = background_imgs  # Pass dtd
        self.n_imgs = n_imgs  # Number of images to generate
        self.countoured_images = []  # Storing generated images
        self.path = path

    def get_random_sign(self):
        index = np.random.randint(len(self.foreground_imgs) - 1)
        return self.foreground_imgs[index]

    def get_random_bg(self):
        index = np.random.randint(len(self.background_imgs) - 1)
        return self.background_imgs[index]

    def set_path(path):
        self.path = path

    def get_images(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)

        for i in range(self.n_imgs):

            img_path = self.get_random_sign()
            bg_img_path = self.get_random_bg()

            ogi_img = cv2.imread(img_path)
            rows, cols, channels = ogi_img.shape
            # Copies of original image
            contoured_image = ogi_img.copy()
            copy_image = ogi_img.copy()

            # Convert image to YCrCb
            imageYCrCb = cv2.cvtColor(copy_image, cv2.COLOR_BGR2YCR_CB)
            # Find region with skin tone in YCrCb image
            skinRegion = cv2.inRange(imageYCrCb, self.min_YCrCb, self.max_YCrCb)
            # Do contour detection on skin region
            masked_img, contours, _ = cv2.findContours(skinRegion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Image no background
            img_no_bg = cv2.bitwise_and(ogi_img, ogi_img, mask=masked_img)

            # Background image
            bg_img = cv2.imread(bg_img_path)
            bg_img = bg_img[0:rows, 0:cols]

            bg_mask = cv2.bitwise_not(masked_img)

            bg_img = cv2.bitwise_and(bg_img, bg_img, mask=bg_mask)

            rows_bg, cols_bg, _ = bg_img.shape

            if(rows == rows_bg and cols == cols_bg):
                temp = img_no_bg + bg_img
                cv2.imwrite("{}/{}.jpg".format(self.path, i), temp)
            else:
                print("Shape error?")
