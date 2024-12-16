import cv2
import numpy as np
import os

# 图像文件夹路径
folder_path = 'C:/Users/PHB/Desktop/withoutgrid/'
output_folder = 'C:/Users/PHB/Desktop/results/'

# 循环处理每张图片
for file_name in os.listdir(folder_path):
    if file_name.endswith('.jpg'):
        # 读取图像
        img = cv2.imread(os.path.join(folder_path, file_name), 0)

        # 全局阈值化
        ret, thresh = cv2.threshold(img, 155, 255, cv2.THRESH_BINARY)

        # 定义结构元素，可以根据需要调整大小和形状
        kernel = np.ones((1, 1), np.uint8)

        # 进行开运算操作，先进行腐蚀，再进行膨胀
        opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

        # 保存图像
        result_path = os.path.join(output_folder, file_name)
        cv2.imwrite(result_path, thresh)






