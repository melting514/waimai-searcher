import cv2

imgName = "bg1.jpg";
kernel_size = (5, 5);
sigma = 3;

img = cv2.imread(imgName);
img = cv2.GaussianBlur(img, kernel_size, sigma);
new_imgName = "New_" +imgName;
cv2.imwrite(new_imgName, img);
