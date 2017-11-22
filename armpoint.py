# coding=utf-8

#분기점을 찾는 클래스

import numpy as np
import copy

class allarmpit:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#겨드랑이 좌표
class armpit:

    def __init__(self, leftarmpit, rightarmpit):
        self.leftarmpit = leftarmpit
        self.rightarmpit = rightarmpit

#armpit 검색 지점
class find_armpit_start_line:
    def __init__(self, left_start_line, right_start_line):
        self.left_start_line = left_start_line
        self.right_start_line = right_start_line

#양쪽의 겨드랑이 point 반환
def GetArmpit(pcImage,start_line):
    outImage = copy.copy(pcImage)  # 객체 복사하기

    #왼쪽 겨드랑이 찾기
    leftarm=allarmpit(0,0)
    leftarm=get_left_arm_point(outImage,start_line.left_start_line)

    #오른쪽 겨드랑이 찾기
    rightarm=allarmpit(0,0)
    rightarm=get_right_arm_point(outImage,start_line.right_start_line)

    my_armpit= armpit(0,0)

    print("------GetArmpit------")
    my_armpit.leftarmpit=leftarm
    my_armpit.rightarmpit=rightarm

    return my_armpit

#왼쪽 겨드랑이 좌표 찾기
def get_left_arm_point(edge,start_line):
    outImage = copy.copy(edge)

    print("-------in get_left_armpoint-------")

    rowNumber = 700L
    colNumber = 525L

    leftpoint1=allarmpit(0,0)
    rightpoint1=allarmpit(0,0)
    middlepoint1=allarmpit(int(colNumber/2),start_line-50) #왜 50을 빼는지 모르겠음...

    #왼쪽 팔 검색
    for i in range(middlepoint1.y,0,-1):
        data=outImage[i]
        for j in range(middlepoint1.x,0,-1):
            if 167 in data[j]:
                rightpoint1.x=j
                rightpoint1.y=i

                while j > 0:
                  j = j - 1
                  if np.any(data[j]==255):
                     leftpoint1.x = j
                     leftpoint1.y = i
                     break

                middlepoint1.x = ((rightpoint1.x + leftpoint1.x) / 2)+1
                middlepoint1.y = i+1
                print("middlepoint.x")
                print(middlepoint1.x)
                print(middlepoint1.y)
                break
        if rightpoint1.x != 0 and leftpoint1.x != 0:
            break

    for i in range(middlepoint1.y, 0, -1):
        data = outImage[i]
        print("실행")
        print(i)
        # middlepoint1.x=middlepoint1.x-2
         # data[middlepoint1.x]=255 왼쪽 및 오른쪽으로 검색한다.
        print(data[middlepoint1.x-1])
        if np.any(data[middlepoint1.x]==255):
            print(middlepoint1.x)
            print(data[middlepoint1.x])
            print(i)
            middlepoint1.y = i


            # 왼쪽으로 열개의 점을 찾는다.
            count = 0
            for j in range(1, 10):
                #해당 배열에는 41이라는 값이 들어 있어야 작동함
                if np.any(data[middlepoint1.x-j]!=255):
                    count = count + 1

            if count > 5:
                leftpoint1.x = middlepoint1.x
                leftpoint1.y = middlepoint1.y
                for j in range(1, colNumber):
                    print("-------------------")
                    print(j)
                    print(middlepoint1.x)
                    print(middlepoint1.x+j)
                    print(data[middlepoint1.x+j])
                    if np.any(data[middlepoint1.x+j]==255):
                        print("****************")
                        print("i am here in if ")
                        print("-----j------ ")
                        print(j)
                        rightpoint1.x = middlepoint1.x + j
                        rightpoint1.y = middlepoint1.y
                        print(rightpoint1.x)
                        print(rightpoint1.y)
                        print("---------------")
                        break # tag==1로 하고 while문으로 해서 변경해보기

            # middlepoint1은 right leg의 경계
            else:
                print("i am here line 115")
                rightpoint1.x = middlepoint1.x
                rightpoint1.y = middlepoint1.y
                # 무한 루프
                while True:
                    j = 1
                    if np.any(data[middlepoint1.x-j]==255):
                        leftpoint1.x = middlepoint1.x - j
                        leftpoint1.y = middlepoint1.y
                        break
                    j = j + 1
            middlepoint1.x = int((leftpoint1.x + rightpoint1.x) / 2)
        else:
            print("i am here line 129")
            pass  # 여기의 역할을 모르겠음

            # 다리의 분기점을 찾습니다.

        if middlepoint1.x == leftpoint1.x or middlepoint1.x == rightpoint1.x:
            print("i am here line 135")
            break
        else:
            pass

    left_arm = allarmpit(0, 0)
    left_arm.x = middlepoint1.x
    left_arm.y = middlepoint1.y

        # 출력 테스트
    print(left_arm.x)
    print(left_arm.y)

    return left_arm


