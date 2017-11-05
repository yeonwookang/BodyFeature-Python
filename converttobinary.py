# coding=utf-8

import cv2 as cv
import numpy as np
import scipy as cp
import math
import copy

def get_BinaryImage(srcImage):
    # [1]이미지 색상 흑백 변환
    srcImage_Gray = cv.cvtColor(srcImage, cv.COLOR_BGRA2GRAY)
    print("|--- in get_BinaryImage ---------|")

    # 가우시안 블러 처리
    srcImage_Gray_Gauss = cv.GaussianBlur(srcImage_Gray,(3, 3), 0)

    # 블러 처리
    srcImage_Gray_Gauss = cv.blur(srcImage_Gray_Gauss, (3, 3))

    # Canny를 이용해 처리된 이미지로부터 edge를 구함
    edge = cv.Canny(srcImage_Gray_Gauss, 30, 15, 3)

    # 정육각형 물체를 가져옴
    element = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))

    edge_temp = edge
    for i in range(0,1):
        edge = cv.dilate(edge_temp, edge, element) #팽창
        edge_temp = edge

    for i in range(0, 1):
        # fillHole() edge 테두리(색상 흰색) 안의 범위를 하얗게 칠한다.
        edge_temp = edge

    th, dst = cv.threshold(edge_temp, 150, 255, cv.THRESH_BINARY, edge)
    Dst = np.zeros(edge.size) # edge 크기의 빈 배열 생성인데... 잘못된 것 같다.


    return Dst  # numpy 배열 반환, numpy 배열은 이미지로 표현될 수 있다.


# 신체 이미지 부분을 색칠하는 함수
def fillHole(srcBw, dstBw):
    m_Size = srcBw.size

    Temp = np.zeros(m_Size.height + 2, m_Size.width + 2, srcBw.type)
    Temp = copy.copy(srcBw)

    cv.floodFill(Temp, (0,0), 255)



def RemoveSmallRegion(Src, Dst, AreaLimit, CheckMode, NeighborMode):
    RemoveCount = 0

    Pointlabel = np.zeros(np.size(Src), cv.CV_8UC1)



