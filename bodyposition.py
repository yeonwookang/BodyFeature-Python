# coding=utf-8
# 신체 특정점을 구하는 메소드들을 가진 클래스

import hand as h
import frontheight as fh
import foot as ft
import shoulder as sd
import armpoint as arm
import legbranch as leg

#body class에 해당 point들을 저장한다...---> 생각해봐야함
class bodyp:
    my_hand=0
    my_height=0


# 키 - 구해진 contour의 최고점 y, 최저점 y를 구한다.
# 키는 사용자로부터 입력 받아 cm당 픽셀수를 구하기 위해 사용


# 손 위치를 구하는 메소드
def getHandPoints(pcImage):

    print("------Get HandPosition------")

    hand_tmp = h.getHand(pcImage)
    myhand = hand_tmp

    return myhand

# 머리와 발끝을 구하는 메소드
def getFrontHeightPoints(pcImage):

    print("------Get FrontHeight------")

    frontheight_tmp = fh.getFrontHeight(pcImage)
    myfrontheight = frontheight_tmp

    return myfrontheight

# 양 발끝을 구하는 메소드
def getFootPoints(pcImage, frontheight_points, hand_points):

    print("------Get FootPoints------")

    footpoints_tmp = ft.getFootPoints(pcImage, frontheight_points, hand_points)
    myfootpoints = footpoints_tmp

    return myfootpoints

# 양쪽 어깨를 구하는 메소드
def getShoulderPoints(pcImage, footpoints):

    print("------Get ShoulderPoints------")

    shoulderpoints_tmp = sd.getShoulderPoints(pcImage, footpoints)
    mysholderpoints = shoulderpoints_tmp

    return mysholderpoints

#겨드랑이는 손의 좌표와 다리 분기점 좌표를 받아와야합니다.
def getArmPoint(pcImage,handPoint,legBranch):

    print("------in BodyPostition(armpoint)-----")

    # 시작점은 0,0에서 시작합니다.
    start_line=arm.find_armpit_start_line(0,0)

    if(handPoint.left_hand.y>legBranch.y):
        #다리의 분기점보다 왼쪽 손의 y점이 더 아래라면 start-line은 왼쪽 손의 y값
        start_line.left_start_line=handPoint.left_hand.y
    else:
        start_line.left_start_line=handPoint.left_hand.y

    if(handPoint.right_hand.y>legBranch.y):
        start_line.right_start_line=handPoint.right_hand.y
    else:
        start_line.right_start_line=handPoint.right_hand.y

    my_armpit=arm.GetArmpit(pcImage,start_line)


    return my_armpit

def getLegBranchPoint(pcImage):
    print("------Get legBranchPoints------")
    leg_branch=leg.findLegPoint(pcImage)

    return leg_branch
