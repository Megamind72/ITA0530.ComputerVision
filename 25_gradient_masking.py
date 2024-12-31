import cv2
import numpy as np

# Load the image in grayscale
image_path = r"C:\Users\ASUA TUF F 15\OneDrive\Pictures\Saved Pictures\OIP.jpg"
a = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if a is None:
    raise FileNotFoundError("Image could not be loaded. Check the file path.")

# Define Laplacian kernels
Lap = np.array([[0, 1, 0],
                [1, -4, 1],
                [0, 1, 0]], dtype=np.float32)

lap = np.array([[-1, -1, -1],
                [-1,  8, -1],
                [-1, -1, -1]], dtype=np.float32)

# Convolve with the first Laplacian kernel
a1 = cv2.filter2D(a, -1, Lap)
a2 = np.uint8(np.abs(a1))  # Convert to uint8

# Display the result of first convolution
cv2.imshow("Laplacian 1 Result", a2)

# Convolve with the second Laplacian kernel
a3 = cv2.filter2D(a, -1, lap)
a4 = np.uint8(np.abs(a3))  # Convert to uint8

# Combine original with a4 for visualization
result = cv2.add(np.uint8(np.abs(a)), a4)

# Display the final result
cv2.imshow("Laplacian 2 Result", result)

# Wait and clean up
cv2.waitKey(0)
cv2.destroyAllWindows()
