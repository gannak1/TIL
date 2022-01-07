# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 17:00:33 2022

@author: gi930
"""
#재귀 1 
## 함수 선언부
def openBox():
    print('상자열기 ~~')
    openBox(
        )


## 메인 코드부
openBox()


#재귀 2
## 함수
def openBox():
    global count
    print('상자열기 ~~')
    count -= 1
    if count == 0:
        print('반지 넣기 ~~~')
        return
    openBox()
    print('!!!상자닫기 ')
    return
## 전역
count = 5

## 메인
openBox()