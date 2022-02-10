# EDA (Exploratory Data Analysis)

# Population vs. Sample 
# 1. Pouplation 
# - Collection of all items of interest to your study
# - N (uppercase N), parameters
# 2. Sample 
# - A subset of the poplulation 
# - n (lowercase n), statistics

# Mean, median, mode 
# Mean : the simple average

library(tidyverse)

seoul <- c(1,2,3,3,3,5,5,6,7,7,8,66)
busan <- c(1,2,3,3,4,5,5,6,7,7,9,33)

samgyubsal <- data.frame(seoul,busan)
samgyubsal

mean(samgyubsal$seoul)
mean(samgyubsal$busan)

# Median : second measure 
# the middle number in an ordered dataset

median(samgyubsal$seoul)
median(samgyubsal$busan)

summary(samgyubsal)
# See. Not affected by outliers!
# Question: Are the majority of restaurants low cost or average?

# Mode 
# the value that occurs most often

# contigency table
# shows the frequency distribution of the data

x <- table(samgyubsal$seoul)
x

names(x)[which(x==max(x))]

y <- table(samgyubsal$busan)
y

names(y)[which(y==max(y))]
# multiple modes are ok

# Skewness 
# indicates whether the observations in a dataset
# are concentrated on one side

library(tidyverse)

col.1 <- c(1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,4,4,5,5,7)
col.2 <- c(1,1,2,2,3,3,3,3,4,4,4,4,4,5,5,5,6,6,7,7)
col.3 <- c(1,2,2,3,3,4,4,4,5,5,5,5,5,6,6,6,6,6,7,7)

df <- data.frame(col.1,col.2,col.3)

summary(df)

p1.1 <-ggplot(df, aes(x = col.1))+
  geom_histogram(binwidth = 1, color="white",fill="red")+
  theme_light( )+labs(title = "Positive Skew")

p1.1

# Result:
# mean > median : positive skew (a.k.a right skew)
# The direction of the skew is counter-intuitive 
# determined by the side the tail is leaning to 

p1.2 <-ggplot(df, aes(x = col.2))+
  geom_histogram(binwidth = 1, color="white",fill="green")+
  theme_light( )+labs(title = "symmetrical")

p1.2
# Result: Symmetrical

p1.3 <-ggplot(df, aes(x = col.3))+
  geom_histogram(binwidth = 1, color="white",fill="grey")+
  theme_light( )+labs(title = "Negative Skew")

p1.3
# Result:
# mean < median : negative skew (a.k.a left skew)

# Importance of skewness
# tell us where the data is situated

