# coding=utf-8
# 신체 특정점을 구하는 메소드들을 가진 클래스

import hand as h
import frontheight as fh
import foot as ft
import shoulder as sd

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
