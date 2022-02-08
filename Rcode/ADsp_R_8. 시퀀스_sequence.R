# 수열 생성

10:30

30:10

5:-5

# rep: 특정 값 반복 
rep(1,5)
rep(100, 10)

# times 인자 : 앞에 나온 숫자를 몇번 반복할지를 정하는 인자
rep(c(10,20), times=5)

# each 인자 : 앞에 나온 숫자 각각을 몇번 반복할지를 정하는 인자
rep(c(1,3), each=5)


rep(c("aaa", "bbbb"), times=3) #숫자 뿐만아니라 문자열도 반복 가능하다.

# seq: 시작 숫자와 끝 숫자를 정해주면 숫자를 생성

seq(2,10) #시작 숫자와 끝숫자를 정해주면 1씩증가시켜서 수열을 만든다.


seq(from=3, to=10)
seq(from=2, to = 10, by=3) # 3자리 씩 건너 뛰어서 

seq(from=2, to=10, length.out= 4) 
# length.out: 수열의 갯수를 4개로 만든다 

seq(from=1, by=2, length.out = 10)
seq(from=1, to=10, length.out= 3)
seq(from=1, to=10, length= 5)

