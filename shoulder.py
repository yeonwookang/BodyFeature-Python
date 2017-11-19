# coding=utf-8
# 어깨 클래스

import numpy as np
import copy

# 왼쪽 어깨
class left_shoulder:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 오른쪽 어깨
class right_shoulder:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 어깨 좌표 (양쪽 어깨 객체를 가짐)
class shoulder:
    left_shoulder = left_shoulder(0,0)
    right_shoulder = right_shoulder(0,0)

    def setShoulder(self, left_shoulder, right_shoulder):
        self.left_shoulder = left_shoulder
        self.right_shoulder = right_shoulder

# 양쪽 어깨점 탐색 - 각각 양쪽 발의 좌표를 기점으로 최상위 y값 contour 좌표를 저장
def getShoulderPoints(pcImage, footpoints):
    outImage = copy.copy(pcImage)  # 이미지 복사하기

    rowNumber = 700L
    colNumber = 525L

    # 왼쪽 어깨
    left = left_shoulder(0,0)

    # 탐색 범위(왼쪽)
    row_start = 0
    row_end = footpoints.left_feet.y
    col_start = footpoints.left_feet.x
    col_end = footpoints.left_feet.x

    for i in range(row_end, row_start, -1):
        data_left = outImage[i]
        if np.any(data_left[col_start]==[0, 255, 0]):
            left.x = footpoints.left_feet.x
            left.y = i
        if i <= 0:
            break

    # 오른쪽 어깨
    right = right_shoulder(0,0)

    # 탐색 범위(오른쪽)
    row_start = 0
    row_end = footpoints.right_feet.y
    col_start = footpoints.right_feet.x
    col_end = footpoints.right_feet.x

    for i in range(row_end, row_start, -1):
        data_right = outImage[i]
        if np.any(data_right[col_start]==[0, 255, 0]):
            right.x = footpoints.right_feet.x
            right.y = i
        if i <= 0:
            break

    # 왼쪽 어깨 좌표 및 오른쪽 어깨 좌표 가져오기
    print("--left shoulder--")
    print(left.x)
    print(left.y)

    print("--right shoulder--")
    print(right.x)
    print(right.y)

    my_shoulder = shoulder()
    my_shoulder.setShoulder(left, right)

    return my_shoulder