# 박스 플롯(box plot)과 상관계수(상관관계) 

# 데이터 입력
grade <- c("A","A","B","B","C","C","D","D","E","E","A","A","B","B","C")
height <- c(154,163,157,145,149,164,165,171,178,169,172,175,181,188,165)
weight<-c(51,57,58,52,49,58,60,63,67,61,81,78,83,88,73)
score<-c(71,69,80,81,72,87,83,79,78,83,62,69,72,75,73)

grade <- as.factor(grade)
grade

class_data <- data.frame(grade,height,weight,score)
class_data

head(class_data)
str(class_data)

# 나무상자(boxplot)
boxplot(class_data)

plot(class_data)

# 상관계수 
cor(class_data$height, class_data$weight, method="pearson")
cor(class_data$height, class_data$score, method="pearson")
