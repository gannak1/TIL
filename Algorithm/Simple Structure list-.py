# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 10:00:47 2022

@author: gi930
"""

### 함수부분
def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen - 1] = friend

def insert_dat(position,friend):
    katok.append(None)
    kLen = len(katok)
    for i  in range(kLen-1, position , -1):
        katok[i] = katok[i-1]
        katok[i-1]= None
    katok[position] = friend

def delete_data(position):
    katok[position] = None
    klen = len(katok)
    for i in range(position + 1, klen,1):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[klen-1])
    
## 전역 변수 부분

# 매인코드 부분
katok = ['다현','정연','쯔위','사나','지효']
katok.append(None) # 빈칸추가

katok[5] = '모모'
a = []
a.append()
katok

katok.append(None)
katok[6] = katok[5]
katok[5] = katok[4]
katok[4] = katok[3]
katok[3] = '미나'
katok
add_data('모모')
katok
insert_dat(3,'미나')
katok
delete_data(4)
katok



