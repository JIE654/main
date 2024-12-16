import os
import cv2
import numpy as np

# 设置图片文件夹路径
folder_path = r'C:/Users/PHB/Desktop/new4/'

# 获取文件夹内所有图片的文件名
img_files = os.listdir(folder_path)

for img_file in img_files:
    # 读入图像
    img = cv2.imread(os.path.join(folder_path, img_file), 0)

    # 将图像转为灰度图像
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 应用二值化
    _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)


    # 应用膨胀操作
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(thresh, kernel, iterations=1)



    # # 检测表格线
    lines = cv2.HoughLinesP(dilated, 1, np.pi/180, 100, minLineLength=500, maxLineGap=10)

    # 判断是否带有网格线
    if len(lines) > 220:
        # 绘制表格线
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

        # 消除表格线
        kernel = np.ones((3, 3), np.uint8)
        img = cv2.erode(img, kernel, iterations=1)

        # 保存带网格线的图片
        cv2.imwrite(os.path.join(folder_path, 'table_with_grid_' + img_file), img)
        print("有网格线")

    else:
        # 保存不带网格线的图片
        cv2.imwrite(os.path.join(folder_path, 'table_without_grid_' + img_file), img)
        print("无网格线")