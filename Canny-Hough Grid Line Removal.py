import cv2
import numpy as np
import os

# 获取当前工作目录下的所有jpg文件
image_path = 'C:/Users/PHB/Desktop/new4/'
images = [os.path.join(image_path, f) for f in os.listdir(image_path) if f.endswith('.jpg')]


# # 定义Canny边缘检测函数
# def canny(image, threshold1, threshold2):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     blur = cv2.GaussianBlur(gray, (5, 5), 0)
#     canny = cv2.Canny(blur, threshold1, threshold2)
#     return canny


# 遍历所有图片
for image_file in images:
    # 读入图像
    img = cv2.imread(image_file)

    # 应用Canny算法
    edges = cv2.Canny(img, 50, 150, apertureSize=3)

    # 应用膨胀操作，将边缘加粗
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(edges, kernel, iterations=1)

    # 检测表格线
    lines = cv2.HoughLinesP(dilated, 1, np.pi / 180, 100, minLineLength=500, maxLineGap=10)

    # 去除表格线
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)

    # 保存图像
    filename = os.path.splitext(os.path.basename(image_file))[0]
    cv2.imwrite(os.path.join(image_path, f"{filename}_no_grid.jpg"), img)
