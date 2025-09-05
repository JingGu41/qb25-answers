#!/usr/bin/env python3

import sys
import fasta
import codons

my_file1 = open(sys.argv[1])
my_file2 = open(sys.argv[2])
contigs1 = fasta.FASTAReader(my_file1)
contigs2 = fasta.FASTAReader(my_file2)
aas1={}
aas2={}

for ident, sequence in contigs1:
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
            if aa not in aas1:
                aas1[aa]=1
            else:
                aas1[aa] += 1 
        else:
            continue 
    #print(len(codon_list))

for ident, sequence in contigs2:
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
            if aa not in aas2:
                aas2[aa]=1
            else:
                aas2[aa] += 1 
        else:
            continue 
    #print(len(codon_list))

print(sys.argv[1])
print(aas1)
print(sys.argv[2])
print(aas2)

reverse= codons.reverse.keys()
my_list =list(reverse)
sort = sorted(my_list)

for i in sort:
    abundance_1 = aas1.get(i)
    abundance_2 = aas2.get(i)
    report = (f"{i}\t{abundance_1}\t{abundance_2}")
    print(report)


