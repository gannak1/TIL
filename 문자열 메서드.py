# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 15:32:08 2021

@author: gi930
"""

# 문자열 메서드
# 문자열 처리와 관련된 메서드

# 1. 기본 메서드 : 벡터 연산 불가(매 원소마다 반복 불가)

'abc'.upper()
'a/b/c'.split('/')
'a/b/c'.split('/')[1]

l1 = ['abc','def']
l2 = ['a/b/c','d/e/f']

l1.upper() #불가
l2.split('/') # 불가

list(map(lambda x:x.upper(),l1))
list(map(lambda x:x.split('/'),l2))

# pandas 메서드 : 벡터화 내장(매 원소마다 반복 가능)
# Series, DataFrame

# 1) split

from pandas import Series, DataFrame

l1
Series(l1)
#0    abc
#1    def
#dtype: object

s1 = Series(l1)

l2
Series(l2)

s2 = Series(l2)

s2.str.split('/')

# 2) 대소 치환
s1.str.upper()
s1.str.lower()
s1.str.title() # 카멜 형식(낙타 형태)

# 3) replace
s1.str.replace('a','A')

s1.str.replace('a','') # very ^ 100

# 예제 - 천단위 구분기호 처리
s3 = Series(['1,200','3,000','4,000'])
s3.sum()
# 천 단위 구분기호 떄문에 문자로 입력된 값이라 문자열 결합으로 인식됨
# 구분기호 문제, 문자로 인식, 더해줘야 하네
s3.str.replace(',',"").astype('int').sum()

#s3 = s3.str.replace(',','')
#sum(list(map(lambda x: int(x),s3)))

# 4) 패턴 확인 : startswith, endswith, contains
s1
s1.str.startswith('a')
s1[s1.str.startswith('a')] # s1 각 원소에서 'a'로 시작하는 원소 추출
s1[s1.str.endswith('c')] # s1 각 원소에서 'c'로 끝나는 원소 추출
s1[s1.str.contains('e')] # s1 각 원소에서 'e'를 포함하는 원소 추출

# 문자열 크기 len()
s1.str.len()

# count 포함 개수
Series(['aabbbb','abcddd']).str.count('a')

# 재거 함수 (공백, 문자)
Series(['       cd            ','       df          '])
Series(['       cd            ','       df          ']).str.strip()
Series(['       cd            ','       df          ']).str.strip().str.len()

s1

s1.str.strip('a') #문자열 제거
Series(['aaaaaabaaaaaaaaacd','abcdaa']).str.strip('a')
# 문자열 제거()
Series(['aaaaaabaaaaaaaaacd','abcdaa']).str.replace('a',"")

#find(위치값 리턴)
s3 = Series(['abc@gmail.com','abcdef@gmail.com'])
s3.str.find('@')

# 문자열 색인(추출) find('a',b) Series내에 b번째에 있는 a의 위치를 반환
'abcde'[0:3] # 문자열 색인
s3
s3[0:3] # Series에서 1번쨰, 2번째, 3번째 원소 추출
s3.str[0:4] # Series에서 각 원소마다 1번째, 2번째, 3번째 문자열 추출

# 이메일 아이디 추출
s4 = Series(['drwill@naver.com','zzuyu@drwill.kr'])
s4
#Id = Series(s4.str.split('@')[:][0])
#email = Series(s4.str.split('@')[:][1])

vno=s4.str.find('@')

list(map(lambda x, y : x[0:y],s4,vno))

s4.map(lambda x : x[:x.find('@')])
s4.str.find('@')

s4.str[0:s4.str.find('@')]
s4.str[0:s4.str.find('@')[0]]
s4.str[0:s4.str.find('@')[1]]
s4.str[0:s4.str.find('@')[1]][0]
s4.str[0:s4.str.find('@')[1]][1]

# pad : 문자열 삽입

#s1.str.pad(5,      #최대 글자수 abc!!
#           'left', #삽입방향
#           '!')    #삽입글자

s1

s1.str.pad(5, 'right','?') # 양이 적어지면 추가 안함

s1.str.pad(6,'right','^')

# 문자열 결합
'a' + 'b'
'a'*3

s5 = Series(['abc','def','123'])
s5.str.cat() # 문자열을 붙여서 출력
s5.str.cat(sep=',')
s5.str.cat(sep='/')

s6=Series([['a','b','c'],['d','e','f']])
s6
s6.str.join(sep='')     # Series 내 각 원소 내부의 문자열을 결합 (공백)
s6.str.join(sep=',')    # Series 내 각 원소 내부의 문자열을 결합 (ㅡ)
#s6=Series(['a','b','c'],['d','e','f']) index 자리에 def가 삽입됨
# 외부 파일 입출력
#1) 파일 불러오기
# np.loadtxt(fname,      # 파일명
#            dtype,           # 데이터 타입
#            delimeter,       # 필드 구분 기호
#            skiprows,        # skip 할 행의 수
#            usecols,(사용할 ) # 선택할 컬럼 값(위치)
#            encoding)(인코딩) # 인코딩 옵션
import numpy as np
np.loadtxt('C:/Users/gi930/OneDrive/바탕 화면/Multicampus/code/20211220/file1.txt',delimiter=',',dtype='str') 
# '%s' : 문자타입(string)


2) 파일 내려쓰기
np.savetxt(fname,       # 파일명
           X,           # 객체명
           delimiter,   # 구분자
           fmt,         # 출력형식(format)
           header,      # 헤더 출력 여부(file 첫 문자열)
           encoding)    # 인코딩 옵션

np.savetxt('file2.txt',a2,delimiter=',',fmt='%s')
# '%s' : 문자타입(string)

# [참고: fmt 전달/변경 방식]
# %s : 문자열
# %f : 실수(float)
# %d : 정수
'%s' % 123 #'123'
'%f' % 123 # '123.000000'
'%.2f' % 123 # '123.00'  #소수점 2째 자리까지 출력
'%d' % 123.000 # '123'   
'%7d' % 123 # '    123'




# 11) 문자열 결합 
'a' + 'b'
'a' * 3

s4 = Series(['abc', 'def', '123'])
s4.str.cat()         # Series 내 서로 다른 원소를 결합
s4.str.cat(sep='/')  # Series 내 서로 다른 원소를 결합(분리구분기호 함께)

s5 = Series([['a','b','c'], ['d','e','f']])
s5
s5.str.join(sep='')  # Series 내 각 원소 내부의 문자열을 결합
s5.str.join(sep=',') # Series 내 각 원소 내부의 문자열을 결합
