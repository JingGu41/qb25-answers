#!/usr/bin/env python3


#Question 3.1: Which samples do you think derive from the lab strain 
#and which samples do you think derive from the wine strain in this region of the genome?
# the wine strain can be 24, 27, 31,62 and 63, the 09, 11, 23, 35, 39 seem to be from the lab strain because the 
#strain 24, 27, 31,62, 63 contain same mismatch regions compare to the reference genome. 


import sys

# sample IDs (in order, corresponding to the VCF sample columns)
sample_ids = ["A01_62", "A01_39", "A01_63", "A01_35", "A01_31",
              "A01_27", "A01_24", "A01_23", "A01_11", "A01_09"] 
# open the VCF file

with open("gt_long.txt", "w") as outfile:
    outfile.write("sample_ID""\t""chrom""\t""pos""\t""genotype""\n")
    for line in open(sys.argv[1]):
        if line.startswith("#"):
            continue
        fields = line.rstrip('\n').split('\t')
        chrom = fields[0]
        pos   = fields[1]

        for i, field in enumerate(fields[9:19]):
            sample_ID= sample_ids[i]
        #print(sample_ID, field)
            list = field.split(':')
            if list[0] == "0":
                genotype = list[0]
            #print(genotype)
            elif list[0] == "1":
                genotype = list[0]
            #print(genotype)
            else:
                continue
            print(f"{sample_ID, chrom, pos, genotype}\n")
            outfile.write(f"{sample_ID}\t{chrom}\t{pos}\t{genotype}\n")

 