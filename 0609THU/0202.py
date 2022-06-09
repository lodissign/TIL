# 0202.py 
# img 영상을 data 폴더에 'Lena.bmp', 'Lena.png', 'Lena2.png', 'Lena2.jpg' 파일로 저장.
import cv2

imageFile = './data/lena.jpg'
img = cv2.imread(imageFile) 
cv2.imwrite('./data/Lena.bmp', img)
cv2.imwrite('./data/Lena.png', img)
cv2.imwrite('./data/Lena2.png',img, [cv2.IMWRITE_PNG_COMPRESSION, 9])   # [cv2.IMWRITE_PNG_COMPRESSION, 9] 는 img를 압축률 9의 png 영상으로 'Lena2.png' 파일에 저장. 압축률은 [0,9]이며 압츅률이 높을수록 시간이 오래 걸림. default=3.
cv2.imwrite('./data/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])    # [cv2.IMWRITE_JPEG_QUALITY, 90]은 img를 90%의 품질을 갖는 jpeg 영상으로 'Lena2.jpg' 파일에 저장. 품질의 범위는 [0,100]이며 높을 수록 영상의 품질이 좋다. default=95.