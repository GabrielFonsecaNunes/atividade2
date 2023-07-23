import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def plot_blur(img, save=False):
    """
    Plota o original e o filtrado com o filtro Blur.

    Args:
        img (img): A imagem a ser filtrada.
        save (bool): Se True, salva a imagem filtrada.
    """
    img_blur = cv.blur(img, (3, 3))
    fig, (ax1, ax2)= plt.subplots(nrows=1, ncols=2)
    plt.title("Original vs Blur", loc = "center")
    ax1.imshow(img)
    ax1.set_title("Original")
    ax2.imshow(img_blur)
    ax2.set_title("Blur")
    if save:
        plt.savefig("Blur Media.jpg")
    plt.show()

def plot_gaussian_blur(img, save=False):
    """
    Plota o original e o filtrado com o filtro Gaussiano.

    Args:
        img (img): A imagem a ser filtrada.
        save (bool): Se True, salva a imagem filtrada.
    """
    img_blurg = cv.GaussianBlur(img, (3, 3), 0)
    fig, (ax1, ax2)= plt.subplots(nrows=1, ncols=2)
    plt.title("Original vs Blur Fitro Gaussiano", loc = "center")
    ax1.imshow(img)
    ax1.set_title("Original")
    ax2.imshow(img_blurg)
    ax2.set_title("Blur Fitro Gaussiano")
    if save:
        plt.savefig("FiltroGaussiano.jpg")
    plt.show()

def plot_median_blur(img, save=False):
    """
    Plota o original e o filtrado com o filtro Mediano.
    Args:
        img (img): A imagem a ser filtrada.
        save (bool): Se True, salva a imagem filtrada.
    """
    img_blurmedian = cv.medianBlur(img, 5)
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
    plt.title("Original vs Blur Fitro Mediano", loc = "center")
    ax1.imshow(img)
    ax1.set_title("Original")
    ax2.imshow(img_blurmedian)
    ax2.set_title("Blur Fitro Mediano")
    if save:
        plt.savefig("FiltroMediano.jpg")
    plt.show()

def plot_bilateral_filter(img, save=False):
    """
    Plota o original e o filtrado com o filtro Bilateral.
    Args:
        img (img): A imagem a ser filtrada.
        save (bool): Se True, salva a imagem filtrada.
    """
    img_blurbl = cv.bilateralFilter(img, 9, 75, 75)
    fig, (ax1, ax2)= plt.subplots(nrows=1, ncols=2)
    plt.title("Original vs Blur Fitro Bilateral", loc = "center")
    ax1.imshow(img)
    ax1.set_title("Original")
    ax2.imshow(img_blurbl)
    ax2.set_title("Blur Fitro Bilateral")
    if save:
        plt.savefig("Bilateral.jpg")
    plt.show()


# Caminho da Imagem
path_img = rf".\atividade2\Laboratorio2\messi5.jpg"

# Leitura da Imagem
img = cv.imread(path_img)

# Verificando se a imagem existe
assert img is not None, "file not could be read"

plot_blur(img, save= True)
plot_gaussian_blur(img, save= True)
plot_median_blur(img, save= True)
plot_bilateral_filter(img, save= True)