# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 17:13:25 2022

@author: gi930
"""
# 재귀 3
## 함수
def addNumber(num):
    if num <= 1:
        return 1
    return num + addNumber(num-1)

print(addNumber(10))

# 팩토리얼

def Factorial(num):
    if num == 1:
        return 1
    else:
        return num * Factorial(num-1)
    
    
print(Factorial(5))

#로켓 카운트다운

def countdown(num):
    if num <= 0:
        print('발사!')
    else:
        print(num) 
        return countdown(num-1)


countdown(5)


# 별모양 출력

def star(num):
    if num <= 1:
        print('*')
        return
    else:
        print(num*'*')
    return star(num-1)

star(5)


# 구구단
def gugu(dan,num):
    if num <= 1:
        print(dan*num)
    else:
        print(dan*num)
        return gugu(dan,num-1)

gugu(9,9)

# 제곱 계신
def pow(x,n):
   if n <= 0:
        return 1
   else:
       return  pow(x,n-1) * x

print(pow(5,3))

# 배열 합
def arySum(arr,n):
    if n <= 0:
        return arr[0]
    else:
        return arr[n] + arySum(arr,n-1)

print(arySum([1,2,3,4,5,6,7,8,9,10],9))