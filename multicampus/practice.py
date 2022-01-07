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
s1.str.contains() # 특정 문자열이 들어 있는지 검사
s1.str.find() # 특정 문자열이 들어있는것을 1, -1로 리턴
class name():
    def __init__(self):
        self.ssss # class 시작과 함께 만들어짐 name.ssss변수가 만들어짐
def :
    
print(1);print(2)

l1 = ['a','b','c','defg']
s1 = Series(l1)
s1.str.pad(5,'left','!')

s1

s1.str.pad(5,'left'','!')

s1.str.pad(5,'right','^')

s4 = Series(['abc','def','123'])
s4.str.cat() #'abcdef123' >> Series 내의 서로 다른 원소 결합
s4.str.cat(sep='/') # 'abc/def/123' >> Series 내의 서로 다른 원소를 구분기호와 함께 결합


df1.iloc[:,0].sum() #열 전부, 행 하나
df1.iloc[:,0].mean()

df1.iloc[0,0] = np.nan
df1.iloc[:,0].mean()
# skipna = rue (default) NaN이 있으면 Skip하는것이 디폴트, 자동으로 NaN을 무시하고 연산

# 평균균값(최대 최소) 대치
df1.iloc[:,0].mean()
df1.iloc[:,0].isnull() #조건

df1.iloc[:,0][df1.iloc[:,0].isnull()] = df1.iloc[:,0].mean()

df1[df1.isnull()] # 데이터 프레임 전체에서 NaN 값 확인

df1.iloc[:,0].var() #분산
df1.iloc[:,0].std() #표준편차
df1.iloc[:,0].min() #최소
df1.iloc[:,0].max() #최대
df1.iloc[:,0].median() # 중위수(중앙값)


pd.read_csv('./data/emp.csv')    # 현재 지정된 폴더 하위폴더인 data 폴더의 emp.csv 읽어줘
pd.read_csv('file1.txt')         # 현재 지정된 폴더 있는 file1.txt 읽어줘
pd.read_csv("C:/Users/student/Desktop/code/data/emp.csv")

import os


emp = pd.read_csv('./data/emp.csv') 
 
emp.ename
emp['ename']


emp.idx = emp['empno']
emp.idx
emp.iloc[:,1:]

emp.set_index('ename')

emp=emp.set_index('ename')

emp.sort_index()                 # 오름차순(default)
emp.sort_index(ascending=True)   # 오름차순


emp.sort_index(ascending=False) # 내림차순


emp.sort_index(axis=0)
emp.sort_index(axis=1)        # 컬럼 순 정렬 


# 2. sort_values
# - Series, DataFrame 호출 가능 
# - 본문의 값(value) 으로 정렬 (Series, DataFrame 특정 칼럼 순서대로)

emp.sort_values(by='sal')  
emp.sort_values('sal')     # by 생략가능 
emp.sort_values(by='sal', ascending=False)  # 내림차순 정리 
emp.sort_values(by=['deptno','sal'])
emp.sort_values(by=['deptno','sal'], ascending=[True,False])


# python pandas groupby(SQL)
# 그룹연산 실행
# 성별 성적 평균, 학년별 성적 최고점수, 부서별 평균 연봉
# groupby 메서드 처리 가능

import pandas as pd
from pandas import Series, DataFrame

kimchi = pd.read_csv('C:/Users/gi930/OneDrive/바탕 화면/Multicampus/code/20211220/kimchi_test.csv',encoding='cp949')
pd.read_csv('././code/20211220/kimchi_test.csv',encoding='cp949')

kimchi.groupby?


kimchi.groupby(by=None, # 그룹핑 할 컬럼(기준)
               axis = 0 # 그룹핑 연산 방향
              level = None) # 보통 여기까지 사용, # 멀티 인덱스 지원, 멀티 인덱스일 경우, 특정 레벨의 값을 그룹핑 컬럼으로 사용

# 예제) 제품별, 판매처 별(김치별) 수량 총 합
kimchi.groupby(by=['제품']).sum()
#Out[5]: <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000015862D0C580>



kimchi.groupby(by=['제품','판매처'])['수량'].sum()


# 제품기준, 수량과 판매금액 총 합 구하기
kimchi.groupby(by='제품')[['수량','판매금액']].sum()
kimchi.수량.sum()

# 멀티 인덱스
kimchi_2 = kimchi.groupby(by=['제품','판매처'])['수량'].sum()

# 예제) 제품별, 판매처별(김치별) 수량 총 합, 평균
kimchi.groupby(by=['제품','판매처'])['수량'].agg(['sum','mean'])

# agg: 여러 함수들을 동시에 전달

# 예제) 제품별, 판매처별(김치별) 수량 판매금액 총합, 평균
kimchi.groupby(by=['제품','판매처'])[['수량','판매금액']].agg(['sum','mean'])


# 예제) 제품별, 판매처별(김치별) 수량은 총합, 판매금액 평균만 >> dict() 사용
kimchi.groupby(by=['제품','판매처'])[['수량','판매금액']].agg({'수량':'sum','판매금액':'mean'})

# 멀티 레벨을 갖는 경우의 groupby 연산
kimchi_2
type(kimchi_2)
# Series(9,) = (9,1)
kimchi_2.groupby(level=0).sum() # 제품별 총합
kimchi_2.groupby(level='제품').sum() # 제품별 총합
kimchi_2.groupby(level=1).sum() # 판매처별 총합
#level ~= 차원