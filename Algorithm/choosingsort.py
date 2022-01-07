import random
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:15:58 2022

@author: gi930
"""
## 선택정렬1 (가장 쉬운 정렬이지만, 실제로 써도 됨)
## 함수
def findMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if ary[minIdx] > ary[i]:
            minIdx = i
    return minIdx

## 전역
before = [random.randint(1,99) for _ in range(20)]
after = []
## 메인
print('정렬 전 -->',before)
for _ in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])


print('정렬 후 -->',after)