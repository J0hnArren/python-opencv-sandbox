import cv2
import os

import numpy as np


def sharpening(image):
    """Пример увеличения резкости на изображении"""
    kernel = np.array([[0, 0, 0],
                       [0, 2, 0],
                       [0, 0, 0]]) - \
             np.array([[1, 1, 1],
                       [1, 1, 1],
                       [1, 1, 1]]) / 9
    return cv2.filter2D(src=image, ddepth=-1, kernel=kernel)


def box_filter(image):
    """Бокс фильтр в общем виде"""
    w = 5
    kernel = np.ones((w, w)) / ((w + 1)*(w + 1))
    return cv2.filter2D(src=image, ddepth=-1, kernel=kernel)


def gaussian_filter(image):
    """
    Пример Гауссова фильтра.

    Здесь:
    ksize - размер kernel (окна фильтрации)

    The final two arguments are sigmaX and sigmaY, which are both set to 0.
    These are the Gaussian kernel standard deviations, in the X (horizontal) and Y (vertical) direction.
    The default setting of sigmaY is zero. If you simply  set sigmaX to zero, then the standard deviations are computed
    from the kernel size (width and height respectively). You can also explicitly set the size of each argument to
    positive values greater than zero.
    """
    return cv2.GaussianBlur(src=image, ksize=(5, 5), sigmaX=0, sigmaY=0)


def custom_linear_filter(image):
    """Пример кастомного линейного фильтра из лекции (по факту это лапласиан гауссиана)"""
    kernel = np.array([[0, 0, -1, 0, 0],
                       [0, -1, -2, -1, 0],
                       [-1, -2, 16, -2, -1],
                       [0, -1, -2, -1, 0],
                       [0, 0, -1, 0, 0]])
    return cv2.filter2D(src=image, ddepth=-1, kernel=kernel, borderType=cv2.BORDER_DEFAULT)


def median_filter(image):
    """Медианный фильтр. ksize - размер стороны квадрата окна"""
    return cv2.medianBlur(src=image, ksize=5)


def main():
    src_img = cv2.imread("./data/cross_0256x0256.png", cv2.IMREAD_GRAYSCALE)
    if src_img is None:
        print('Could not read image')
        exit(1)
    # images = read_dataset("./data/other", cv2.IMREAD_GRAYSCALE)
    # write_dataset("./output/other", images, "grayscale")

    dst1 = sharpening(src_img)
    dst2 = box_filter(src_img)
    dst3 = gaussian_filter(src_img)
    dst4 = custom_linear_filter(src_img)
    dst5 = median_filter(src_img)
    res = cv2.hconcat([src_img, dst1, dst2, dst3, dst4, dst5])
    cv2.namedWindow("result", cv2.WINDOW_NORMAL)
    cv2.imshow("result", res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("./output/result.png", res)


if __name__ == "__main__":
    main()
