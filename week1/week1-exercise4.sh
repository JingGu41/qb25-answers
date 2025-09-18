#!/bin/bash
(qb25) cmdb@QuantBio-25 week1 %  bedtools intersect -c -a hg19-kc.bed -b snps-chr1.bed | sort -n -k5 | tail
#chr1	245912648	246670581	ENST00000490107.6_7	5445

#Describe the gene: What is the systematic name (e.g. ENST00000413465.6_5), human readable name (e.g. TP53), position (e.g. hg19 chr17:7,565,097-7,579,912), size (e.g. 14,816), exon count (e.g. 7)
#hg19 -chr1:245,912,649-246,670,581, size is 757,933 bp, the readable name is SMYD3, 	ENST00000490107.6_7, and there is 12 exons 

#Why do you think this gene has the most SNPs?
#long coding sequence, expressed in lots of tissues, lots of samples from various donors 

(qb25) cmdb@QuantBio-25 week1 % bedtools sort -i hg19-kc.bed > sorted_hg19.bed
(qb25) cmdb@QuantBio-25 week1 % bedtools sample -n 20 -seed 42 -i snps-chr1.bed | bedtools sort > sorted_snp.bed
(qb25) cmdb@QuantBio-25 week1 % bedtools closest -d -t first -a "sorted_snp.bed" -b "sorted_hg19.bed"
# 15 SNPs are inside the gene, closest snp from the gene is 1664, furthest snp is 22944nt from the gene