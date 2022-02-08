# 벡터
c(1,2,3,4)

c('a', 'b','c') #문자 

vector1<-c(11,22,33)
vector1

vector2=c(21,22,11)
vector2

 vector2[2]

vector2[1]

aa<-c(33,44,55,66,77)
aa
aa[-3] #3번째 요소 생략

aa[-1:-2] #1번째 요소와 2번째 요소 생략 
aa[2:4] #2번째 요소부터 4번째 요소 가져오기

aa[3]<-100 #3번째 요소 값 100 삽입
aa

#새로운 내용을 추가
aa <-c(aa, 200)
aa

aa[9]<-99
aa

append(aa, 1111)
aa

append(aa, 5454, after=4)

append(aa, 1111, after=0)

z<-c(TRUE, FALSE)
z

# 벡터 연산

c(1,2,3)+c(4,5,6)
c(1,2,3)+1

x<-c(1,2,3)
y<-c(2,3,4)
x+y

c(1,2,'a') 
# 문자가 하나라도 원소로 있으면 전부 문자로 변경


# 벡터의 길이를 얻는 함수 length()

x
length(x) #원소의 갯수를 알고 싶을 때



