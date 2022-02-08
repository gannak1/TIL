# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 13:14:30 2021

@author: gi930
"""

# 14. drop, shift, rename

# 기타 메소드

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

run my_modules #Spyder의 경우 우측 상단의 폴더를 설정해줘야 함

emp = pd.read_csv('C:/Users/gi930/OneDrive/바탕 화면/Multicampus/code/20211227/emp.csv')

emp

# scott 퇴사

emp.loc[emp['ename'] == 'scott'] # scott 관련된 record

emp['ename'] == 'scott' #조건문

emp.loc[emp['ename'] == 'scott',:]
emp.loc[~(emp['ename'] == 'scott'),:]

emp.drop(4,axis=0) # 행기준, 4번째 idx 제외

#[예제]
# emp 데이터셋에서 sal 컬럼 제외 (iloc)
emp
emp.drop('sal',axis=1)
emp.iloc[:,:-1]

emp.loc[:,'empno':'deptno']

emp.drop(['ename','deptno'],axis=1)

# shift
# - 행 또는  열을 이동
# - 전일자 대비 증감율


emp
emp['sal'].shift() # default : axis=0 (행)


# [예제 - 다음 데이터 프레임에서 전일자 대비 즘감율]
s1 = Series([3000,3500,4200,2800,3600], index=['2021/01/01','2021/01/02','2021/01/03','2021/01/04','2021/01/05'])
s1

# 1월 2일 증감율 >> (3500-3000)/3000
s1.shift()
((s1-s1.shift())/s1.shift()) * 100
'''
2021/01/01          NaN
2021/01/02    16.666667
2021/01/03    20.000000
2021/01/04   -33.333333
2021/01/05    28.571429
dtype: float64
'''

# 3. rename
# - 행, 컬럼명 변경

emp
emp.columns = ['emptno','ename','deptno','salary']
emp

emp.rename?

emp.rename({'salary':'sal','deptno':'dept_no'},axis=1)

# [예제] emp 데이터에서 ename을 index로 설정 후 scott을 SCOOT 변경해보세요
emp.set_index('ename').rename({'scott':'SCOTT'},axis=0)

emp.rename({'scott':'SCOTT'},axis=0)
