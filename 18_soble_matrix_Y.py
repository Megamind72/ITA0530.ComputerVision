import cv2 
img = cv2.imread(r"C:\Users\ASUA TUF F 15\OneDrive\Pictures\Saved Pictures\OIP.jpg")  
# Display original image 
cv2.imshow('Original', img) 
cv2.waitKey(0) 
 # Convert to graycsale 
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
# Blur the image for better edge detection 
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)  
 # Sobel Edge Detection 
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
# Sobel Edge Detection on the Y axis 
# Display Sobel Edge Detection Images 
cv2.imshow('Sobel Y', sobely) 
cv2.waitKey(0)  
