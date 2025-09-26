part 1 
(qb25) cmdb@QuantBio-25 week2 % mkdir genomes
(qb25) cmdb@QuantBio-25 week2 % cd genomes
(qb25) cmdb@QuantBio-25 genomes cp ~/Data/References/sacCer3/sacCer3.fa.gz . gunzip sacCer3.fa.gz
(qb25) cmdb@QuantBio-25 genomes % bowtie2-build sacCer3.fa sacCer3
(qb25) cmdb@QuantBio-25 genomes % cd ..
(qb25) cmdb@QuantBio-25 week2 % mkdir variants
(qb25) cmdb@QuantBio-25 week2 % cd variants
(qb25) cmdb@QuantBio-25 variants % bowtie2 -p 4 -x ../genomes/sacCer3 -U ~/Data/BYxRM/fastq/A01_01.fq.gz > A01_01.sam
(qb25) cmdb@QuantBio-25 variants % samtools sort -o A01_01.bam A01_01.sam 
(qb25) cmdb@QuantBio-25 variants % samtools index A01_01.bam
(qb25) cmdb@QuantBio-25 variants % samtools idxstats A01_01.bam > A01_01.idxstats

part 2
how this visualization compares to haplotypes in BYxRM_GenoData.txt
forthe snps from CHr01_ 27000-32000, there are majority strain specific SNP variations but the cross does transfer some SNP variation across species 

part 4
(qb25) cmdb@QuantBio-25 longreads % minimap2 -ax map-ont ~/qb25-answers/week2/genomes/sacCer3.fa ~/qb25-answers/week2/rawdata/ERR8562476.fastq > longreads.sam
(qb25) cmdb@QuantBio-25 longreads %  samtools sort -o longreads.bam longreads.sam 
(qb25) cmdb@QuantBio-25 longreads % samtools index longreads.bam
(qb25) cmdb@QuantBio-25 longreads % samtools idxstats longreads.bam > longreads.idxstats

part 5 
(qb25) cmdb@QuantBio-25 rawdata % fasterq-dump -p  SRR10143769
(qb25) cmdb@QuantBio-25 genomes % hisat2-build sacCer3.fa sacCer3
(qb25) cmdb@QuantBio-25 rawdata % wc SRR10143769.fastq 
(qb25) cmdb@QuantBio-25 rna % hisat2 -p 4 -x ../genomes/sacCer3 -U ~/qb25-answers/week2/rawdata/SRR10143769.fastq > rna.sam 
(qb25) cmdb@QuantBio-25 rna %  samtools sort -o rna.bam rna.sam
(qb25) cmdb@QuantBio-25 rna %  samtools index rna.bam
(qb25) cmdb@QuantBio-25 rna %  samtools idxstats rna.bam > rna.idxstats

what part of the genes appear to have the most coverage
the termination site of the gene, when its close to the stop codon its likely to have high gene coverage 