#!/usr/bin/env python3

import sys

my_file = open(sys.argv[1])

dictionary= {}
mismatch= {}
NM_dict= {}
perfect_match=0
for line in my_file:
    if line.startswith("@"): 
        continue
    else:
        if "NM" not in line : 
            perfect_match += 1
            line= line.strip().split("\t")
            chrom= line[2] #python start with 0
            if chrom in dictionary:
                dictionary[chrom] += 1
            else: 
                dictionary[chrom] = 1
        else:
            line= line.strip().split("\t")
            chrom= line[2] #python start with 0
            if chrom in dictionary:
                dictionary[chrom] += 1
            else: 
                dictionary[chrom] = 1
            for column in line:
                if column.startswith("NM"):
                    if column in mismatch:
                        mismatch[column] += 1 
                    else:
                        mismatch[column] = 1
                else:
                    continue 

#print(dictionary)
#print(sum(dictionary.values()))
#print(mismatch)
#print(perfect_match)
#print(sum(mismatch.values()))

for key in dictionary.keys():
    print(key, dictionary[key])

for i in mismatch.keys():
    new_key = int(i[5:])
    NM_dict[new_key]= mismatch[i]
for key in sorted(NM_dict.keys()):
    print(key, NM_dict[key])


