# 도수 분포표

count <- c(4567,1234, 2345, 3456)
names(count) <- c("drwill","hacker","dangi","pagoda")
count

# 바 차트_bar chart

barplot(count, col="red", border = "black", main="교육서비스 수강생수",
        xlab="교육서비스제공자", ylab="수강생수")


# 상대 도수 분포표

sum <- sum(count)
count_relative <- count/sum
count_relative
barplot(count_relative, col="blue", border = "black", 
        main="교육서비스 수강생 비율",
        xlab="교육서비스제공자", ylab="수강생수")

# 파이차트(Pie Chart)
pie(count_relative, radius=1, col="yellow", border="black",
    main="교육서비스 수강생 비율 파이차트")
