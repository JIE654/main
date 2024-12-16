import cv2
import numpy as np
import os

# 图像文件夹路径
folder_path = 'E:/withoutgrid'
output_folder = 'E:/results'

# 循环处理每张图片
for file_name in os.listdir(folder_path):
    if file_name.endswith('.jpg'):
        # 读取图像
        img = cv2.imread(os.path.join(folder_path, file_name), 0)

        # 全局阈值化
        ret, thresh = cv2.threshold(img, 105, 255, cv2.THRESH_BINARY)
        cv2.imwrite("thresh.jpg", thresh)
        # 合并原图与阈值图
        combined = cv2.addWeighted(img, 0.2, thresh, 0.8, 0)
        cv2.imwrite("combined.jpg", combined)
        # 增强合并图片对比度和细节
        kernel = np.ones((3, 3), np.uint8) / 2
        combined = cv2.erode(combined, kernel, iterations=1)
        cv2.imwrite("combined2.jpg", combined)
        # 保存图像
        result_path = os.path.join(output_folder, file_name)
        cv2.imwrite(result_path, combined)
