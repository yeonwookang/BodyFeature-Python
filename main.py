# coding=utf-8

from scipy.misc import imread, imsave, imresize
import cv2 as cv
import numpy as np
import copy

import converttobinary as ctb
import bodyposition as bp
import hand as h

# 소스 이미지 가져오기
# cv::Mat형 자료 -> numppy로 변환 가능 (numpy 배열로 python에서 이미지를 저장할 수 있다.)
ImageName = "1_front.png" # 이미지 파일 이름, 현재 이미지를 1_front.png 외에 다른 것으로 바꾸었을 때 실행되지 않는 오류가 있음 - 원인 이미지 크기 (641 * 840)
srcImage = imread(ImageName) # 이미지 파일 이름을 이용해 이미지를 가져온다. (같은 디렉토리 내에 위치 해있어야 함.)

Dst = ctb.get_BinaryImage(srcImage)

print srcImage.dtype, srcImage.shape, srcImage.size # 3차원 배열로 나옴
#print Dst.dtype, Dst.shape, Dst.size

# 실제 키가 170 인 것으로 가정
height = 170.00 * 10 # 170.00 * 10 mm
ratio = 0.0 # 픽셀 비율
#ratio = GetRatio(Dst, height, ratio)

# 여러가지 몸의 point들이 들어있는 class를 받아온다.

#결과 값을 출력
pp=bp.GetBodyPosition(srcImage)
pp2=bp.GetBodyPosition2(srcImage)

#손의 대한 내용을 출력한다.
print("|---Print Hand--------|")

    
# 화면 가로선 그리기 - 후처리 이미지
# 손
th = cv.line(Dst, (0, pp.left_hand.y), (1000, pp.rignt_hand.y), (0, 0, 255), 1)  # 화면 크기의 x 최대 값으로 오른쪽 점 x좌표 값을 바꿔주어야 함
# 머리선
th2 = cv.line(Dst, (0, pp2.head.y), (1000, pp2.head.y), (0, 0, 255), 1)
# 발선
th3 = cv.line(Dst, (0, pp2.foot.y), (1000, pp2.foot.y), (0, 0, 255), 1)

# 손 점 찍기
img = cv.line(Dst,(pp.left_hand.x,pp.left_hand.y),(pp.left_hand.x,pp.left_hand.y),(255,0,0),10)
img2 = cv.line(Dst,(pp.rignt_hand.x,pp.rignt_hand.y),(pp.rignt_hand.x,pp.rignt_hand.y),(255,0,0),10)

# 머리점
img3 = cv.line(Dst,(pp2.head.x,pp2.head.y),(pp2.head.x,pp2.head.y ),(255,0,0),5)
# 발끝점
img4 = cv.line(Dst,(pp2.foot.x,pp2.foot.y),(pp2.foot.x,pp2.foot.y ),(255,0,0),5)

# 후처리 이미지에 결과 값을 출력 (확인용)
pp=bp.GetBodyPosition(Dst)
# 이미지 보이기
cv.imshow('BodyFeature-Origin', srcImage) # 원본 이미지
cv.imshow('BodyFeature', Dst) # 후처리 이미지
cv.waitKey()

