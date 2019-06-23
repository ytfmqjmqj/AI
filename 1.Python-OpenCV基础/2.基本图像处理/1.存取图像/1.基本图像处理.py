import cv2

# 1.读取一张700x509分辨率的图像.
# Note:高度509,宽度是700.
color_img = cv2.imread('xiaoyao1.jpeg')
print(color_img.shape)

# 2.直接读取单通道.
gray_img = cv2.imread('xiaoyao1.jpeg', cv2.IMREAD_GRAYSCALE)
print(gray_img.shape)

# 3.把单通道图片保存后，再读取，仍然是3通道，相当于把单通道复制到3个通道保存
cv2.imwrite('xiaoyao1_grayscale.jpg', gray_img)
reload_grayscale = cv2.imread('xiaoyao1_grayscale.jpg')
print(reload_grayscale.shape)