# correlation btw two variables 

install.packages("ggplot2")
install.packages("tidyverse")
library(tidyverse)

homes <- read.csv("land_data.csv", stringsAsFactors = F)
homes <- as.tibble(homes)
homes

homes %>% subset(Date == 2001.25) %>% 
  ggplot(aes(y=Structure.Cost,
             x=log(Land.Value)))+
  geom_point() + theme_light()+
  labs(x="Land Value(transformed)",
       y= "Structure Cost(USD)",
       title = "Relationship btw land value and structure cost")

# covaraince (positive, zero, negative)
# gives a sense of the direction 
# in which the two variables are moving

# correlation coefficient 
# adjusts the covariance value 

cor(homes$Structure.Cost, homes$Land.Value)
# correlation value
# -1<= correlation value <= 1

# perfect positive correlation 
# correlation coefficient = 1.0

# no correlation 
# correlation coefficient = 0

# perfect negative correlation 
# correlation coefficient = -1.0

cor.test(homes$Structure.Cost, homes$Land.Value)
