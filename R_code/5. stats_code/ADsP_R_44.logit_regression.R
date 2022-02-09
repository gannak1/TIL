# drwill_stat_summary_r_code 

# ah yeah drwill statistics in the house 

# logit_regression 

# Reg_1 로지스틱 회귀모델

head(iris)
iris.new <- iris
iris.new$Species <- as.integer(iris.new$Species) # 범주형 자료를 정수로 변환
head(iris.new)
mod.iris <- glm(Species ~., data= iris.new) 	# 로지스틱 회귀모델 도출
summary(mod.iris) 			# 회귀모델의 상세 내용 확인

# Reg_2 로지스틱 회귀모델 예측

# 예측 대상 데이터 생성(데이터프레임)
unknown <- data.frame(rbind(c(5.1, 3.5, 1.4, 0.2)))
names(unknown) <- names(iris)[1:4]
unknown 				# 예측 대상 데이터

pred <- predict(mod.iris, unknown) 		# 품종 예측, mod.iris 로지스틱회귀모델 
pred 					# 예측 결과 출력
round(pred,0) 		# 예측 결과 출력(소수 첫째 자리에서 반올림)

# 실제 품종명 알아보기
pred <- round(pred,0)
pred
levels(iris$Species)
levels(iris$Species)[pred] 

# Reg_3 로지스틱 회귀모델 예측_다수의 데이터 

test <- iris[,1:4] 			# 예측 대상 데이터 준비
head(test)
pred <- predict(mod.iris, test) 	# 모델을 이용한 예측
pred <- round(pred,0)
pred 				# 예측 결과 출력
answer <- as.integer(iris$Species) 	# 실제 품종 정보
pred == answer 		# 예측 품종과 실제 품종이 같은지 비교
acc <- mean(pred == answer) 	# 예측 정확도 계산
acc 

