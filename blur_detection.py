from imutils import paths
import argparse
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True)
args = vars(ap.parse_args())

threshold = 100

for imagePath in paths.list_images(args["images"]):
    
    image = cv.imread(imagePath)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    focus_measure = cv.Laplacian(image, cv.CV_64F).var()
    text = "Not Blur"
    
    if focus_measure < threshold:
        text = "Blur Image "

    cv.putText(image, "{}: {:.2f}".format(text, focus_measure),(30, 30), cv.FONT_ITALIC, 1.0, (0, 184, 50), 5)
    cv.imshow("Image", image)
    key = cv.waitKey(0)
