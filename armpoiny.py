# coding=utf-8
import cv2 as cv
import numpy as np
import copy

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

def GetArmpit(edge):
    outImage = copy.copy(edge)  # 객체 복사하기

