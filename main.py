# coding=utf-8
# Main class

#
# 2017.11.19(일)
# 연우
# 양쪽 발끝 점, 어깨 점 구하기
#


import cv2
import bodycontour as bc # 윤곽선을 구하는 기능
import bodyposition as bp # 신체의 특정점들을 가져오는 기능
import math
from PIL import Image # 이미지 모듈 라이브러리
import numpy as np
import copy

# 마우스 클릭 이벤트 처리를 위한 변수
ix, iy = -1, -1 # 마우스 좌표값 (시작점)
mode = False # 마우스 클릭 이벤트 플래그
length = 0 # 선의 길이

# 사용자로부터 입력받은 키와 픽셀/키 값을 저장할 변수
height = 0 # 사용자 키
cm_per_pixel = 0 # pixel당 cm 비율

# 사용자로부터 이미지를 받아옴
# 빠른 테스트를 위해 이미지 경로 지정
# 이미지 원본은 srcImage에 저장함
imgPath = "1_front3.png" #이미지 경로
srcImage = cv2.imread(imgPath, 1) # 원본 이미지

# 사용자로부터 받아온 이미지를 처리하여
# 윤곽선을 구해온 이미지를 저장 (윤곽선을 여기서는 RGB(0, 255, 0) 형광 초록으로 하여 눈에 잘 띄게 하겠음)
pcImage = bc.getProcessedImage(srcImage) # 윤곽선을 구한 이미지

# 거리를 구하는 공식 함수 - 시작점의 x, y값 끝점의 x, y값을 매개변수로 받음
def getDistance(start_x, start_y ,end_x, end_y):
    #받은 좌표값을 이용해 거리 계산\
    distance = math.sqrt((start_x-end_x)*(start_x-end_x)+(start_y-end_y)*(start_y-end_y))
    return distance

# 마우스 클릭처리를 담당할 리스너 함수
def onMouse(event, x, y, flag, param):
    # 전역 변수들 사용
    global ix, iy, mode,  srcImage, pcImage, length, height, cm_per_pixel

    # 마우스 왼쪽 버튼이 눌러졌을 때
    if event == cv2.EVENT_LBUTTONDOWN:
        mode = True # 선 그리기 시작
        ix, iy = x, y # 시작점 좌표 저장

    # 마우스 왼쪽 버튼이 떨어졌을 때
    elif event == cv2.EVENT_LBUTTONUP:
        mode = False # 선 그리기 종료
        cv2.line(pcImage, (ix, iy), (x, y), (0, 0, 255), 2) # 붉은 선을 그림 (시작점 - 끝점)
        cv2.imshow("ProcessedImage", pcImage) # 처리된 이미지에 표시

        # 시작점 - 끝점 거리 구하기
        length = getDistance(ix, iy, x, y)

        print("----length(pixel)----")
        print(length) # 픽셀 개수
        print("----length(cm)-------")
        print (length*cm_per_pixel)  # cm ( 픽셀 개수 * 픽셀당 센치미터 비율)
        print("---------------------")
    return

# 윤곽선이 구해진 이미지를 사용해 특정점 구하기를 시작

# 손 찾아 점 찍기
hand_points = bp.getHandPoints(pcImage) # 손의 좌표를 가져옴
cv2.circle(pcImage, (hand_points.left_hand.x, hand_points.left_hand.y), 3, (0, 0, 255), -1) #왼손 찍기
cv2.circle(pcImage, (hand_points.right_hand.x, hand_points.right_hand.y), 3, (0, 0, 255), -1) #오른손 찍기

# 정면 키 찾아 점 찍기
frontheight_points = bp.getFrontHeightPoints(pcImage) # 정면 키 좌표를 가져옴
cv2.circle(pcImage, (frontheight_points.front_head.x, frontheight_points.front_head.y), 3, (0, 0, 255), -1) #머리점 찍기
cv2.circle(pcImage, (frontheight_points.front_head.x, frontheight_points.front_foot.y), 3, (0, 0, 255), -1) #발끝점 찍기 - 발끝의 x는 머리의 x로 둠

#양 발 끝 점찍기 - 머리 점을 기준으로 왼쪽 오른쪽 나누어서 탐색 시도, frontheight_points, hand_points 값을 매개변수로 넘긴다
footpoints = bp.getFootPoints(pcImage, frontheight_points, hand_points)

#cv2.circle(pcImage, (footpoints.left_feet.x, footpoints.left_feet.y), 3, (0, 0, 255), -1) #왼쪽 발끝점 찍기
#cv2.circle(pcImage, (footpoints.right_feet.x, footpoints.right_feet.y), 3, (0, 0, 255), -1) #오른쪽 발끝점 찍기

#양 어깨에 점찍기 - 양쪽 발 끝점을 기준으로 해당 좌표 y의 최상위 contour 값을 탐색
# 양 발끝의 좌표를 매개변수로 넘긴다
shoulderpoints = bp.getShoulderPoints(pcImage, footpoints)
cv2.circle(pcImage, (shoulderpoints.left_shoulder.x, shoulderpoints.left_shoulder.y), 3, (0, 0, 255), -1) #왼쪽 어깨점 찍기
cv2.circle(pcImage, (shoulderpoints.right_shoulder.x, shoulderpoints.right_shoulder.y), 3, (0, 0, 255), -1) #오른쪽 어깨점 찍기