#오른쪽 겨드랑이 좌표 찾기
def get_right_arm_point(edge,start_line):
    outImage = copy.copy(edge)
    print("-------in get_right_armpoint-------")

    rowNumber = 700L
    colNumber = 525L

    leftpoint1 = allarmpit(0, 0)
    rightpoint1 = allarmpit(0, 0)
    middlepoint1 = allarmpit(int(colNumber / 2), start_line - 50)

    # 왼쪽 팔 검색
    for i in range(middlepoint1.y, 0, -1):
        data = outImage[i]
        for j in range(middlepoint1.x, colNumber-1, -1):
            if np.any(data[j] == 0):
                leftpoint1.x = j
                leftpoint1.y = i

            while j > 0:
                j = j - 1
                if 255 in data[j]:
                    rightpoint1.x = j
                    rightpoint1.y = i
                    break
            middlepoint1.x = (rightpoint1.x + leftpoint1.x) / 2
            middlepoint1.y = i
            break
        if rightpoint1.x != 0 and leftpoint1.x != 0:
            break

        for i in range(middlepoint1.y, 0, -1):
            data = outImage[i]

            # data[middlepoint1.x]=255 왼쪽 및 오른쪽으로 검색한다.
            if np.any(data[middlepoint1.x]==255):
                middlepoint1.y = i

                # 왼쪽으로 열개의 점을 찾는다.
                count = 0

                for j in range(1, 10):
                    if 255 in data[middlepoint1.x - j]:
                        count = count + 1
                if count > 5:
                    leftpoint1.x = middlepoint1.x
                    leftpoint1.y = middlepoint1.y

                    for j in range(1, colNumber):
                        if np.any(data[middlepoint1.x+j]==255):
                            rightpoint1.x = middlepoint1.x + j
                            rightpoint1.y = middlepoint1.y
                            break
                # middlepoint1은 right leg의 경계
                else:
                    rightpoint1.x = middlepoint1.x
                    rightpoint1.y = middlepoint1.y
                    # 무한 루프
                    while True:
                        j = 1
                        if 255 in data[middlepoint1.x - j]:
                            leftpoint1.x = middlepoint1.x - j
                            leftpoint1.y = middlepoint1.y
                            break
                        j = j + 1

                middlepoint1.x = int((leftpoint1.x + rightpoint1.x) / 2)
            else:
                pass  # 여기의 역할을 모르겠음

            # 다리의 분기점을 찾습니다.

            if middlepoint1.x == leftpoint1.x or middlepoint1.x == rightpoint1.x:
                break
            else:
                pass

        right_arm = allarmpit(0, 0)

        right_arm.x = middlepoint1.x
        right_arm.y = middlepoint1.y

        # 출력 테스트
        print(right_arm.x)
        print(right_arm.y)

        return right_arm

def search_arm(edge):
    outImage = copy.copy(edge)
    data = outImage[175]
    for i in range(160,400):
        print("print data[i]")
        print(data[i])
        print(i)

        if(np.any(data[i])==255):
            print("!!!!!!HERE contour!!!!!!!!!")
            print("print data[i]")
            print(data[i] + "," + i)


