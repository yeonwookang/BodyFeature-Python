# coding=utf-8
# 이미지를 처리하는 클래스

import cv2
import numpy as np
import copy

# 원본 이미지를 처리하여 윤곽선을 딴 이미지를 반환하는 메소드
def getProcessedImage(srcImage):
    image = copy.copy(srcImage) # 매개변수로 받은 이미지 저장
    print "image.shape", image.shape #이미지 셰이프 출력

    #r = 600.0 / image.shape[1]  # shape[0] 이미지 높이 600 픽셀에대한 비율
    #dim = (600, int(image.shape[0] * r))  # 차원 (600, 같은 비율로 이미지 너비 설정)
    #print "dimension =", dim

    # 이미지 비율조정
    #image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    #이미지 흑백 변환
    imagegray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 이미지 블러 처리
    imageblurred = cv2.bilateralFilter(imagegray, 7, 35, 35)

    # Canny로 외곽선 구하기
    canny = cv2.Canny(imageblurred, 40, 150)

    # Thresholding 잡음 줄이기
    ret, thresh = cv2.threshold(canny, 127, 255, 0)

    # Contour로 외곽선 그리기
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # 흑백처리한 이미지 위에 외곽선을 그려봄
    processedImage = cv2.drawContours(image, contours, -1, (0, 255, 0), 1)
    # 처리된 이미지는 processedImage에 저장하여 반환

    return processedImage