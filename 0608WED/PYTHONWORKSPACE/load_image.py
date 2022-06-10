import matplotlib.pyplot as plt
# matplotlib는 자료를 시각화 하는데 사용하는 대표적인 라이브러리. 3차원 시각화 도구를 제공하지만 평면상에서 알아보기 힘들어 2차원 위주의 기능. 
# pyplot을 plt라는 이름으로 import한다는 뜻.

import matplotlib.image as mpimg

# reading in an image

image = mpimg.imread('solidWhiteCurve.jpg')
# 'solidWhiteCurve.jpg' 읽어와서 image에 저장.

# printing out some stats and plotting the image

print('This image is:', type(image), 'with dimensions:', image.shape)
# image type, image (높이,너비,색상채널) 터미널 출력.

plt.imshow(image)  
plt.show()
# 읽어온 이미지 show후