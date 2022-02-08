# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 11:21:53 2021

@author: gi930
"""

# 17. 날짜표현
# 월벼르 일별, 요일별 집계
# 현재 날짜 - 입사일자 = 근무 일자

# 현재 날짜
import pandas as pd
import numpy as np
from pandas import Series,DataFrame

from datetime import datetime
datetime.now()
# datetime.datetime(2021, 12, 29, 11, 25, 34, 726107)

d1 = datetime.now()
type(d1)

d1.year         #연
d1.month        #월
d1.day          #일

# 2. 날짜 파싱
d2='2022/01/01'
d2.year
# AttributeError: 'str' object has no attribute 'year'

#datetime.strptime(date_string, format)
# 벡터 연산이 안됨

datetime.strptime(d2,'%Y/%m/%d')
# Out[81]: datetime.datetime(2022, 1, 1, 0, 0)

datetime.strptime('09/12/25','%m/%d/%y') # 2025년 9월 12일 해석 실제 -> 2009년 12월 25일

# Series 벡터 연산 불가
# 해결방안 map
s1 = Series(['2022/01/01','2022/01/02','2022/01/03'])
datetime.strptime(s1,'%Y/%m/%d')
# TypeError: strptime() argument 1 must be str, not Series

s1.map(lambda x:datetime.strptime(x,'%Y/%m/%d'))
'''
0   2022-01-01
1   2022-01-02
2   2022-01-03
dtype: datetime64[ns]
'''

# 2) pd.to_datetime
# 벡터 연산가능
s1
pd.to_datetime(s1)
s2 = pd.to_datetime(s1)
'''
0   2022-01-01
1   2022-01-02
2   2022-01-03
dtype: datetime64[ns]
'''
'''
pd.to_datetime(s2,format = '%Y/%m/%d')

# Series라서 변환 안됨
s2 = pd.DataFrame({'date':['01-05-21','01-06-21','01-07-21']})
type(s2)
s2
'''

s3 = pd.DataFrame({'date' : ['01-05-21','01-06-21','01-07-21',]})
s3.dtypes
s3


# 3) 날짜 포맷 변경 datetime.strftime(string format time)
# 요일 추출(날짜에서 요일을return 하도록 날짜 출력 형식 변경)
# *(연/월/일) --> (월/일/연) 순서로 변경
# (주의) 날짜 포맷 변경 한 후 return 데이터 타입은 무조건 문자라는 사실 !!!

d1 = datetime.now()
d1
datetime.strftime(d1,'%A') # 요일 리턴 # Wednesday
datetime.strftime(d1,'%a') # 요일 리턴 # Wed
datetime.strftime(d1, '%m-%d,%y') # 12-29-2021
# %y = 뒤의 연도만 나옴 ex) 2021 > 21 %Y 모두나옴 ex)2021 > 2021

datetime.strftime(d1, '%Y') # 연도 리턴(완전체) '2021'
datetime.strftime(d1, '%y') # 연도 리턴(완전체) '21'

s2
datetime.strftime(s2,'%Y') 
# TypeError: descriptor 'strftime' for 'datetime.date' objects doesn't apply to a 'Series' object
s2.map(lambda x: datetime.strftime(x,'%Y'))

#timedelta  날짜 연산
#dateoffset 날짜 연산 시험에는 안나옴

## 4) 날짜 연산 매우 중요
d1          # 현재 날짜
d1 + 100    # 100일 기념일 프로그램 만들어야 하는데 안됨
# 타입이 틀려서 연산 불가

# 1) offset

from pandas.tseries.offsets import Day,Hour,Second
d1 + Day(100) # Out[133]: Timestamp('2022-04-08 11:42:50.552239')

# 2) timedelta (날짜와의 차이)

from datetime import timedelta

d1 + timedelta(100) #Out[135]: datetime.datetime(2022, 4, 8, 11, 42, 50, 552239)

# 3) (실무용) DateOffset 매우중요
d1 + pd.DateOffset(months = 4)

# 5. 날짜 - 날짜
d1 - datetime.strptime(d2,'%Y/%m/%d')
d3 = d1 - datetime.strptime(d2,'%Y/%m/%d')

d3.days
d3.seconds

# [연습문제]
# 요일별 통화건 수 총합

deli = pd.read_csv('C:/Users/gi930/OneDrive/바탕 화면/Multicampus/code/20211227/delivery.csv', encoding='cp949')
deli.dtypes
deli.head()
deli.info() # 자료의 대략적인 형태를 보여줌

deli.describe()
deli.boxplot()

# 날짜 파싱
deli
pd.to_datetime(deli['일자'])
pd.to_datetime(deli['일자'],format = '%Y%m%d')
deli['일자'] = pd.to_datetime(deli['일자'],format = '%Y%m%d')

# 요일 리턴
datetime.strftime(deli['일자'],'%A')

deli['일자'].map(lambda x : datetime.strftime(x,'%A'))
deli['요일'] = deli['일자'].map(lambda x : datetime.strftime(x,'%A'))
# 요일별로 그룹화 (통화건수)

total = deli.groupby('요일')['통화건수'].sum()
total[['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']] # sort는 요일별로 정렬기능이 지원하지 않는다 고로 직접 재배치를 해줘야 한다.



# 일자별 통화건수 알고 싶어요.
deli.groupby('일자')['통화건수'].sum()
deli



