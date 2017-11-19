# coding=utf-8
# 머리점, 발끝점을 구하는 메소드

import numpy as np
import copy

# 머리 좌표
class front_head:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 발끝 좌표점
class front_foot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 정면 키 좌표 (머리와 발끝 객체를 가진다.)
class frontheight:
    front_head=front_head(0,0)
    front_foot=front_foot(0,0)

    def setFrontHeight(self, front_head, front_foot):
        self.front_head=front_head
        self.front_foot=front_foot

# 정면 키의 좌표를 가져오는 메소드
def getFrontHeight(pcImage):

        outImage = copy.copy(pcImage)  # 객체 복사하기
        rowNumber = 700L
        colNumber = 525L
        col_start = 0
        col_end = colNumber - 1

        # 머리
        head = front_head(0, 0)
        # 인체의 흑백 차트를 찾는다.
        for i in range(0,rowNumber):
            data_head = outImage[i]
            for j in range(col_start, col_end):
                if np.any(data_head[j]==[0, 255, 0]):  # 초록색 점에 닿으면
                    head.x = j
                    head.y = i
                    break

            if head.x > 0:
                break

        foot = front_foot(0, 0)
        for k in range(rowNumber-1, 0, -1):
            data_foot = outImage[k]
            for l in range(col_start, col_end):
                if np.any(data_foot[l]==[0, 255, 0]):  # 초록색 점에 닿으면
                    foot.x = l
                    foot.y = k
                    break

            if foot.y > 0:
                break

        # 왼손 좌표 및 오른손 좌표 가져오기
        print("--front head--")
        print(head.x)
        print(head.y)

        print("--front foot--")
        print(foot.x)
        print(foot.y)

        my_front_height=frontheight()
        my_front_height.setFrontHeight(head,foot)

        return my_front_height