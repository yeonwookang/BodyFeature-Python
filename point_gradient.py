# coding=utf-8
import copy
import numpy as np

#차이점을 찾기 위헤서 몸체 측면 사이의 기울기를 찾는 알고리즘입니다.
#두 개의 가로 좌표가 같으면 기울기는 무한대이며 INF로 설정합니다.
INF=100000

class Dstpoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


#세개의 함수가 존재합니다.

def get_gradient(p1,p2):
    print("|--- in get_gradient ---------|")
    k=0

    if p1.x==p2.x:
        k=INF
    else:
        k=(p1.y-p2.y)+1.0/(p1.x-p2.x)
    #기울기를 구한 후 반환한다. -> 해당 데이터를 모아 학습시키는 방법은..?
    return k


def Get_Left_PointGradient(edge):
    outImage = copy.copy(edge)  # 객체 복사하기


    # 사진의 픽셀 수
    rowNumber = 840L
    colNumber = 641L

    #p1은 이전노드 p2는 이후 노드로 구성
    p1=Dstpoint(0,0)
    p2=Dstpoint(0,0)

    #k1은 이전 선분의 기울기, k2는 현재 두점 사이의 기울기
    k1=0.0
    k2=0.0

    #해당 값을 넣을 수 있는 벡터 생성: 빈 배열
    Left_Gradient_Collention=np.array([])

    #모든 픽셀 값을 순횐한다.

    for i in range(0,rowNumber):
        data=outImage[i]

        for j in range(0,colNumber):
            if 255 in data[j]:
                p2.x=j
                p2.y=i

                k2=get_gradient(p1,p2)

                if(k1==k2):
                    #마지막 값을 삭제하게 해야한다.
                    size=Left_Gradient_Collention.size
                    np.delete(Left_Gradient_Collention,size,0)
                    #그리고 새로운 요소를 집어넣습니다.
                    np.insert(Left_Gradient_Collention,)





def Get_Right_PointGradient(edge):
     pass