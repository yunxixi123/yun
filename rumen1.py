from PIL import Image
import numpy as np

# 打开图像
image = Image.open('f.jpg')  # 将'your_image.jpg'替换为你的图像文件名

# 转换为numpy数组
image_matrix = np.array(image)
height, width, channels = image_matrix.shape
print(image_matrix[:, 1, 2])
# 打印高度、宽度和颜色通道数
# print(f"高度: {height}, 宽度: {width}, 颜色通道数: {channels}")
# # 查看矩阵
# print(image_matrix)
