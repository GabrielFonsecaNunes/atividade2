import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def apply_blur(img):
    """
    Args:
        img (np.Array):
    """
    return cv.blur(img, (3, 3))

def apply_gaussian_blur(img):
    """
    Args:
        img (np.Array):
    """
    return cv.GaussianBlur(img, (3, 3), 0)

def apply_median_blur(img):
    """
    Plota Filtro mediano
    Args:
        img (np.Array):
    """
    return cv.medianBlur(img, 5)

def apply_bilateral_filter(img):
    """
    Filtro Bilateral
    Args:
        img (np.Array):
    """
    return cv.bilateralFilter(img, 9, 75, 75)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Display the resulting frame
    cv.imshow('Original', frame)

    # Display the resulting frame
    cv.imshow('Blur', apply_blur(frame))

    # Display the resulting frame
    cv.imshow('Gaussian Filter', apply_gaussian_blur(frame))
    
    # Display the resulting frame
    cv.imshow('Median Filter', apply_median_blur(frame))
    
    # Display the resulting frame
    cv.imshow('Bilateral Filter', apply_bilateral_filter(frame))

    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
