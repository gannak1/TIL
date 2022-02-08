# Data exploration : Numerical summary statistics

# set working directory

### student math grade data ####

stud<-read.csv("stud_math.csv")
head(stud)
dim(stud)
str(stud)

# descriptive statistics :
summary(stud)
# summary() : 각 변수별 요약 통계량 제공 (기출)

# character variable to factor
stud<-read.csv("stud_math.csv", stringsAsFactors = TRUE)
# stringsAsFactors = TRUE 문자 --> 범주형 데이터 
str(stud)

attach(stud)

# descriptive statistics : compare with the above
summary(stud)

# Numerical analytics
mean(G3)
sd(G3)
sqrt(var(G3))

# 특정변수들에 대한 요약통계량 
# vars <-c("변수1","변수2", "변수3")
vars<-c("G1", "G2", "G3")
head(stud[vars])
summary(stud[vars])

# categorical data(범주형 데이터) 요약 
# table(변수이름)
table(health)

health_freq<-table(health)
names(health_freq) <- c ("very bad", "bad", "average", "good",
                      "very good")
barplot(health_freq, col=3)

# 2*2 contingency table (분할표: 범주형 변수요약)
# table(변수1, 변수2)
table(health,studytime)

chisq.test(health,studytime)

