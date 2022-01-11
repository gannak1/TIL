# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 13:19:52 2021

@author: student
"""

# 13. merge vs. concat
# 행이 서로 분리되어 있는 하나의 데이터프레임으로 합치기  
# 컬럼이 서로 분리되어 있는 하나의 데이터프레임으로 합치기
# 참조 조건 사용, 연관된 두 데이터를 병합(join)

import pandas as pd
import numpy as np 
from pandas import Series, DataFrame 

np.arange(1,7)
np.arange(1,7).reshape(2,3)

DataFrame(np.arange(1,7).reshape(2,3), columns=['A','B','C'])
df1 = DataFrame(np.arange(1,7).reshape(2,3), columns=['A','B','C'])

DataFrame(np.arange(10,61,10).reshape(2,3), columns=['A','B','C'])
df2 = DataFrame(np.arange(10,61,10).reshape(2,3), columns=['A','B','C'])

# concat
pd.concat([df1, df2])  
# 행의 결합 
# 기본은 세로방향으로 합쳐짐
pd.concat([df1, df2], ignore_index=True) 
# 순차적인 인덱스 번호 부여됨

pd.concat([df1, df2], axis=0)  
pd.concat([df1, df2], axis=1)
# 가로방향으로 합쳐짐 (열의 결합)
 
emp = pd.read_csv('./data/emp.csv')
emp

DataFrame({'deptno':[10,20,30], 'dname':['인사부','총무부','IT분석팀']})
df_dept = DataFrame({'deptno':[10,20,30], 'dname':['인사부','총무부','IT분석팀']})

# 조인 
# 두 데이터프레임(테이블) 참조조건 활용, 하
