import os
import cv2
import numpy as np
import time


image_dir = "E:/withoutgrid"
result_dir = "E:/results"

if not os.path.exists(result_dir):
    os.mkdir(result_dir)

image_name_list = os.listdir(image_dir)
image_num = len(image_name_list)
for i, image_name in enumerate(image_name_list):
    image_pathname_src = f"{image_dir}/{image_name}"
    image_pathname_dst = f"{result_dir}/{image_name}"
    img_src = cv2.imread(image_pathname_src, cv2.IMREAD_GRAYSCALE)
    ret, img_temp = cv2.threshold(img_src.copy(), 160,255, cv2.THRESH_BINARY)
    cv2.imwrite("1.jpg", img_temp)
    img_temp = 255 - img_temp
    cv2.imwrite("2.jpg", img_temp)
    num_objects, labels = cv2.connectedComponents(img_temp)
    print(num_objects)
    max_sum = 0
    start_time = time.time()
    for n in range(1, num_objects + 1):
        area = labels == n
        area = area.astype(np.uint8)
        s = area.sum()
        if s > max_sum:
            max_sum = s
            mask = area
    mask = mask * 255
    cv2.imwrite("3.jpg", mask)
    kernel = np.ones((4, 4), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)
    mask = mask / 255
    # cv2.imwrite("4.jpg", mask)
    img_temp = 255 - (255 - img_src) * (1 - mask)
    cv2.imwrite(image_pathname_dst, img_temp)
    cv2.imwrite("mask.jpg", mask*255)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"[{i + 1} / {image_num}] {image_name} ({elapsed_time:.2f}s)")




