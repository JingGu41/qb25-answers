
Exercise 2

1. What is the “size” (i.e., slope) of this relationship? Interpret the slope in plain language. Does it match your plot?
the slope is 0.37757, is a positive relationship, increase 0.377 DMNs per increase in one year of the mother age/ 
it matches my plot 

2. Is the relationship significant? How do you know? Explain the p-value in plain but precise language.
its significant, because the p-value is smaller than 0.05, there is less than a 5% chance of you getting this correlation by chance

3. Repeat the step above but for paternal age vs. paternal DNMs.
the slope is 1.35384, is a positive relationship, increase 1,35384 DMNs per increase in one year of the father age/ 
it matches my plot, from 20 to 50 years old parent, the number of DMNs increase from 30 to 90

4. Use the paternal regression model to predict the expected number of paternal DNMs for a father of age 50.5. 
y= 1.35384x + 10.32632, x is paternal age and y is number of paternal DNMs
and when x is 50.5, y will be 50.5*1.35384+10.32632= 78.695, so either 78 or 79 DMNs

5. What is the “size” of this relationship (i.e., the average difference in counts of maternal and paternal DNMs)? Interpret the difference in plain language. Does it match your plot?
-39.23485 on averagely, there is 40 more DMNs from the father, it matches my plot

6. Is the relationship significant? How do you know? Explain the p-value in plain but precise language.
yes, its significant, the p value is < 2.2e-16, there is less than 2.2e-16 chance that the different we see is due to random chance

7. Note that the paired t-test is equivalent to using the difference between the maternal and paternal DNM counts per proband as the response variable and fitting a model with only an intercept term (indicated with 1 on the right side of the model formula).Fit this model using lm() and compare to the results of the paired t-test. How would you interpret the coefficient estimate for the intercept term?
the coefficient estimate from linear model is similar to the mean difference in the t.test 

Exercise 3

TidyTuesday dataset: Pokemon 

from the pokemon dataset, I group the pokemons into 2 groups- the ones contain a single type_1, and the other group contains the second type_2, I calculated the means of the base_experience for the two group, and stitch the data back through type_1, I then plot the base experience based on type 1, some interesting pattern- dragon have the highest base experience when contain 2 type.  flying have highest base experience among the group contain 1 type.

Step 3.3 — Pose and test a linear-model hypothesis

State a hypothesis, fit a linear model, evaluate fit, and report results in README.md.
the hypothesis is having a second type will enahnce the pokemon's base experience, but when I compare the ones with a seconary type with the ones only have one type based on the primary type- there is not a significant difference the p-value is 0.53612 which means there is a 50% change the difference i see is due to random chance. 
