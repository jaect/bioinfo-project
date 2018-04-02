# Bioinformatics Group Project
# Authors:
# Due Date:
#

from Bio import SeqIO # to parse sequence data

handle = open("ucscoutput", "r")

# parse sequences in 'fasta' format; this returns an iterator,
# which stores a sequence of elements
sequences = SeqIO.parse(handle, "fasta")

# each sequence is stored as a SeqRecord object
# http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec:seq_features


sequenceObjList = [] # Stores all sequence objects read in from file
geneDictionary = {} # Stores all genes with 2 or more binding sites
consensusSequence = []
num = 0

# Add sequence objects from file to list
for s in sequences:
    sequenceObjList.append(s)
    num = num + 1

print("Number of sequence objects is: ", len(sequenceObjList))

for s in sequenceObjList:
    print("====================================")
    print()
    print("ID = ", s.id)  # use .id for ID/header
    print(s.seq)  # use .seq for sequence
    print("seq length = ", len(s))
    print()