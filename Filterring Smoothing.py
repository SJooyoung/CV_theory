import cv2
import numpy as np

src = cv2.imread("window.jpg")
#이미지 불러오기

if src is None:
    print("Image load is failed!!")
#오류시 출력

Ycbcr = cv2.cvtColor(src, cv2.COLOR_RGB2YCrCb)
# opencv 함수를 이용한 Ycbcr 변환

Ycbcr_plane = cv2.split(Ycbcr)
# 채널별로 나눠주기


kernel = np.ones((3,3),np.float32)/9
# 3*3 커널값 저장

for i in range(5):
    Ycbcr_plane[0] = cv2.filter2D(Ycbcr_plane[0],-1, kernel)
#Averagin filter 5번 적용

dst_Ycbcr = cv2.merge(Ycbcr_plane)

dst = cv2.cvtColor(dst_Ycbcr,cv2.COLOR_YCrCb2RGB)
# RGB영상으로 다시 만들기

resize_src = cv2.resize(src,(400,400))
resize_dst = cv2.resize(dst,(400,400))
# 사이즈 조절

PSNR1 = cv2.PSNR(src, dst)
#cv2를 이용하여 PSNR값 구하기

print("원본영상과 복원영상의 PSNR은 {:.5} 입니다".format(PSNR1))


cv2.imshow("src", resize_src)
cv2.imshow("dst", resize_dst)
# 출력

cv2.waitKey()

cv2.destroyAllWindows()



