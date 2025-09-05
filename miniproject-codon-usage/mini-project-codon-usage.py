#!/usr/bin/env python3

import sys
import fasta
import codons

my_file = open(sys.argv[1])
contigs =fasta.FASTAReader(my_file)
aas={}

for ident, sequence in contigs:
    #codon_list=[]
    #print(ident)
    #print(sequence)
    #print(len(sequence))
    counter=list(range(0,len(sequence)+1,3))
    #print(counter)
    for i in range(len(sequence)):
        #print(i)
        if i in counter:
            codon= sequence[i:i+3]
            aa = (codons.forward).get(codon)
            #print(codon)
            #print(aa)
            #codon_list.append(codon)
            if aa not in aas:
                aas[aa]=1
            else:
                aas[aa] += 1 
        else:
            continue 
    #print(len(codon_list))

print(aas)