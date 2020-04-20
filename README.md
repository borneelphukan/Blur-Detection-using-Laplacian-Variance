# Blur-Detector-using-OpenCV-Laplacian-Variance

## INTRODUCTION  

This mini computer vision project focuses on the use Laplacian Variance using OpenCV
to determine the level of blurriness of an input image. I'm setting a threshold value to state if an image is blurred or not blurred. 
By default, the threshold value of Laplacian Variance to label an image as blurred is 100. If the threshold value is less than 100, 
the image is classified as blurred and if it is greater than 100, it is classified as non-blurred.

OpenCV contains the Laplacian Kernel which is a pre-defined 3X3 matrix. This matrix slides through the image and returns the overall 
Laplacian Variance of the image.

## STEPS EXPLAINING THE STRUCTURE OF CLASSIFIER:

STEP 1: Import the libraries. 
Step 2: Set the input directory of the images. 
STEP 3: Set the threshold value (by default I've taken 100) 
STEP 4: Run a loop through every images in the directory. 
          i. Run the 3x3 Laplacian Kernel over the image. 
          ii. If the value received is less than threshold, 
                then, it is a blurred image. 
          iii. If the value received is more than threshold, 
                then, it is a non-blur image.
