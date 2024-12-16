import cv2
import numpy as np

# 读入图像
img = cv2.imread('C:/Users/PHB/Desktop/new4/Scan_0005.jpg', cv2.IMREAD_GRAYSCALE)

# 计算梯度
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
cv2.imwrite('C:/Users/PHB/Desktop/new4/1.png', sobelx)
cv2.imwrite('C:/Users/PHB/Desktop/new4/2.png', sobely)

# 水平方向
horizontal = cv2.convertScaleAbs(sobelx)
_, thresh = cv2.threshold(horizontal, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
eroded = cv2.erode(thresh, kernel, iterations=1)
dilated = cv2.dilate(eroded, kernel, iterations=1)
lines_h = cv2.HoughLinesP(dilated, 1, np.pi/180, 100, minLineLength=500, maxLineGap=10)

# 竖直方向
vertical = cv2.convertScaleAbs(sobely)
_, thresh = cv2.threshold(vertical, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
eroded = cv2.erode(thresh, kernel, iterations=4)
dilated = cv2.dilate(eroded, kernel, iterations=4)
lines_v = cv2.HoughLinesP(dilated, 1, np.pi/180, 40, minLineLength=40, maxLineGap=8)

# 绘制水平方向直线
for line in lines_h:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 2)

# 绘制竖直方向直线
for line in lines_v:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 2)

# 保存图像
cv2.imwrite('C:/Users/PHB/Desktop/new4/table_without_grid.png', img)
