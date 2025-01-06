import cv2
wm = cv2.imread(r"C:\Users\ASUA TUF F 15\OneDrive\Pictures\Saved Pictures\OIP.jpg")
img = cv2.imread(r"C:\Users\ASUA TUF F 15\OneDrive\Pictures\Saved Pictures\monkey NFT.jpg")
if img is None or wm is None:
    print("Error: Could not load one or both images. Check the file paths.")
    exit()
h_wm, w_wm = wm.shape[:2]
h_img, w_img = img.shape[:2]
if h_wm > h_img or w_wm > w_img:
    print("Resizing the watermark to fit within the main image...")
    scaling_factor = min(h_img / h_wm, w_img / w_wm) * 0.5
    wm = cv2.resize(wm, (int(w_wm * scaling_factor), int(h_wm * scaling_factor)))
    h_wm, w_wm = wm.shape[:2]
center_x = w_img // 2
center_y = h_img // 2
top_y = center_y - h_wm // 2
left_x = center_x - w_wm // 2
bottom_y = top_y + h_wm
right_x = left_x + w_wm
roi = img[top_y:bottom_y, left_x:right_x]
result = cv2.addWeighted(roi, 1, wm, 0.3, 0)
img[top_y:bottom_y, left_x:right_x] = result
cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
