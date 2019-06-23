import cv2

# 读取一张四川大录古藏寨的照片.
img = cv2.imread('tiger_tibet_village.jpg')
print(img.shape)

# 缩放成200x200的方形图像.
img_200x200 = cv2.resize(img, (200, 200))
print(img_200x200.shape)

# 不直接指定缩放大小，通过fx和fy指定缩放比例，0.5则长度和宽度都为原来的一半.
# 等效于img_200x300 = cv2.resize(img, (300, 200)),注意指定大小的格式是（宽度，高度）.
# 插值方法默认是cv2.INTER_LINEAR，这里指定为最近邻插值.
img_200x300 = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5, interpolation = cv2.INTER_NEAREST)
print(img_200x300.shape)

# 在上张图片的基础上，上下各贴50像素的黑边，生成300x300的图像
img_300x300 = cv2.copyMakeBorder(img, 50, 50, 0, 0, cv2.BORDER_CONSTANT, value = (0, 0, 0))
print(img_300x300.shape)