# 확률분포 

# 이항확률분포 
# dbinom( x, size, prob) 확률값구하기
# x=구하고자 하는 변수값, size=n, prob=p
?dbinom
p <- dbinom(c(0,1,2,3), 3, 0.9)
p
names(p)=c(0,1,2,3)
p

barplot(p, col="red", border="black", main="이항확률분포",
        xlab="접속 성공횟수")


# 포아송 분포
# λ = 3 인 포아송 분포 그래프
# (1) 포아송 분포 그래프 (Poisson distribution plot)

# dpois 밀도함수 (density poisson function)
# dpois(x, lambda)

plot(dpois(x=c(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), lambda = 3), 
     type='h', main = "포아송분포, lambda = 3")

# P ( X = 15) 확률 계산 : dpois(x, lambda)
# 동부산 톨게이트의 1시간 당 방문 고객 수가 
# λ = 20 인 포아송 분포를 따른다고 한다.  
# 1시간 당 방문고객수가 15명일 확률은?

dpois(x=15, lambda = 20)

# ppois() 누적분포함수: ppois(q, lambda, lower.tail = TRUE/FALSE)

# P ( X <= 15) 확률 계산 : ppois(q, lambda, lower.tail = TRUE)
# 동부산 톨게이트의 1시간 당 방문 고객 수가 
# λ = 20 인 포아송 분포를 따른다고 한다.  
# 1시간 당 방문고객수가 15명 이하일 확률은?

# (3) P(X =< 15) in Poisson distribution with lambda = 20

ppois(q=15, lambda = 20, lower.tail = TRUE)

# the same result with the ppois()
sum(dpois(x=c(0:15), lambda = 20)) 


# 표준정규분포
install.packages("ggplot2")
library(ggplot2)
ggplot(data.frame(x=c(-4,4)),aes(x=x))+
  stat_function(fun=dnorm, args=list(mean=0, sd=1),
                colour="red", size=1)+
  ggtitle("Graph of Standard Normal Distribution")

# dnorm( x, mean=0, sd=1): 확률밀도함수 구하기
# x=구하고자 하는 변수값

# 인터넷서버에 접속하여 이용하는 평균시간 2분, 표준편차 30초 
# 표준화 변수 z=(X-120)/30 
# 60초 미만 머물 확률을 표준화 
# P(X<60)= P(z=(X-120)/30 < (60-120)/30 ) = P(z<-2) 
pnorm(-2, mean=0, sd=1, lower.tail = T)
#pnorm(q, mean=0, sd=1,lower.tail = T)
#누적확률값 구하기, q: 확률변수값 

# 상위 10%에 해당하는 사용자의 표준화 값과 몇 초를 이용할까? 
# 표준화 값
p<- qnorm(0.1, mean = 0, sd=1, lower.tail = F)
p
# qnorm(p, mean=0, sd=1, lower.tail=T)
# 누적확률이 p가 되는 x값 구하기, p=누적확률

x <- p*60+120
x
x/120
