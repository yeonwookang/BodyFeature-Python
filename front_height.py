# coding=utf-8
import cv2 as cv
import numpy as np
import copy
import hand as h

# 머리와 발을 찾는 클래스
class head: # 머리
    def __init__(self, x, y):
        self.x = x
        self.y = y

class foot: # 발
    def __init__(self, x, y):
        self.x = x
        self.y = y

class height: # 키 (머리부터 발까지)
    head=head(0,0)
    foot=foot(0,0)

    def setHeight(self,head,foot):
        self.head=head
        self.foot=foot

def GetHeight(edge):

    outImage = copy.copy(edge)  # 객체 복사하기
    rowNumber = 840L # 이미지 크기와 관련있어 보임
    colNumber = 641L

    # 튜플에 해당 값을 삽입

    # 머리 초기화
    headpoint = head(0, 0)
    print("|--- in GetHeight ---------|")
    row_start = 0
    row_end =rowNumber - 1
    col_start = 0
    col_end = colNumber - 1

    data_head = outImage
    # 인체의 흑백 차트를 찾는다. (머리의 y좌표)
    for i in range(0, rowNumber):
        for j in range(col_start, col_end):
            if np.any(data_head[j] != 255):
                headpoint.y = j
                headpoint.x = i
                break
        if headpoint.y > 0:
            break

    # 발 초기화
    footpoint = foot(0, 840)



    # 임시 출력
    print(headpoint.x)
    print(headpoint.y)
    print(footpoint.x)
    print(footpoint.y)

    my_height = height()
    my_height.setHeight(headpoint, footpoint)

    return my_height #height 넘김