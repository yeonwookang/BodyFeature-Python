# BodyFeature
DSWU Computer Science FYP

 Duksung Women's University
 Computer Science 2017 Final Year Project
 - 2D auto body measurement system

# Mirae 프로그램

## 기존 연우언니 프로그램에서 진행한 것
 - 사진 경로 지정 (imgPath 변수)  (이미지의 크기는 525x700 픽셀)
 - 콘솔창에 키 입력
 - 콘솔창에 자동으로 구해진 치수 출력 (총장, 어깨너비, 양팔 길이)
 - 마우스 클릭&드래그로 치수 측정 가능
 - 현재 머리, 양쪽 손끝, 발끝, 어깨점 추출 완료

## 현재 브랜치에서 진행된 상태
   -현재 겨드랑이점을 찾고 있음

 ### 오류: 겨드랑이점을 제대로 찾지 못하고 있음
-해결방법:
<li>해당 이미지의 배경처리와 c++코드의 이미지 처리로 인해서 값이 변경되면서 해당 코드를 수정 중</li>
<li>기존 연우언니 코드에서 처리되는 초록색 컨투어 값을 이용하여 [(예시)if (data[middlepoint1.x - j] == 255)]값을 처리해볼 생각임</li>
<li>c++코드에서 if 배경일경우~를 처리하는 부분은 "if 컨투어 값 이외의 값을 입력받으면~" 이라는 식으로 진행해볼 예정</li>

-오류 사진
![image](https://user-images.githubusercontent.com/26568793/32992016-fd9df098-cd88-11e7-8c89-717804c6d4b0.png)
![image](https://user-images.githubusercontent.com/26568793/32992045-2e0c0be8-cd89-11e7-9be9-8c4d876f28fa.png)


