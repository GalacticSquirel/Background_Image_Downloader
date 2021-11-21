# import the necessary packages
from skimage.metrics import structural_similarity as compare_ssim
import argparse
import imutils
import cv2
import os
def compare(imageA,imageB):
    # construct the argument parse and parse the arguments
    # load the two input images
    # convert the images to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    # compute the Structural Similarity Index (SSIM) between the two
    # images, ensuring that the difference image is returned
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    cv2.waitKey(0)
    return ("SSIM: {}".format(score))
for image in os.listdir("images"):
    print(image)
    i = 0
    image_list = os.listdir("images")
    image1 = cv2.imread(image)
    for image in image_list:
        print(image)
        image2 = cv2.imread(image_list[i])
        print(compare(image1, image2))
        i += 1
    




