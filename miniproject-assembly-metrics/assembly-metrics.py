#!/usr/bin/env python3

import sys
import fasta

my_file = open(sys.argv[1])
contigs =fasta.FASTAReader(my_file)
total_length=0
number_of_contigs=0

for ident, sequence in contigs:
    #print(ident)
    length= len(sequence)
    total_length += length
    number_of_contigs +=1

average_length= total_length/number_of_contigs
print((f"Number of contigs:{number_of_contigs},\tTotal length:{total_length},\tAverage length:{average_length}"))


# for contig in contigs:
#     print(contig)

# for line in my_file:
#     print(line)