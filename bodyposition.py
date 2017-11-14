# coding=utf-8
# 신체 특정점을 구하는 메소드들을 가진 클래스

import hand as h
import frontheight as fh

# 키 - 구해진 contour의 최고점 y, 최저점 y를 구한다.
# 키는 사용자로부터 입력 받아 cm당 픽셀수를 구하기 위해 사용

# cm당 픽셀 수를 구하는 메소드

# 손 위치를 구하는 메소드
def getHandPoints(pcimage):
    print("------Get HandPosition------")

    hand_tmp = h.getHand(pcimage)
    myhand = hand_tmp

    return myhand

# 머리와 발끝을 구하는 메소드
def getFrontHeightPoints(pcimage):
    print("------Get FrontHeight------")

    frontheight_tmp = fh.getFrontHeight(pcimage)
    myfrontheight = frontheight_tmp

    return myfrontheight

