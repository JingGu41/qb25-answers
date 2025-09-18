#!/bin/bash

(qb25) cmdb@QuantBio-25 week1 %   grep 1_Active nhek.bed > nhek-active.bed
(qb25) cmdb@QuantBio-25 week1 % grep 12_Repressed nhek.bed > nhek-Repressed.bed
(qb25) cmdb@QuantBio-25 week1 %   grep 1_Active nhlf.bed > nhlf-active.bed
(qb25) cmdb@QuantBio-25 week1 % grep 12_Repressed nhlf.bed > nhlf-repressed.bed
(qb25) cmdb@QuantBio-25 week1 % wc nhek-active.bed
(qb25) cmdb@QuantBio-25 week1 % wc nhek-repress.bed 
(qb25) cmdb@QuantBio-25 week1 % wc nhlf-active.bed 
(qb25) cmdb@QuantBio-25 week1 % wc nhlf-repress.bed

(qb25) cmdb@QuantBio-25 week1 %  bedtools intersect -u -a nhek-active.bed -b nhek-repress.bed | wc 
#       0       0       0
(qb25) cmdb@QuantBio-25 week1 %  bedtools intersect -u -a nhlf-active.bed -b nhlf-repress.bed | wc 
#       0       0       0

(qb25) cmdb@QuantBio-25 week1 %  bedtools intersect -u -a nhek-active.bed -b nhlf-active.bed | wc
#  11608   92864  745322
(qb25) cmdb@QuantBio-25 week1 %  bedtools intersect -v -a nhek-active.bed -b nhlf-active.bed | wc
#  2405   19240  154383

#How many features are output by the first command? by the second command?
#first output 11608 genes, the second one 2405 genes
#Do these two numbers add up to the original number of lines in nhek-active.bed?
#yes

(qb25) cmdb@QuantBio-25 week1 %  bedtools intersect -f 1 -a nhek-active.bed -b nhlf-active.bed | head 
#chr1	25558413	25559413	1_Active_Promoter	0	.	25558413	25559413
(qb25) cmdb@QuantBio-25 week1 %  bedtools intersect -F 1 -a nhek-active.bed -b nhlf-active.bed | head
#chr1	19923013	19924213	1_Active_Promoter	0	.	19922613	19924613
(qb25) cmdb@QuantBio-25 week1 %  bedtools intersect -f 1 -F 1 -a nhek-active.bed -b nhlf-active.bed | head
#chr1	1051137	1051537	1_Active_Promoter	0	.	1051137	1051537

#How does the relationship between the NHEK and NHLF chromatin state change as you alter the overlap parameter?
# for -f command- the nhek-active chromatin state is enclosed by the nhlf-active chromatin state, the nhlf-active region is longer than nhek one, 
#the -F is the opposite which is the  nhlf-active chromatin state enclosed by the nhek-active chromatin state 
#the -f -F is when both are equal length. 

#Construct three bedtools intersect commands to identify the following types of regions. Use UCSC Genome Browser to save one PDF image for each of the three types of regions. Describe the chromatin state across all nine conditions.

#Active in NHEK, Active in NHLF
(qb25) cmdb@QuantBio-25 week1 %  bedtools intersect -u -a nhek-active.bed -b nhlf-active.bed |head
#chr1	19922613	19924613	1_Active_Promoter	0	.	19922613	19924613
# across all nine conditions, all the chromatin state are active 

#Active in NHEK, Repressed in NHLF
(qb25) cmdb@QuantBio-25 week1 %  bedtools intersect -u -a nhek-active.bed -b nhlf-repress.bed | head
#chr1	1981140	1981540	1_Active_Promoter	0	.	1981140	1981540
# when NHEK is active and NHLF is repressed, HSMM and HUVEC are repressed, GM12878, H1-hESC, HMEC  is active, K562 is insulator, HepG2 is strong enhancer

#Repressed in NHEK, Repressed in NHLF
(qb25) cmdb@QuantBio-25 week1 %  bedtools intersect -u -a nhek-repress.bed -b nhlf-repress.bed | head 
#chr1	11534013	11538613	12_Repressed	0	.	11534013	11538613
# across all nine condition, all the chromatin state are repressed 