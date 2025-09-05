#!/usr/bin/env python3

import sys
import fasta

my_file = open(sys.argv[1])
contigs =fasta.FASTAReader(my_file)

for ident, sequence in contigs:
    codon_list=[]
    #print(ident)
    #print(sequence)
    #print(len(sequence))
    counter=list(range(0,len(sequence)+1,3))
    #print(counter)
    for i in range(len(sequence)):
        #print(i)
        if i in counter:
            codon= sequence[i:i+3]
            #print(codon)
            codon_list.append(codon)
        else:
            continue 
    #print(len(codon_list))