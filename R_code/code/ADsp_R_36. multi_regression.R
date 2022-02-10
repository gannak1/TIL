# drwill_stat_summary_r_code 

# ah yeah drwill statistics in the house 

# regression_multiple regression 

# Reg_1 다중회귀분석  

install.packages("car")
library(car)

head(Prestige)
str(Prestige)

newdata <- Prestige[,c(1:4)] 		# 회귀식 작성을 위한 데이터 준비
head(newdata)

# 산점도를 통해 변수 간 관계 확인
plot(newdata, pch=16, col="blue", 	
     main="Matrix Scatterplot")

mod1 <- lm(income ~ education + prestige + # 회귀식 도출
             women, data=newdata)
summary(mod1)
# income = 141.435 prest + -50.896 women - 253.850

# Reg_2 다중회귀분석_주요 변수 추출

library(MASS) 		# stepAIC( ) 함수 제공
Prestige[,c(1:5)]
newdata2 <- Prestige[,c(1:5)] # 모델 구축에 사용할 데이터셋 생성
head(newdata2)

mod2 <- lm(income ~ education + prestige +
             women + census, data= newdata2)
mod2
summary(mod2)

mod3 <- stepAIC(mod2) 	# 변수 선택 진행
mod3 			# 변수 선택 후 결과 확인
summary(mod3) 		# 회귀모델 상세 내용 확인

