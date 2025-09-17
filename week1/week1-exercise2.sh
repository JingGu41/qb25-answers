#!/bin/bash
(qb25) cmdb@QuantBio-25 week1 % wget https://hgdownload.soe.ucsc.edu/goldenPath/hg16/bigZips/hg16.chrom.sizes
(qb25) cmdb@QuantBio-25 week1 % grep -v _ hg16.chrom.sizes > hg16-main.chrom.sizes
(qb25) cmdb@QuantBio-25 week1 % bedtools makewindows -g hg16-main.chrom.sizes -w 1000000 > hg16-1mb.bed
(qb25) cmdb@QuantBio-25 week1 % wc hg16-1mb.bed
(qb25) cmdb@QuantBio-25 week1 % mv ~/Downloads/hg16-kc.tsv . 
(qb25) cmdb@QuantBio-25 week1 % wc hg16-kc.tsv 
(qb25) cmdb@QuantBio-25 week1 % cut -f1-3,5 hg16-kc.tsv > hg16-kc.bed
(qb25) cmdb@QuantBio-25 week1 % head hg16-kc.bed
(qb25) cmdb@QuantBio-25 week1 % bedtools intersect -c -a hg16-1mb.bed -b hg16-kc.bed > hg16-kc-count.bed
(qb25) cmdb@QuantBio-25 week1 % wc hg16-kc-count.bed 

#How many genes are in hg19?
(qb25) cmdb@QuantBio-25 week1 % wc hg19-kc.bed 
  80270  321080 3508249
#How many genes are in hg19 but not in hg16?
Use intersect with a 1-letter option to find genes with no overlaps
(qb25) cmdb@QuantBio-25 week1 % bedtools intersect -v -a hg19-kc.bed -b hg16-kc.bed | wc
   42717  170868 1864450
#Why are some genes in hg19 but not in hg16?
#because there are newer technique for assembly sequencing so we sequence genome more completely 

#Answer the same three questions but with respect to hg16
#How many genes are in hg16?
(qb25) cmdb@QuantBio-25 week1 % wc hg16-kc.bed 
   21365   85460  697180
#How many genes are in hg16 but not in hg19?
(qb25) cmdb@QuantBio-25 week1 % bedtools intersect -v -a hg16-kc.bed -b hg19-kc.bed | wc
    3460   13840  113693
#Why are some genes in hg16 but not in hg19?
# lack of information, presudo genes might also be included in the previous assembly, or screening errors create difference in alleles