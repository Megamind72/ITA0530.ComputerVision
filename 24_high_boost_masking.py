import cv2
resized_img = cv2.imread(r"C:\Users\ASUA TUF F 15\OneDrive\Pictures\Saved Pictures\OIP.jpg")
resized_wm = cv2.imread(r"C:\Users\ASUA TUF F 15\OneDrive\Pictures\Saved Pictures\OIP.jpg")

if resized_img is None or resized_wm is None:
    raise FileNotFoundError("Input image or watermark image could not be loaded. Check the file paths.")

h_img, w_img, _ = resized_img.shape
center_y = int(h_img / 2)
center_x = int(w_img / 2)
h_wm, w_wm, _ = resized_wm.shape

if h_wm > h_img or w_wm > w_img:
    scale = min(h_img / h_wm, w_img / w_wm)
    resized_wm = cv2.resize(resized_wm, (int(w_wm * scale), int(h_wm * scale)))
    h_wm, w_wm, _ = resized_wm.shape

top_y = center_y - int(h_wm / 2)
left_x = center_x - int(w_wm / 2)
bottom_y = top_y + h_wm
right_x = left_x + w_wm
roi = resized_img[top_y:bottom_y, left_x:right_x]
result = cv2.addWeighted(roi, 1, resized_wm, 0.3, 0)
resized_img[top_y:bottom_y, left_x:right_x] = result

output_filename = r"C:\Users\ASUA TUF F 15\OneDrive\Pictures\Saved Pictures\OIP.jpg"
cv2.imwrite(output_filename, resized_img)
cv2.imshow("Resized Input Image with Watermark", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
