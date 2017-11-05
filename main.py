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
ImageName = "1_front.png" # 이미지 파일 이름
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

#손의 대한 내용을 출력한다.
print("|---Print Hand--------|")

# print(pp.left_hand)

img = cv.line(srcImage,(pp.left_hand.x,pp.left_hand.y),(pp.rignt_hand.x,pp.rignt_hand.y ),(255,0,0),5)

# print(pp.my_hand.my_right_hand)

# 이미지 보이기
cv.imshow('BodyFeature-Origin', srcImage) # 원본 이미지
cv.imshow('BodyFeature', Dst) # 후처리 이미지
cv.waitKey()

# 가로선을 그리는 메소드
# def draw_position(edge, line):