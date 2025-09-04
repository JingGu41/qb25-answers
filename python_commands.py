#!/usr/bin/env python3
# Day2 python Script Exercise 
# Exercise 2

#Recalculate ce11_genes.bed scores using Python
#Write a script that for each feature (line) recalculates the score (column 5) such that
#new_score = original_score * feature_size
#new_score is positive or negative based on the strand (column 6)


import sys

my_file = open(sys.argv[1])

for line in my_file:
    line= line.strip('\n')
    line= line.split('\t')
    original_score = int(line[4])
    start= int(line[1])
    end= int(line[2])
    size= end-start
    new_score= original_score*size
    if line[5] != "+":
        new_score =new_score* (-1)
    
    print(line[0],"\t",start,"\t",end,"\t", line[3],new_score, "\t", line[5])