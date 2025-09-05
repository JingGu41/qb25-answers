# My project 
description: this script will intake the fasta file, using FASTAReader to get the sequence, then it will intake the sequence and break the string into three nucleotide codons
by using the subset sequence file:
NP_001077862.1 {"type": "CDS", "gene": "DDTL", "product": "D-dopachrome decarboxylase-like protein", "locus": ""}
NP_001094090.1 {"type": "CDS", "gene": "TROAP", "product": "tastin isoform 2", "locus": ""}
my code successfully break it down into a list, i think the output is correct, because the length of the sequence is 405 nt, and the length of my list is 135 is which 405/3