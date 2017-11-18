# coding=utf-8
# 중간점, 다리를 찾는 클래스

import cv2
import bodycontour as bc # 윤곽선을 구하는 기능
import bodyposition as bp # 신체의 특정점들을 가져오는 기능
import numpy as np
import copy

# 중간점, 양 다리 점
class leftpoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class rightpoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class middlepoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 중간점을 찾는 메소드드
def getMiddlePoint(pcImage):

    outImage = copy.copy(pcImage)  # 객체 복사하기
    rowNumber = 700L
    colNumber = 525L

    col_start = 0
    col_end = colNumber - 1

    row_start = 0
    row_end = rowNumber - 1

    left_point = leftpoint(0, 0)
    right_point = rightpoint(0, 0)

    middle_point_X = int(colNumber/2)
    middle_point_Y = rowNumber-1
    middle_point = middlepoint(middle_point_X, middle_point_Y)

    for i in range(rowNumber-1, 0, -1):
        data_middle = outImage[i]
        for j in range(col_start, col_end):
            if np.any(data_middle[j]==[0, 255, 0]):
                middle_point.x = i

        count = 0
        for j in range(1, 10):
            if np.any(data_middle[j] == [0, 255, 0]):
                count = count + 1

        if(count > 5):
            left_point.x = middle_point.x
            left_point.y = middle_point.y

            for j in range(1, colNumber-1, 1):
                if np.any(data_middle[j] == [0,255,0]):
                    right_point.x = middle_point.x + j
                    right_point.y = middle_point.y
                    break

    return middle_point
