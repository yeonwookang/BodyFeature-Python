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
def GetHand(edge, hand):
    outImage = copy.copy(edge) #객체 복사하기
    rowNumber = outImage.rows
    colNumber = outImage.cols

