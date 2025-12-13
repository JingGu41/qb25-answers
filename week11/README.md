Step1.1
How many 100bp reads are needed to sequence a 1Mbp genome to 3x coverage?
num_reads = genome_size * coverage / readlength
1000000*3/100 = 30000 reads are needed

Step1.4
In your simulation, how much of the genome has not been sequenced (has 0x coverage)?
50000/1000000 is about 5% of the genome 
How well does this match Poisson expectations? How well does the normal distribution fit the data?
its a bit skewed to left when compare to normal distribution, and poisson expectation fits the distribution better 

step1.5
In your simulation, how much of the genome has not been sequenced (has 0x coverage)?
43/1000000 almost to 0% of the genome 
How well does this match Poisson expectations? How well does the normal distribution fit the data?
poisson and normal distribution both predict this result well 

step1.6 
In your simulation, how much of the genome has not been sequenced (has 0x coverage)?
all are sequenced 
How well does this match Poisson expectations? How well does the normal distribution fit the data?
both matches prefectly 

step2.4 command line 
(graphviz) cmdb@QuantBio-25 week11 % dot -Tpng debruijn_graph.dot -o ex2_digraph.png

step2.5
 one possible genome sequence that would produce these reads is 
CAT → ATT → TTG → TGA → GAT → ATT → TTC → TCT → CTT → TTA → TAT → ATT → TTT

step2.6 
 what would it take to accurately reconstruct the sequence of the genome? 
 Accurate genome reconstruction would require sufficient read definitely greater than 3x coverage to ensure that all k-mers and their correct multiplicities are represented in the de Bruijn graph. The graph must contain a unique  path but the repeats can be confusing therefore it need to have a larger k, additional coverage information, or paired-end reads to distinguish between alternative paths.