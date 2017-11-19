# coding=utf-8
# 원래 코드에서는 middlepoint였지만 해당 코드에서는 다리 분기점을 찾는 곳으로 사용됩니다.

import cv2 as cv
import numpy as np
import copy


class livepoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def findLegPoint(edge):

    outImage = copy.copy(edge)  # 객체 복사하기

    rowNumber = 700L
    colNumber = 525L

    # leftpoint,rightpoint, middlepoint 생성

    leftpoint=livepoint(0,0)
    rightpoint=livepoint(0,0)
    middlepoint=livepoint(int(colNumber/2),rowNumber-1)



    print("|--- in findThepoint ---------|")
    for i in (rowNumber-1,0,-1):
        # 사진 배열을 data에 복사한다.
        data = outImage[i]

        if 255 in data[middlepoint.x]:
            middlepoint.y=i #처음 시작은 아까 초기값과 동일하게
            count=0
            for j in range(1,10):
                if 255 in data[middlepoint.x-j]:
                    count=count+1

            if count >5:
                leftpoint.x=middlepoint.x
                leftpoint.y=middlepoint.y

                for j in range(1,colNumber):
                    if 255 in data[middlepoint.x+j]:
                        rightpoint.x=middlepoint.x+j
                        rightpoint.y=middlepoint.y
                        break
            else:
                rightpoint.x=middlepoint.x
                rightpoint.y=middlepoint.y

                # 무한 루프
                while True:
                    j = 1
                    if 255 in data[middlepoint.x - j]:
                        leftpoint.x = middlepoint.x - j
                        leftpoint.y = middlepoint.y
                        break
                    j = j + 1

            middlepoint.x = int((leftpoint.x + rightpoint.x) / 2)
        else:
            pass  # 여기의 역할을 모르겠음

            # 다리의 분기점을 찾습니다.

        if middlepoint.x == leftpoint.x or middlepoint.x == rightpoint.x:
            break
        else:
            pass


    dstpoint=livepoint(0,0)

    dstpoint.x=middlepoint.x
    dstpoint.y=middlepoint.y

    print(dstpoint.x)
    print (dstpoint.y)

    return dstpoint



