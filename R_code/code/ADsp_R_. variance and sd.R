# Variance vs. Standard deviation 
# sd : by calculating the square root of the variance
# Coefficient of variation : relative standard deviation 

seoul <- c(1,2,3,3,5,6,7,8,9,10)
la <- c(1,2,3,4,5,6,7,8,9,10)

pizza <- data.frame(seoul, la)
pizza$seoul.mxn <- c(18.81, 37.62, 56.40, 56.34,95.0,
                     123.4,131.3, 150.3, 167.4, 200.1)

pizza

# sapply() 
# great for running opearations repetedly, 
# from element to element in the form of data frame

# lapply()
# applies the function you pass to every element in a list

lapply(pizza, mean)

sapply(pizza, mean)
sapply(pizza, var)
sapply(pizza, sd)
coef.var <- sapply(pizza,sd)/sapply(pizza,mean)
coef.var
