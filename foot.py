# coding=utf-8
# 양쪽 발끝을 찾는 클래스

import cv2
import numpy as np
import copy

# 왼쪽 발
class left_feet:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 오른쪽 발
class right_feet:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 중간점 포인트 - 양쪽 발 끝의 포인트 객체를 가짐
class footpoints:
    left_feet = left_feet(0,0)
    right_feet = right_feet(0,0)

    def setFootPoints(self, left_feet, right_feet):
        self.left_feet = left_feet
        self.right_feet = right_feet

# 양쪽 발끝점 탐색 - 왼쪽발: 0~머리 기준점 / 오른발: 머리 기준점~col_end
def getFootPoints(pcImage, frontheight_points, hand_points):

    # 탐색 범위 지정을 위한 양쪽 손 끝점, 머리점 사용
    hand = hand_points
    frontheight = frontheight_points

    outImage = copy.copy(pcImage)  # 객체 복사하기

    rowNumber = 700L
    colNumber = 525L

    # 탐색 범위
    row_start = hand.left_hand.y
    row_end = frontheight.front_foot.y
    col_start = hand.left_hand.x
    col_end = frontheight.front_head.x

    # 왼쪽 발
    left = left_feet(0,0)
    for k in range(row_end, row_start, -1):
        data_left = outImage[k]
        for l in range(col_start, col_end):
            if np.any(data_left[l] == [0, 255, 0]):  # 초록색 점에 닿으면
                left.x = l
                left.y = k
                break

        if left.y > 0:
            break

    # 탐색 범위
    row_start = hand.right_hand.y
    row_end = frontheight.front_foot.y
    col_start = frontheight.front_head.x
    col_end = colNumber - 1

    # 오른쪽 발
    right = right_feet(0,0)
    for k in range(row_end, row_start, -1):
        data_right = outImage[k]
        for l in range(col_end, col_start, -1):
            if np.any(data_right[l] == [0, 255, 0]):  # 초록색 점에 닿으면
                right.x = l
                right.y = k
                break

        if right.y > 0:
            break

    # 왼발 좌표 및 오른발 좌표 가져오기
    print("--left feet--")
    print(left.x)
    print(left.y)

    print("--right feet--")
    print(right.x)
    print(right.y)

    my_footpoints = footpoints()
    my_footpoints.setFootPoints(left, right)

    return my_footpoints