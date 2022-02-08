# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 02:31:18 2022

@author: gi930
"""

b = np.array(np.arange(1,10).reshape(3,3))


np.where(b>5,b,'B')


a2.sum(axis=0) # 행기준, 행 별 총함(서로 다른 행끼리, 세로방향 연산)
a2.sum(axis=1) # 옇기준, 열 별 총함(서로 다른 열끼리, 가로방향 연산)

# [축 번호]
# 2차원 : 행(0) 열(1)
# 3차원 : 층(0) 행(1) 열(2)

# 8. 전치 메서드
1) T : 행과 열을 전치

a1 = np.arange(1,9).reshape(4,2)
a1
a1.T

# 2) swapaxes: 두 축을 전달 받아서 두축을 서로 전치, 전달 순서는 중요치 않음
a1.swapaxes(0,1)
a1.swapaxes(1,0)

# 3) transpose
# 원본의 차원에 맞는 축번호를 인수에 차례대로 전달. 그리고 그대로 전치 전달되는 순서 중요
a1.transpose(0,1) # 원본 그대로 출력
a1.transpose(1,0) # 행과 열 전치

# 외부 파일 입출
# np.load



# np.savetxt(fnbame,      #파일명
#           X,           # 객체명
#           delimiter,   #구분자
#           fmt,         # 출력형식(format)
#           header,      # 헤더출력여부(file 첫 문자열)
#           encoding     # 인코딩옵션
           
           
x = np.arange(0.0,5.0,1.0)
np.savetxt('./data/t',x,delimiter=',',fmt='%s',header=False,encoding=U)
# '%s':문자타입(string)

#[참고 : fmt 전달/변경 방식]
# %s : 문자열
# %f : 실수(float)
# %2f : 2자리 실수
# %d : 정수(int)
# %10d : 10자리 정수


s4 = Series ([10,20,30,40])
s5 = Series ([10,20,30,40],index= ['c','d','e','f'])

s1 + s4 # key가 같은 값끼리 연산가능
s3 + s5 # key가 다른경우 모두 Na 반환
# 해당하는 key값이 없으면 NaN 반환 Na = 아예 없는 수치 NaN = 한쪽만 있지만 나머지는 Na, Dtype가 쓸 수 없는 Data
s3.add(s5,fill_value=0)    
# 양쪽 모두 존재하지 않는 key 일 경우 
# NA 반환되는 것을 방지하기 위해 fill)value 옵션 사용 적극 추천
s3 - s5
s3.sub(s5,fill_value='0') # - 연산
s3.mul(s5, fill_value=1) # * 연산
s3.div(s5, fill_value=1) # / 연산


df1 = DataFrame(d1)
df1
#    name   sal
#0  smith   900
#1   will  1800

import numpy as np
d3 = DataFrame(np.arange(1,7).reshape(2,3), index=['a','b'],columns=['col1','col2','col3']) # Series 한줄 = 열(columns)
d3

# 색인(indexing) **중요**

d3.col1
#a    1
#b    4

d3['col1']
#a    1
#b    4

d3.['col1','col2','col3']

#iloc loc **중요
# iloc : positional indexing
# loc : label indexing
d3

d3.iloc[:,0]
d3.iloc[:,0:3]
d3.iloc[:,[0,-1]]
d3.iloc[:,[0,2]]

d3.loc[:,['col1','col3']]

#조건색인 처리
d3.loc[d3.col1 ==1,:]

# 기본 메서드
d3.dtypes # 각 column 별 데이터 타입 확인
d3.index
d3.columns
d3.values

d3.columns=['A','B','C'] # 컬럼 이름 변경
d3

# 연산
d3 + 10

d4 = DataFrame({'A':[10,40],"B":[20,30],'C':[30,80]},index=['a','b'])
d5 = DataFrame({'A':[10,40],"B":[20,30]},index=['a','b'])

d3 + d5
d3.add(d5,fill_value=0)
d3.sub(d5,fill_value=0)
d3.mul(d5,fill_value=1)
d3.div(d5,fill_value=1)


s3 = Series([['a','b','c'],['A','B','C']])
s3.str.find('a')
s3.str.join('')
s1.str.upper().str.lower()
class name():
    def __init__(self):
        self.ssss # class 시작과 함께 만들어짐 name.ssss변수가 만들어짐
def :