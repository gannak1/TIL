# 의사결정나무 모형

# 패키지(tree, rpart, party)

# tree패키지(binary recursive partitioning방법을 이용) 
# rpart 패키지(CART(classification and regression 방법을 이용)): 
# 두개의 패키지는 연산속도는 빠르지만, 과적합화의 위험성이 존재

# party 패키지
# Unbiased recursive partitioning 
# based on permutation test 방법을 이용) 
# 입력변수의 레벨이 31개로 제한되어 있음

# 과대적합(Over fitting) 
# training set이 정확한 결과를 보여주기 위해서 
# 복잡하게 모델을 만드는 것(Over fitting)
# 모델이 너무 간단해서 정확도가 낮은 모델(Under fitting)

# 과대 적합은 training data에서는 정확도가 높지만, 
# 새로운 데이터가 입력되면 잘못 예측할 수있다. 
# 과소 적합은 training data조차도 정확도가 떨어진다.

## 과대적합과 과소 적합의 문제점을 해결하기 위해서는 
## 더많고 더다양한 데이터를 확보하고,
## 확보한 데이터로 부터 다양한 특징을 찾아내는 것


library(rpart)
m<-rpart(Species~., data=iris)
m

plot(m, compress=T, margin=.3) 
text(m, cex=1.5)
?cex
# numeric character expansion, the final character size
# Null, NA: 1.0   
  
install.packages("rpart.plot")
library(rpart.plot)

prp(m, type=0, extra=2, digits=3)
prp(m, type=1, extra=2, digits=3)
prp(m, type=3, extra=2, digits=3)
prp(m, type=4, extra=2, digits=3)
?prp
# type: 0 (default), 1: label all nodes(not leaves)
# type: 3 Draw sepate split labels, 4: label all nodes
# extra=2 : display the classification rate

rpart.pred<-predict(m, newdata=iris, type="class")
rpart.pred
head(rpart.pred)

install.packages("caret")
library(caret)

install.packages('e1071')
confusionMatrix(rpart.pred, iris$Species)


