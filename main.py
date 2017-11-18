# coding=utf-8
# Main class

import cv2
import bodycontour as bc # 윤곽선을 구하는 기능
import bodyposition as bp # 신체의 특정점들을 가져오는 기능
import math
from PIL import Image # 이미지 모듈 라이브러리
import numpy as np
import copy

# 마우스 클릭 이벤트 처리를 위한 변수
ix, iy = -1, -1
mode = False
length = 0

# 사용자로부터 입력받은 키와 픽셀/키 값을 저장할 변수
height = 0
pixel_per_cm = 0

# 사용자로부터 이미지를 받아옴
# 빠른 테스트를 위해 이미지 경로 지정
# 이미지 원본은 srcImage에 저장함
imgPath = "body.jpg"
srcImage = cv2.imread(imgPath, 1)

# 사용자로부터 받아온 이미지를 처리하여
# 윤곽선을 구해온 이미지를 저장 (윤곽선을 여기서는 RGB(0, 255, 0) 형광 초록으로 하여 눈에 잘 띄게 하겠음)
pcImage = bc.getProcessedImage(srcImage)

def onMouse(event, x, y, flag, param):
    global ix, iy, mode,  srcImage, pcImage, length, height, pixel_per_cm

    if event == cv2.EVENT_LBUTTONDOWN:
        mode = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if mode:
            cv2.imshow("ProcessedImage", pcImage)

    elif event == cv2.EVENT_LBUTTONUP:
        mode = False
        cv2.line(pcImage, (ix, iy), (x, y), (0, 0, 255), 2)
        cv2.imshow("ProcessedImage", pcImage)

        # 시작점 - 끝점 거리 구하기
        length = math.sqrt((ix-x)*(ix-x)+(iy-y)*(iy-y))
        print("----length(pixel)----")
        print(length)
        print("----length(cm)-------")
        print (length*pixel_per_cm)
        print("---------------------")
    return


# 윤곽선이 구해진 이미지를 사용해 특정점 구하기를 시작

# 손 찾아 점 찍기
hand_point = bp.getHandPoints(pcImage) # 손의 좌표를 가져옴
cv2.circle(pcImage, (hand_point.left_hand.x, hand_point.left_hand.y), 3, (0, 0, 255), -1) #왼손 찍기
cv2.circle(pcImage, (hand_point.right_hand.x, hand_point.right_hand.y), 3, (0, 0, 255), -1) #오른손 찍기

# 정면 키 찾아 점 찍기
frontheight_point = bp.getFrontHeightPoints(pcImage) # 정면 키 좌표를 가져옴
cv2.circle(pcImage, (frontheight_point.front_head.x, frontheight_point.front_head.y), 3, (0, 0, 255), -1) #머리점 찍기
cv2.circle(pcImage, (frontheight_point.front_head.x, frontheight_point.front_foot.y), 3, (0, 0, 255), -1) #발끝점 찍기 - 발끝의 x는 머리의 x로 둠

#중앙점 찾아 선 긋기 - 수정 필요
#middlepoint = bp.getMiddlePoint(pcImage)
#cv2.line(pcImage, (0, middlepoint.y), (700, middlepoint.y), (255, 0, 0), 3) #키 - 발끝의 x는 머리의 x로 둠

#머리, 어깨, 허리, 손, 무릎, 발목, 발 선 긋기
cv2.line(pcImage, (hand_point.left_hand.x, hand_point.left_hand.y), (hand_point.right_hand.x, hand_point.right_hand.y), (255, 0, 0), 1) #손
cv2.line(pcImage, (frontheight_point.front_head.x, frontheight_point.front_head.y), (frontheight_point.front_head.x, frontheight_point.front_foot.y), (255, 0, 0), 1) #키 - 발끝의 x는 머리의 x로 둠

#임의 선
cv2.line(pcImage, (frontheight_point.front_head.x, frontheight_point.front_head.y), (hand_point.left_hand.x, hand_point.left_hand.y), (255, 200, 0), 1) #머리-왼손
cv2.line(pcImage, (frontheight_point.front_head.x, frontheight_point.front_head.y), (hand_point.right_hand.x, hand_point.right_hand.y), (255, 200, 0), 1) #머리-오른손
cv2.line(pcImage, (frontheight_point.front_head.x, frontheight_point.front_foot.y), (hand_point.left_hand.x, hand_point.left_hand.y), (255, 200, 0), 1) #왼손-발
cv2.line(pcImage, (frontheight_point.front_head.x, frontheight_point.front_foot.y), (hand_point.right_hand.x, hand_point.right_hand.y), (255, 200, 0), 1) #오른손-발

# bodyPosition의 getPixelPerCm()를 이용하여 픽셀 수를 구해봄
# 입력받은 키 / 머리에서 발까지 길이 = cm당 픽셀 수
# 사용자에게 키 입력 받기
height = input(">> INSERT HEIGHT(cm): ")
height = float(height)

# 발-머리 거리 구하기
print("---distance(head-foot)---")
distance = float(frontheight_point.front_foot.y - frontheight_point.front_head.y)
print(distance)
print("-----pixel per cm-----")
pixel_per_cm = float(height/distance)
print(pixel_per_cm)
print("------------------------")

#원본 이미지 띄우기
#cv2.imshow("OriginalImage", srcImage")

# 처리된 이미지 띄우기
cv2.namedWindow("ProcessedImage") # 이미지 윈도우 이름 지정
cv2.setMouseCallback("ProcessedImage", onMouse, param=None)
cv2.imshow("ProcessedImage",pcImage)
cv2.waitKey(0)

print("length: ", length)
