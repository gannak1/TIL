# set working directory

### student math grade data ####

stud<-read.csv("stud_math.csv", stringsAsFactors = TRUE)

head(stud)
dim(stud)
str(stud)

attach(stud)
dev.off()
# 1. histogram with color and title, legend
# 히스토그램(1학년, 2학년, 3학년 성적 분포)
hist(G1, breaks = 10, col = "lightblue", main="Histogram of Grade 1" )
hist(G2, breaks = 10, col = "green", main="Histogram of Grade 2" )
hist(G3, breaks = 10, col = "coral", main="Histogram of Grade 3" )

# 2. boxplot(거주지역에 따른 G3, 통학시간에 따른 G3)
par(mfrow=c(1,2))
boxplot(G3~address, boxwex = 0.5, col = c("yellow", "coral"), main="G3 by (Urban, Rural)")
boxplot(G3~traveltime, boxwex = 0.5, col = c("red","orange","yellow","green"), main="G3 by traveltime")
# 결과해석
# - 도심지역 학생들 성적이 외곽지역 학생들보다 높다 
# - 통학시간이 짧은 15분 이내 학생들의 성적이 더 높다
  
# boxplot
par(mfrow=c(1,2))
# academic achievement by freetime
# 자유시간에 따른 G3, 공부시간에 따른 G3
# 1 - very low to 5 - very high
boxplot(G3~freetime, boxwex = 0.5, col = c("yellow", "green", "blue","grey","red"),main="G3 by freetime")
# academic achievement by studytime  
# 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours 
boxplot(G3~studytime, boxwex = 0.5, col = c("yellow", "blue","grey","red"), main="G3 by studytime")

# 결과해석 
# - 주중 공부시간이 5시간 이상(3: 5-10시간, 4: 10시간 이상)
#   학생의 성적이 높은 편임

# 3. xyplot : lattice package 
# 통학시간과 최종성적(G3) 멀티패널 그림(성별)
library(lattice)
xyplot(G3 ~ traveltime | sex , data = stud, pch=16, main = "G3 ~ traveltime | sex ")

# 결과해석
# - 학생 대다수가 30분 이내 통학거리에 있음
# - 통학거리가 짧은 학생들의 성적 평균이 다소 높게 나옴
# - 통학거리가 1시간 이상은 표본이 상대적으로 적음

# 0점인 데이터 확인 필요
# data (G3=0)
s1<-subset(stud, G3==0)
s1

# 4. 산점도 scatterplot : ggplot2 package
library(ggplot2)
# scatterplot for G1 and G3 by sex
ggplot(stud, aes(x=G1, y=G3, color=sex, shape=sex)) + 
  geom_point(size=2)

# 성별에 따른 차이가 없음 

# 5. bar chart : ggplot2 package
# bar chart for romantic by sex
ggplot(data=stud, aes(factor(romantic)))+geom_bar(aes(fill=factor(sex)), width=.4, colour="black")+ ggtitle("Romantic by sex")
# 연예경험 있는 경우, 여학생 비율이 높음

# bar chart for internet use by (Urban, Rural)
ggplot(data=stud, aes(factor(internet)))+geom_bar(aes(fill=factor(address)), width=.4, colour="black")+ggtitle("Internet use by (Urban, Rural)")
# 인터넷 사용자 중, 도심지역 사는 경우 훨씬 높음

# 6. pariwise plot (기출)
# new variable lists
vars1<-c("G1", "G2", "G3")
# pariwise plot
pairs(stud[vars1], main = "Student Math Data",pch = 21, bg = c ("red","green3"))

# 결과해석
# - G1,G2,G3 상관성은 매우 높음 
# - 성별 간 차이가 없음

