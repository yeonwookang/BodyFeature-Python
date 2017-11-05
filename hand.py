# coding=utf-8
import cv2 as cv
import numpy as np
import copy

# 왼손 좌표
class left_hand:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 으론슨 좌표점
class right_hand:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 손끝의 지문 좌표 (왼손과 오른손 객체를 가진다.)
class hand:

    def __init__(self, left_hand, right_hand):
        self.left_hand = left_hand
        self.right_hand = right_hand

# 손의 좌표를 가져오는 메소드
def GetHand(edge):
        outImage = copy.copy(edge)  # 객체 복사하기
        rowNumber = 840L
        colNumber = 641L

        # 튜플에 해당 값을 삽입

        # 왼쪽손
        left = left_hand(0, 0)

        print("|--- in GetHand ---------|")

        row_start = 0
        row_end = 0
        row_start = 100
        row_end = rowNumber - 200

        # 인체의 흑백 차트를 찾는다.
        for i in range(0, colNumber):
            for j in range(row_start, row_end):
                data_left = outImage[j]  # 주소를 얻는 것이라고 하는데 ... 공부를 해봐야할 것같음
                if np.any(data_left[i] != 255):
                    print("|--- in LeftHand ---------|")
                    print(i)
                    print(j)
                    left.x = i
                    left.y = j
                    break
            if left.x > 0:
                break

        right = right_hand(0, 0)

        for i in range(colNumber - 1, 0):
            for j in range(row_start, row_end):
                data_right = outImage[j]
                if np.any(data_right[i] != 255):
                    print("|--- in rightHand ---------|")
                    print(i)
                    print(j)
                    right.x = i
                    right.y = j
                    break
            if right.x > 0:
                break

        # 왼손 좌표 및 오른손 좌표 가져오기

        my_hand=hand(left,right)
        return my_hand

def GetLeftHand(edge):
    outImage = copy.copy(edge)  # 객체 복사하기
    rowNumber = 840L
    colNumber = 641L

    # 튜플에 해당 값을 삽입

    # 왼쪽손
    left = left_hand(0, 0)

    print("|--- in GetHand ---------|")

    row_start = 0
    row_end = 0
    row_start = 100
    row_end = rowNumber - 200

    # 인체의 흑백 차트를 찾는다.
    for i in range(0, colNumber):
        for j in range(row_start, row_end):
            data_left = outImage[j]  # 주소를 얻는 것이라고 하는데 ... 공부를 해봐야할 것같음
            if np.any(data_left[i] != 255):
                print("|--- in LeftHand ---------|")
                print(j)
                print(j)
                left.x = i
                left.y = j
                break
        if left.x > 0:
            break


    my_left_hand=left
    return my_left_hand
