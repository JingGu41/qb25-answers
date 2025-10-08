#!/usr/bin/env python3

import sys
AF_list = []
DP_list = []
for line in open(sys.argv[1]):
    if line.startswith('#'):
        continue
    fields = line.rstrip('\n').split('\t')
    info= fields[7].split(';')
    for item in info: 
        if item.startswith('AF'):
            item= item.strip('AF=')
            AF_list.append(item)

    for DP_value in fields[9:19]:   
         list = DP_value.split(':')
         DP_list.append(list[2])
            #second value from each sample
 
with open('AF.txt', 'w') as outfile:
    outfile.write("AF\n") #creates the header line
    for item in AF_list: #loops through your list
        outfile.write(f"{item}\n")

with open('DP.txt', 'w') as outfile:
    outfile.write("DP\n") #creates the header line
    for value in DP_list: #loops through your list
        outfile.write(f"{value}\n")

#Interpret this figure in two or three sentences in your own words.
#Does it look as expected? Why or why not? Bonus: what is the name of this distribution?
