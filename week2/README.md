
(qb25) cmdb@QuantBio-25 week2 % mkdir genomes
(qb25) cmdb@QuantBio-25 week2 % cd genomes
(qb25) cmdb@QuantBio-25 genomes cp ~/Data/References/sacCer3/sacCer3.fa.gz . gunzip sacCer3.fa.gz
(qb25) cmdb@QuantBio-25 genomes % bowtie2-build sacCer3.fa sacCer3
(qb25) cmdb@QuantBio-25 genomes % cd ..
(qb25) cmdb@QuantBio-25 week2 % mkdir variants
(qb25) cmdb@QuantBio-25 week2 % cd variants
(qb25) cmdb@QuantBio-25 variants % bowtie2 -p 4 -x ../genomes/sacCer3 -U ~/Data/BYxRM/fastq/A01_01.fq.gz > A01_01.sam
(qb25) cmdb@QuantBio-25 variants % samtools sort -o A01_01.bam A01_01.sam 
(qb25) cmdb@QuantBio-25 variants %  samtools index A01_01.bam
(qb25) cmdb@QuantBio-25 variants % samtools idxstats A01_01.bam > A01_01.idxstats


