# coding=utf-8
# 손 클래스

import cv2
import numpy as np
import copy

# 왼손 좌표
class left_hand:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 오른손 좌표점
class right_hand:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 손끝의 지문 좌표 (왼손과 오른손 객체를 가진다.)

class hand:
    left_hand=left_hand(0,0)
    right_hand=right_hand(0,0)

    def setHand(self,left,right):
        self.right_hand=right
        self.left_hand=left

# 손의 좌표를 가져오는 메소드
def getHand(pcImage):

        outImage = copy.copy(pcImage)  # 객체 복사하기
        rowNumber = 700L
        colNumber = 525L

        # 튜플에 해당 값을 삽입

        row_start = 0
        row_end = 0
        row_start = 0
        row_end = rowNumber - 1

        # 왼쪽손
        left = left_hand(0, 0)
        # 인체의 흑백 차트를 찾는다.
        for i in range(0, colNumber):
            for j in range(row_start, row_end):
                data_left = outImage[j]  # 주소를 얻는 것이라고 하는데 ... 공부를 해봐야할 것같음
                #print "left: ", data_left[i]
                if np.any(data_left[i]==[0, 255, 0]): # 초록색 점에 닿으면
                    left.x = i
                    left.y = j
                    break
            if left.x > 0:
                 break

        right = right_hand(0, 0)
        for k in range(colNumber -1, 0, -1):
            for l in range(row_start, row_end):
                data_right = outImage[l]
                # print "right: ", data_right[k]
                if np.any(data_right[k]==[0, 255, 0]):  # 초록색 점에 닿으면
                    right.x = k
                    right.y = l
                    break

            if right.x > 0:
                break

        # 왼손 좌표 및 오른손 좌표 가져오기
        print("--left hand--")
        print(left.x)
        print(left.y)

        print("--right hand--")
        print(right.x)
        print(right.y)

        my_hand=hand()
        my_hand.setHand(left, right)

        return my_hand

