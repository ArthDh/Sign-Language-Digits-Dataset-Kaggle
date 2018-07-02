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

    def draw_contours(self):
        for img in self.foreground_imgs:
            ogi_img = cv2.imread(img)

            rows, cols, channels = ogi_img.shape
            print(rows, cols, channels)
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
            bg_img = cv2.imread(self.background_imgs[0])
            bg_img = bg_img[0:rows, 0:cols]

            bg_mask = cv2.bitwise_not(masked_img)

            bg_img = cv2.bitwise_and(bg_img, bg_img, mask=bg_mask)

            temp = img_no_bg + bg_img

            # Display image with no bg
            cv2.imshow('Countoured: ', temp)
            # Check for user input to close program
            keyPressed = cv2.waitKey(1)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def mask_background(self):
        pass

    def add_background(self):
        pass

    def generate_images(self):
        pass


if __name__ == '__main__':

    hand_images = []
    background_imgs = []

    h1_path = "/Users/arth/Desktop/ML/projects/Sign Language/Dataset/test/0/IMG_4069.JPG"
    b1_path = "/Users/arth/Desktop/backgroud_ds/banded_0008.JPG"
    hand_images.append(h1_path)
    background_imgs.append(b1_path)

    imgen = ImageGen(hand_images, background_imgs, 1)
    imgen.draw_contours()
