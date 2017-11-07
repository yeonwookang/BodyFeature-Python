# coding=utf-8
import cv2 as cv
import numpy as np
import copy
import hand as h

class allarmpit:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class armpit:
    leftarmpit = allarmpit(0, 0)
    rightarmpit = allarmpit(0, 0)

    def setHand(self, leftarmpit, rightarmpit):
        self.leftarmpit = leftarmpit
        self.rightarmpit = rightarmpit

class find_armpit_start_line:
    def __init__(self, left_start_line, right_start_line):
        self.left_start_line = left_start_line
        self.right_start_line = right_start_line


def GetArmpit(edge,start_line_a):
    outImage = copy.copy(edge)  # 객체 복사하기
    #겨드랑이의 포인트를 출력한다.

    #초기 데이터
    start_line=find_armpit_start_line(0,0)
    leftarm=armpit(0,0).leftarmpit
    rightarm=armpit(0,0).rightarmpit
    my_armpit=armpit(leftarm,rightarm)

    start_line=start_line_a

    print("|--- in GetArmpit ---------|")

    #겨드랑이의 포인트를 가져와야한다.
    leftarm=get_left_arm_point(edge,start_line)
    # rightarm=get_right_arm_point(edge,start_line)

    my_armpit.leftarmpit=leftarm
    # my_armpit.rightarmpit=rightarm

#left armpit bifurcation(분기점) 지점의 좌표를 찾는다.
def get_left_arm_point(edge,start_line):
    outImage=copy.copy(edge)

    print("|--- in get_left_arm_point ---------|")

    #<!!해당 이미지 row와 col 값을 찾아오는 방법을 해결해야함 >
    rowNumber = 840L
    colNumber = 641L

    #point점 초기화
    leftpoint1=allarmpit(0,0)
    rightpoint1=allarmpit(0,0)
    middlepoint1=allarmpit(int(colNumber/2),start_line-50)

    #왼쪽 팔 시드 검색 지점을 계산한다.
    for i in range(middlepoint1.y,0,-1):
        data = outImage[i]
        for j in range(middlepoint1.x,0,-1):
            if 0 in data[j]:
                rightpoint1.x=j
                rightpoint1.y=i
                while j>0:
                    j=j-1
                    if 255 in data[j]:
                        leftpoint1.x=j
                        leftpoint1.y=i
                        break
                middlepoint1.x=(rightpoint1.x+leftpoint1.x)/2
                middlepoint1.y=i
                break
        if rightpoint1.x!=0 and leftpoint1.x!=0:
            break



    for i in range(middlepoint1.y,0,-1):
        data=outImage[i]

        #data[middlepoint1.x]=255 왼쪽 및 오른쪽으로 검색한다.
        if 255 in data[middlepoint1.x]:
            middlepoint1.y=i

            #왼쪽으로 열개의 점을 찾는다.
            count=0

            for j in range(1,10):
                if 255 in data[middlepoint1.x-j]:
                    count=count+1
            if count>5:
                leftpoint1.x=middlepoint1.x
                leftpoint1.y=middlepoint1.y

                for j in range(1,colNumber):
                    if 255 in data[middlepoint1.x+j]:
                        rightpoint1.x=middlepoint1.x+j
                        rightpoint1.y=middlepoint1.y
                        break
            #middlepoint1은 right leg의 경계
            else:
                rightpoint1.x=middlepoint1.x
                rightpoint1.y=middlepoint1.y
                #무한 루프
                while True:
                 j=1
                 if 255 in data[middlepoint1.x-j]:
                    leftpoint1.x=middlepoint1.x-j
                    leftpoint1.y=middlepoint1.y
                    break
                 j=j+1

            middlepoint1.x=int((leftpoint1.x+rightpoint1.x)/2)
        else:
            pass # 여기의 역할을 모르겠음

        #다리의 분기점을 찾습니다.

        if middlepoint1.x==leftpoint1.x or middlepoint1.x==rightpoint1.x:
            break
        else:
            pass

    left_arm=allarmpit(0,0)

    left_arm.x=middlepoint1.x
    left_arm.y=middlepoint1.y
    # 출력 테스트
    print("left_arm x:" + left_arm.x)
    print("left_arm y:" + left_arm.y)

    return left_arm
