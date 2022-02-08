# 추정 및 검정
install.packages("tidyverse")
library(tidyverse)
# sample() 표본 
# 1000명 중 10명 표본 추출 (단순 무작위 추출)
sample(1:1000, 10)

# 20명의 회원이 (주)한시경 사이트 접속하려고 할 때,
# 평균(m)이 42초, 표준오차(sxbar=sd/sqrt(n))라 가정 
# 1. 접속자 평균 45초 이하일 확률 
m <- 42
sxbar <- 33.57472/sqrt(20)

ggplot(data.frame(xis=c(m-4*sxbar, m+4*sxbar)),
       aes(x=xis))+stat_function(fun=dnorm, args = list(mean=m, sd=sxbar),
                                 colour="red", size=1)+
  ggtitle("정규분포 그래프")

# data.frame(xis=c(m-4*sxbar, m+4*sxbar)
# xis의 값을 m-4*sxbar ~ m+4*sxbar
# stat_function(fun=dnorm) : dnorm(정규분포: normal distribution)
# args=list(mean=m, sd=sxbar): 모수설정, 평균 m, 표준편차 sxbar로 설정

p1<- pnorm(45, mean=m, sd=sxbar, lower.tail = T)  
p1  

# 2. 접속자 평균 35초 이상, 45초 이하일 확률
p2<- pnorm(35, mean=m, sd=sxbar, lower.tail = T)  
p3<- p1-p2  
p3

# 3. 접속자 평균 45초 이상일 확률
p4<- pnorm(45, mean=m, sd=sxbar, lower.tail = F)  
p4  

# 표본비율 
# e.g. 갤럽조사. 대상자 1000명 
# 대통령 직무평가 긍정(p) 60% 부정(q=1-p) 40% 
# 평균 np (>=5), pq(>=5) 정규분포에 근사 
# p_bar = sqrt(pq/n)

p=0.6 # 표본비율 0.6
sd = sqrt(0.6*0.4/1000)
ggplot(data.frame(xis=c(p-4*sd, p+4*sd)), aes(x=xis))+
  stat_function(fun=dnorm, args=list(mean=p, sd=sd),
                colour="red", size=1)+
  ggtitle("Graph of sample poplulation")

# 구간추정

# 유의수준(alpha)에 따른 계수 구하기
# qnorm(p, mean=0, sd=1, lower.tail=F)
# 평균 0, SD 1인 정규분포에서 
# 오른쪽 꼬리 부분 확률이 p%가 되는 정규분포 값

qnorm(0.025, mean=0, sd=1, lower.tail = F)
qnorm(0.005, mean=0, sd=1, lower.tail = F)

# t분포에서 확률 구하기 
# (주)한시경 서버 접속 이용 시간 조사
# 대상자: 회원 30명, 표본평균 2분(120초), 표본표준편차(sd) 30초

# 모평균에 대한 95% 신뢰구간  
# 95% 신뢰구간: x의 평균+- 오차한계 
# x_bar +- t_0.025(n-1)*(sd/sqrt(n))
qt(0.025, 29, lower.tail = F)
# 2.04523 (t_0.025(n-1))
30/sqrt(30)
x_bar = 120 #표본평균
t_range=qt(0.025, 29, lower.tail = F)
error=30/sqrt(30)
error_range=(t_range*error)
error_range
confidence_range_0.95_min= x_bar - error_range
confidence_range_0.95_max= x_bar + error_range
confidence_range_0.95_min
confidence_range_0.95_max
# 5.477226 (sd/sqrt(n))
# 95% 신뢰구간: 120 +- 11.20218 (108.7978 ~ 131.2022)

# 가설검정 
# p 값을 이용한 가설검정
# 역병에 의해 재택교육 상황 
# 싸강위한 인터넷 서버증설 문제 가설검정 
# 표본데이터 64개 추출, 표본평균 22.5시간, 모평균편차 2시간

# 1. 가설설정 h(0) = mean <=22, h(a)= mean > 22
# 2. 유의수준 결정 alpha = 0.05 (95% 신뢰수준)
# 3. 검정통계량 z= (x_bar - mean) / (sd/sqrt(n))
# 4. p-value 값 계산
# z= (22.5-22) / (2/sqrt(64)) = 2
pnorm(2, mean=0, sd=1, lower.tail=F)
# 0.02275013 <0.005 : 귀무가설(h0) 기각, 대립가설(연구가설) 채택 
# 유의수준 0.05 이하에서 하루 인터넷 서버 접속시간 평균 22시간 이상
# 인터넷 서버 증설해야 함.
# 
