#!/usr/bin/env python3

import sys
import fasta

my_file = open(sys.argv[1])
contigs =fasta.FASTAReader(my_file)
total_length=0
number_of_contigs=0
contigs_lengths=[]
cumulative_length=0

for ident, sequence in contigs:
    #print(ident)
    length= len(sequence)
    contigs_lengths.append(length)
    total_length += length
    number_of_contigs +=1

contigs_lengths.sort(reverse=True)
for i in range(len(contigs_lengths)):
    cumulative_length += contigs_lengths[i]
    if cumulative_length > total_length/2 :
        print (f"sequence length of the shortest contig at 50% of the total assembly length is {contigs_lengths[i]}")
        break 

average_length= total_length/number_of_contigs
print((f"Number of contigs:{number_of_contigs},\tTotal length:{total_length},\tAverage length:{average_length}"))


# for contig in contigs:
#     print(contig)

# for line in my_file:
#     print(line)