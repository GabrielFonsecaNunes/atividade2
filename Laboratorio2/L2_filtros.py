import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def plot_blur(img):
    """
    """
    img_blur = cv.blur(img, (3, 3))
    fig, (ax1, ax2)= plt.subplots(nrows=1, ncols=2)
    plt.title("Original vs Blur", loc = "center")
    ax1.imshow(img)
    ax1.set_title("Original")
    ax2.imshow(img_blur)
    ax2.set_title("Blur")
    plt.show()


def plot_gaussian_blur(img):
    """
    
    """
    img_blurg = cv.GaussianBlur(img, (3, 3), 0)
    fig, (ax1, ax2)= plt.subplots(nrows=1, ncols=2)
    plt.title("Original vs Blur Fitro Gaussiano", loc = "center")
    ax1.imshow(img)
    ax1.set_title("Original")
    ax2.imshow(img_blurg)
    ax2.set_title("Blur Fitro Gaussiano")
    plt.show()


def plot_median_blur(img):
    """
    Plota Filtro mediano
    Args:
        img (img)
    """
    img_blurmedian = cv.medianBlur(img, 5)
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
    plt.title("Original vs Blur Fitro Mediano", loc = "center")
    ax1.imshow(img)
    ax1.set_title("Original")
    ax2.imshow(img_blurmedian)
    ax2.set_title("Blur Fitro Mediano")
    plt.show()

def plot_bilateral_filter(img):
    """
    Plota Filtro Bilateral
    """
    img_blurbl = cv.bilateralFilter(img, 9, 75, 75)
    fig, (ax1, ax2)= plt.subplots(nrows=1, ncols=2)
    plt.title("Original vs Blur Fitro Bilateral", loc = "center")
    ax1.imshow(img)
    ax1.set_title("Original")
    ax2.imshow(img_blurbl)
    ax2.set_title("Blur Fitro Bilateral")
    plt.show()

# Caminho da Imagem
path_img = "./Laboratorio2/messi5.jpg"

# Leitura da Imagem
img = cv.imread(path_img)

# Verificando se a imagem existe
assert img is not None, "file not could be read"