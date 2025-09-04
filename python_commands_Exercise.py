#!/usr/bin/env python3

# Day2 python Script Exercise 
# Exercise 4 Transform GTEx data using Python

#Write a script that extracts expression values for the first gene (DDX11L1) which is stored on a single line spread across more than 17,000 columns and transposes the data so that the expression in each sample is stored on a separate line.
#Open the expression data file GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_tpm.gct

#Skip the first two lines using .readline()
#Read the next header line and save the fields after splitting
#Read the next data line and save the fields after splitting
#Create a dictionary by looping through the fields, using header[i] as the key to store data[i] as the value
#Open the metadata file GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
#If the SAMPID in the first column is present in the dictionary, print out the SAMPID, expression, and SMTSD e.g.

import sys

my_file = open(sys.argv[1])
_ = my_file.readline()
_ = my_file.readline()
header = my_file.readline().rstrip().split("\t")
data_file= my_file.readline().rstrip().split("\t")
dictionary={}

for i in range(len(header)):
    place= header[i]
    dictionary[place]=data_file[i]

#print(dictionary)

metadata_Attribution= ("/Users/cmdb/Data/GTEx/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt")
for line in open(metadata_Attribution):
    line= line.rstrip("\n")
    line=line.split("\t")
    if line[0] in dictionary:
        SAMPID= line[0]
        TISSUE= line[6]
        EXPRESSION= dictionary[SAMPID]
        print(SAMPID)
        print(f"SAMPID:{SAMPID},'\t'EXPRESSION:{EXPRESSION},'\t'TISSUE:{TISSUE}'\n\'")
    else:
        continue
        

    
my_file.close()

