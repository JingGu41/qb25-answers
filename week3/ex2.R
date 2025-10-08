
library(tidyverse)

df_AF <-  read_delim(
  "~/qb25-answers/week3/AF.txt",delim=",")

plot_a <- ggplot(data = df_AF, aes(x=df_AF$AF))+
  geom_histogram(bins=11)+
  labs(x= "Allele_Frequency", y="count")
print(plot_a)

ggsave("~/qb25-answers/week3/AF.png")

#Question 2.1: Interpret this figure in two or three sentences in your own words. 
#Does it look as expected? Why or why not? Bonus: what is the name of this distribution?
# this plot is a normal distribution graph which the highest allele frequency is around 0.5 which is 
#expected, because its a heterozygote progeny from the cross of the Ork and Wine, and the allele frequency 
# is will be around 0.5

df_DP <-  read_delim(
  "~/qb25-answers/week3/DP.txt",delim=",")

plot_b <- ggplot(data = df_DP, aes(x=df_DP$DP))+
  geom_histogram(bins=21)+
  labs(x= "read depth distribution", y="count")+
  xlim(0, 20)
print(plot_b)

ggsave("~/qb25-answers/week3/DF.png")

#Question 2.2: Interpret this figure in two or three sentences in your own words. 
#What does it represent? Does it look as expected? Why or why not? Bonus: what is the name of this distribution?
# this plot is a right-skewed distribution graph, the sequence coverage is 5 on average, it does look like expected because some 
#gene gets mapped more than the other to make the skewed tails, when the majority is 5 coverage. 

