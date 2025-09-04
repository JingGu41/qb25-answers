#!/bin/bash

# Day2 Unix Script Exercise 
# Exercise 1
#How many features (lines)?
(base) cmdb@QuantBio-25 unix-python-scripts % wc -l ce11_genes.bed 
#there are 53935 lines in ce11_genes.bed

#How many features per chr? e.g. chrI, chrII
(qb25) cmdb@QuantBio-25 unix-python-scripts % cut -f 1 ce11_genes.bed | uniq -c
#5460 chrI
#12 chrM
#9057 chrV
#6840 chrX
#6299 chrII
#21418 chrIV
#4849 chrIII

#How many features per strand? e.g. +, -
(base) cmdb@QuantBio-25 unix-python-scripts % cut -f 6 ce11_genes.bed | sort | uniq -c
#26626 -
#27309 +

#Exercise 3
(qb25) cmdb@QuantBio-25 unix-python-scripts % cp ~/Data/GTEx/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt ~/qb25-answers/unix-python-scripts 
#Which three SMTSDs (Tissue Site Detail) have the most samples?
(qb25) cmdb@QuantBio-25 unix-python-scripts % cut -f 6 GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt | sort | uniq -c | sort -k 1n -r
#blood, brain and skin have the most samples 

#How many lines have “RNA”?
(qb25) cmdb@QuantBio-25 unix-python-scripts % grep "RNA"  GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt | wc -l
#20017 lines contain "RNA"

#How many lines do not have “RNA”?
(qb25) cmdb@QuantBio-25 unix-python-scripts % grep -v "RNA"  GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt | wc -l 
#2935 lines don't contain "RNA"