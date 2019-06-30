import cv2
import numpy as np

# 读取一张四川大录古藏寨的照片.
img = cv2.imread('tiger_tibet_village.jpg')
print(img.shape)

# 缩放成200x200的方形图像.
# 等效于img_200x300 = cv2.resize(img, (300, 200)),注意指定大小的格式是（宽度，高度）.
img_200x200 = cv2.resize(img, (200, 200))
print(img_200x200.shape)

# 不直接指定缩放大小，通过fx和fy指定缩放比例，0.5则长度和宽度都为原来的一半.
# 插值方法默认是cv2.INTER_LINEAR，这里指定为最近邻插值.
img_200x300 = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5, interpolation = cv2.INTER_NEAREST)
print(img_200x300.shape)

# 在上张图片的基础上，上下各贴50像素的黑边，生成300x300的图像.
img_300x300 = cv2.copyMakeBorder(img, 50, 50, 0, 0, cv2.BORDER_CONSTANT, value = (0, 0, 0))
print(img_300x300.shape)

# 对照片中树的部分进行剪裁.
patch_tree = img[20:150, -180:-50]
cv2.imwrite('cropped_tree.jpg', patch_tree)
cv2.imwrite('resized_200x200.jpg', img_200x200)
cv2.imwrite('resized_200x300.jpg', img_200x300)
cv2.imwrite('bordered_300x300.jpg', img_300x300)

# 图像的旋转.
# 默认按顺时针旋转.
# windows上的图片wxh,前面是宽，后面是高。但img.shape前两个数字，第一个数字表示高，第二个数字表示宽。
theta = 30 * np.pi / 180
M_rotate = np.array([[np.cos(theta), -np.sin(theta), 0],
                    [np.sin(theta), np.cos(theta), 0]], dtype = np.float32)
img_rotated = cv2.warpAffine(img, M_rotate, (400, 600))
print('img_rotate, height, width', img_rotated.shape)
cv2.imwrite('image_rotated.jpg', img_rotated)

img_rotated2 = cv2.warpAffine(img, M_rotate, dsize = img.shape[-2::-1])
cv2.imwrite('image_rotated2.jpg', img_rotated2)
print(img_rotated2.shape)
