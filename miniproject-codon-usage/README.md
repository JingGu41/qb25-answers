# My project 
- description: this script will intake the fasta file, using FASTAReader to get the sequence, then it will intake the sequence and break the string into three nucleotide codons
- by using the subset sequence file:
NP_001077862.1 {"type": "CDS", "gene": "DDTL", "product": "D-dopachrome decarboxylase-like protein", "locus": ""}
NP_001094090.1 {"type": "CDS", "gene": "TROAP", "product": "tastin isoform 2", "locus": ""}
my code successfully break it down into a list, i think the output is correct, because the length of the sequence is 405 nt, and the length of my list is 135 is which 405/3

- then my script will using the codons dictionary to translate the sequence into amino acids and recording the abundance of the amino acids in the sequence in the dictionary 
using the subset.fa, its correct because the sequence start with a ATG which translate to M, translate TGA as a *

- to analysis the difference between membrane.fa and cytoplasm.fa
(qb25) cmdb@QuantBio-25 miniproject-codon-usage % ./mini-project-codon-usage.py membrane.fa
{'M': 1010, 'A': 3364, 'E': 2953, 'S': 4272, 'R': 2511, 'G': 3143, 'L': 5044, 'Y': 1438, 'W': 595, 'C': 1031, 'F': 1961, 'V': 2921, 'I': 2365, 'K': 2207, 'P': 3053, 'T': 3468, 'H': 1224, 'Q': 1879, 'N': 1797, 'D': 2039, '*': 100}
(qb25) cmdb@QuantBio-25 miniproject-codon-usage % ./mini-project-codon-usage.py cytoplasm.fa 
{'M': 988, 'P': 2762, 'F': 1610, 'L': 4769, 'E': 3544, 'D': 2252, 'T': 2633, 'N': 1704, 'A': 3183, 'R': 2622, 'V': 2525, 'G': 2663, 'K': 2570, 'C': 954, 'S': 3808, 'I': 1907, 'Q': 2166, 'H': 1273, 'Y': 1201, '*': 100, 'W': 535}
the difference is due to the file size, i think there is just simply more reads in the membrane.fa than the cytoplasm.fa
