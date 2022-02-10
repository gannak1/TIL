# regression_simple regression 

# Reg_1 단순선형회귀_산점도 

head(cars)4
plot(dist~speed, data=cars) 		# 산점도를 통해 선형 관계 확인

model <- lm(dist~speed, cars) 	# 회귀모델 구하기
model

abline(model) 			# 회귀선을 산점도 위에 표시
coef(model)[1] 			# b 값 출력
coef(model)[2] 			# W 값 출력

# Reg_2 단순선형회귀_주행속도에 따른 제동거리 구하기

b <- coef(model)[1]
W <- coef(model)[2]

speed <- 30 			# 주행속도
dist <- W*speed + b
dist 				# 제동거리

speed <- 35 			# 주행속도
dist <- W*speed + b
dist 				# 제동거리

speed <- 40 			# 주행속도
dist <- W*speed + b
dist 				# 제동거리

# Reg_3 단순선형회귀_예상 제동거리, 실제 제동거리, 오차 구하기

head(cars)
cars[,1] # speed 의 원소 
speed <- cars[,1] 			# 주행속도
pred <- W * speed + b
pred 				# 예상 제동거리

data.frame(pred, cars[,2], pred-cars[,2])
compare <- data.frame(pred, cars[,2], pred-cars[,2])
colnames(compare) <- c('예상','실제','오차')
head(compare)




