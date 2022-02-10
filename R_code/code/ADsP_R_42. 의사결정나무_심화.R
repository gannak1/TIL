# 의사결정나무(심화)

# 1. rpart 
iris
idx <- sample(1:2, nrow(iris), replace=T, prob=c(0.7,0.3))
# 변수 idx에 sample()값 지정
# sample(값 리스트, 데이터 개수, replace=T: 복원 추출)
# prob=c(0.7,0.3): 첫 번째 값 70%, 두번째 값 30%

table(idx)

train <- iris[idx ==1, ] #train dataset
# idx=1인 행만 추출

test <- iris[idx ==2, ] #test dataset
# idx=2인 행만 추출


# 의사결정나무모형 설정 : rpart(종속변수~. data = dataset)
install.packages("rpart")
library(rpart)
library(ggplot2)

tree_model <- rpart(Species~., data=train)
#train data로 모델 개발 
tree_model

#printcp()
printcp(tree_model)
plotcp(tree_model)

#분류실시 prune()함수 이용 가지치기
ptree <- prune(tree_model, cp=0.2)
# prune(): 가지치기 함수 
# cp(complexity parameter)
# 가치치기하려는 x 상대오차의 최대값, 여기서는0.2로 설정
plot(ptree)
text(ptree) #라벨 붙이기 
# 결과해석
# Sepal.Length <2.45면, setosa
# Sepal.Length >= 2.45 이고 Petal.Width<1.75 versicolor
# Sepal.Length >= 2.45 이고 Petal.Width>=1.75 virginia

#성과분석 
predtree <-predict(ptree, test, type = "class")
library(caret)
confusionMatrix(predtree,test$Species)

#party 패키지 활용 
install.packages("tree")
library(party)
tree_model2 <- ctree(Species~.,data=train)
tree_model2
plot(tree_model2)
pred_model2 <- predict(tree_model2, test)
confusionMatrix(pred_model2,test$Species)
