import cv2 
import numpy as np 
kernel = np.ones((5,5),np.uint8) 
img = cv2.imread(r"C:\Users\ASUA TUF F 15\OneDrive\Pictures\Saved Pictures\OIP.jpg",cv2.IMREAD_COLOR) 
img = cv2.resize(img,(300,300)) 
cv2.imshow("image",img) 
cv2.waitKey(0) 
