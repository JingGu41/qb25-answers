 #!/bin/bash

 for sample in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63
 do
 # to use variable, prefix it with a $
    echo "***" $sample  
    ls -l ~/qb25-answers/week3/BYxRM_bam/$sample.bam
    samtools index /Users/cmdb/qb25-answers/week3/BYxRM_bam/$sample.bam
    samtools view -c /Users/cmdb/qb25-answers/week3/BYxRM_bam/$sample.bam >> read_counts.txt
    echo $sample.bam >> bamListFile.txt
done 

(qb25) cmdb@QuantBio-25 week3 % cp ~/Data/References/sacCer3/sacCer3.fa.gz 
(qb25) cmdb@QuantBio-25 week3 % gunzip sacCer3.fa.gz
(qb25) cmdb@QuantBio-25 BYxRM_bam % freebayes -f sacCer3.fa -L /Users/cmdb/qb25-answers/week3/BYxRM_bam/bamListFile.txt --genotype-qualities -p 1 > unfiltered.vcf
(qb25) cmdb@QuantBio-25 BYxRM_bam % vcffilter -f "QUAL > 20" -f "AN > 9" unfiltered.vcf > filtered.vcf

# Question 1.1: How many aligned reads does each BAM file contain?
#A01_09 669548
#A01_11 656245
#A01_23 708732
#A01_24 797385
#A01_27 602404
#A01_31 610360
#A01_35 803554
#A01_39 713726
#A01_62 816639
#A01_63 620829