# 양쪽 팔 길이 선
cv2.line(pcImage, (shoulderpoints.left_shoulder.x, shoulderpoints.left_shoulder.y), (hand_points.left_hand.x, hand_points.left_hand.y), (255, 0, 0), 1)
cv2.line(pcImage, (shoulderpoints.right_shoulder.x, shoulderpoints.right_shoulder.y), (hand_points.right_hand.x, hand_points.right_hand.y), (255, 0, 0), 1)
# 어깨 너비 선
cv2.line(pcImage, (shoulderpoints.left_shoulder.x, shoulderpoints.left_shoulder.y), (shoulderpoints.right_shoulder.x, shoulderpoints.right_shoulder.y), (255, 0, 0), 1)
#키
cv2.line(pcImage, (frontheight_points.front_head.x, frontheight_points.front_head.y), (frontheight_points.front_head.x, frontheight_points.front_foot.y), (255, 0, 0), 1) #키 - 발끝의 x는 머리의 x로 둠

##다리 분기점##
leg_branch=bp.getLegBranchPoint(pcImage)

##겨드랑이##
armpit=bp.getArmPoint(pcImage,hand_points,leg_branch)
cv2.circle(pcImage,(armpit.leftarmpit.x,armpit.leftarmpit.y),3,(0,0,255),-1)

# cv2.line(pcImage,(leg_branch.x,0),(leg_branch.x,10000),(255,0,0),1)


#임의 선
#cv2.line(pcImage, (hand_points.left_hand.x, hand_points.left_hand.y), (hand_points.right_hand.x, hand_points.right_hand.y), (255, 0, 0), 1) #손
#cv2.line(pcImage, (frontheight_points.front_head.x, frontheight_points.front_head.y), (frontheight_points.front_head.x, frontheight_points.front_foot.y), (255, 0, 0), 1) #키 - 발끝의 x는 머리의 x로 둠

#cv2.line(pcImage, (frontheight_points.front_head.x, frontheight_points.front_head.y), (hand_points.left_hand.x, hand_points.left_hand.y), (255, 200, 0), 1) #머리-왼손
#cv2.line(pcImage, (frontheight_points.front_head.x, frontheight_points.front_head.y), (hand_points.right_hand.x, hand_points.right_hand.y), (255, 200, 0), 1) #머리-오른손
#cv2.line(pcImage, (frontheight_points.front_head.x, frontheight_points.front_foot.y), (hand_points.left_hand.x, hand_points.left_hand.y), (255, 200, 0), 1) #왼손-발
#cv2.line(pcImage, (frontheight_points.front_head.x, frontheight_points.front_foot.y), (hand_points.right_hand.x, hand_points.right_hand.y), (255, 200, 0), 1) #오른손-발
#cv2.line(pcImage, (shoulderpoints.left_shoulder.x, shoulderpoints.left_shoulder.y), (footpoints.left_feet.x, footpoints.left_feet.y), (100, 200, 100), 1) # 왼쪽 어깨 - 왼쪽 발

# 입력받은 키 / 머리에서 발까지 길이 = cm당 픽셀 수
# 사용자에게 키 입력 받기
height = input(">> INSERT HEIGHT(cm): ")
height = float(height)

# 발-머리 픽셀 수 구하기
print("---pixel count(head~foot)---")
height_pixel = float(frontheight_points.front_foot.y - frontheight_points.front_head.y)
print(height_pixel)
print("-----cm per pixel-----")
cm_per_pixel = float(height/height_pixel)
print(cm_per_pixel)
print("------------------------")

###############################################################################
#                       구해진 픽셀로 치수 구하기                               #
###############################################################################

# 총장 (뒷목 중간 ~ 발끝) * 여기선 편의를 위해 어깨 위치로 뒷목 높이를 잡았으나, 카라가 있는 의상에선 오차 크게 발생할 수 있음
# 오차를 감안하고 왼쪽 어깨부터 왼쪽 발까지를 사용하였다.
total_length_pixel = getDistance(shoulderpoints.left_shoulder.x, shoulderpoints.left_shoulder.y, footpoints.left_feet.x, footpoints.left_feet.y)
total_length_cm = total_length_pixel * cm_per_pixel
print("총장: {}"  .format(total_length_cm))

# 어깨너비
shoulder_width_pixel = getDistance(shoulderpoints.left_shoulder.x, shoulderpoints.left_shoulder.y, shoulderpoints.right_shoulder.x, shoulderpoints.right_shoulder.y)
shoulder_width_cm = shoulder_width_pixel * cm_per_pixel
print("어깨너비: {}" .format(shoulder_width_cm))

# 왼팔길이 * 손끝이 아니라 손목을 사용해야 할 듯, 오차 발생할 수 있음 (다른 사진에서도 오차범위가 일정하다면 계산으로 해결 가능하지 않을까요?
left_arm_length_pixel = getDistance(shoulderpoints.left_shoulder.x, shoulderpoints.left_shoulder.y, hand_points.left_hand.x, hand_points.left_hand.y)
left_arm_length_cm = left_arm_length_pixel * cm_per_pixel
print("왼팔길이: {}" .format(left_arm_length_cm))

# 오른팔길이
right_arm_length_pixel = getDistance(shoulderpoints.right_shoulder.x, shoulderpoints.right_shoulder.y, hand_points.right_hand.x, hand_points.right_hand.y)
right_arm_length_cm = right_arm_length_pixel * cm_per_pixel
print("오른팔길이: {}" .format(right_arm_length_cm))

###############################################################################

#원본 이미지 띄우기
#cv2.imshow("OriginalImage", srcImage)

# 처리된 이미지 띄우기
cv2.namedWindow("ProcessedImage") # 이미지 윈도우 이름 지정
cv2.setMouseCallback("ProcessedImage", onMouse, param=None) # 마우스 콜백함수 지정
cv2.imshow("ProcessedImage",pcImage)
cv2.waitKey(0)