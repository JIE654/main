import os
import random
import shutil

# 文件夹路径和分配比例
dir_path = "C:/Users/PHB/Desktop/pure4zData"
ratios = [5/6, 1/6]  # 按照6:2:2的比例分配

# 获取文件名列表并打乱
file_names = os.listdir(dir_path)
random.shuffle(file_names)

# 按比例分成几份
num_files = len(file_names)
num_train = int(num_files * ratios[0])
num_test = int(num_files * ratios[1])

# 分别处理每份文件名列表
train_names = file_names[:num_train]
test_names = file_names[num_train:]


# 将每份文件名列表移动到对应文件夹
for name_list, folder_name in zip([train_names, test_names], ['train', 'test']):
    folder_path = os.path.join(dir_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    for name in name_list:
        src_path = os.path.join(dir_path, name)
        dst_path = os.path.join(folder_path, name)
        shutil.move(src_path, dst_path)
