#!/usr/bin/env python3

#====================#
# Read in parameters #
#====================#
import sys
import numpy as np
from fasta import readFASTA

input_sequences = readFASTA(open(sys.argv[1]))
seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]
sigma_file = sys.argv[2]

# The scoring matrix is assumed to be named "sigma_file" and the 
# output filename is assumed to be named "out_file" in later code

# Read the scoring matrix into a dictionary
fs = open(sigma_file)
sigma = {}
alphabet = fs.readline().strip().split()
for line in fs:
	line = line.rstrip().split()
	for i in range(1, len(line)):
		sigma[(alphabet[i - 1], line[0])] = float(line[i])
fs.close()

# Read in the actual sequences using readFASTA

#=====================#
# Initialize F matrix #
#=====================#
f_matrix = np.zeros((len(sequence1) + 1, len(sequence2) + 1), dtype= int)
print(f_matrix)

#=============================#
# Initialize Traceback Matrix #
#=============================#
Traceback_matrix = np.empty((len(sequence1) + 1, len(sequence2) + 1), dtype= str)
print(Traceback_matrix)

#===================#
# Populate Matrices #
#===================#
gap_penalty = int(sys.argv[3])
for j in range(1, len(sequence2)+1):
	f_matrix[0,j]= f_matrix[0, j-1]+ gap_penalty
	Traceback_matrix[0,j]= "h"
for i in range(1, len(sequence1)+1 ):
	f_matrix[i,0]= f_matrix[i-1,0]+ gap_penalty
	Traceback_matrix[i,0]= "v"

print(Traceback_matrix)

for i in range(1, len(sequence1)+1):
	for j in range(1, len(sequence2)+1):
		h_score = gap_penalty+ f_matrix[i, j-1]
		v_score = gap_penalty+ f_matrix[i-1, j]
		if sequence1[i-1]==sequence2[j-1]:
			match_score= sigma[(sequence1[i-1],sequence2[j-1])]
			d_score = match_score+ f_matrix[i-1, j-1]
		else:
			mismatch_score= sigma[(sequence1[i-1],sequence2[j-1])]
			d_score = mismatch_score+ f_matrix[i-1, j-1]
		
		highest_score = max(v_score, h_score, d_score)
		f_matrix[i,j] = highest_score
		if d_score == highest_score:
			Traceback_matrix[i,j]= "d"
		elif h_score == highest_score:
			Traceback_matrix[i,j]= "h"
		else: 
			Traceback_matrix[i,j]= "v"
print(f_matrix)
print(Traceback_matrix)

#========================================#
# Follow traceback to generate alignment #
#========================================#

# The aligned sequences are assumed to be strings named sequence1_aligment
# and sequence2_alignment in later code
i = len(sequence1)
j = len(sequence2)
alignment_1 = ""
alignment_2 = ""

while i != 0 or j != 0:
	#print(i,j)
	
	if Traceback_matrix[i,j] == "v":
		alignment_1= alignment_1+sequence1[i-1]
		alignment_2= alignment_2+"-"
		i= i-1
		continue

	if Traceback_matrix[i,j] == "h":
		alignment_1= alignment_1+"-"
		alignment_2= alignment_2+sequence2[j-1]
		j= j-1
		continue

	if Traceback_matrix[i,j] == "d": 
		alignment_1= alignment_1+sequence1[i-1]
		alignment_2= alignment_2+sequence2[j-1]
		i=i-1
		j=j-1
		continue

print(alignment_1)
print(alignment_2)

#=================================#
# Generate the identity alignment #
#=================================#

# This is just the bit between the two aligned sequences that
# denotes whether the two sequences have perfect identity
# at each position (a | symbol) or not.

identity_alignment = ''
for i in range(len(alignment_1)):
	if alignment_1[i] == alignment_2[i]:
		identity_alignment += '|'
	else:
		identity_alignment += ' '


#===========================#
# Write alignment to output #
#===========================#

# Certainly not necessary, but this writes 100 positions at
# a time to the output, rather than all of it at once.

output = open(sys.argv[4], 'w')

for i in range(0, len(identity_alignment), 100):
	output.write(alignment_1[i:i+100] + '\n')
	output.write(identity_alignment[i:i+100] + '\n')
	output.write(alignment_2[i:i+100] + '\n\n\n')

#=============================#
# Calculate sequence identity #
#=============================#

alignment_1_identity = identity_alignment.count("|")/len(sequence1) *100
alignment_2_identity = identity_alignment.count("|")/len(sequence2) *100
#======================#
# Print alignment info #
#======================#
print(alignment_1.count("-"))
print(alignment_2.count("-"))
print(alignment_1_identity)
print(alignment_2_identity)
print(f_matrix[len(sequence1), len(sequence2)])

# You need the number of gaps in each sequence, the sequence identity in
# each sequence, and the total alignment score
