import random
from Bio import (SeqIO)
from random import randint

fastafile = raw_input("Enter the input fasta filename: ")
fastqfile = raw_input("Enter the output fastq filename: ")
readLength = 50
numreads = 100000


with open(fastafile,'r') as data:
    sequence = SeqIO.read(data, "fasta")

genomicseq = str(sequence.seq)

def dummyval():
	randstr=''                                           #To generate a random string of length 50 whose ascii are between 33 and 126
	for i in range(1,readLength+1):
		randstr=randstr+chr(randint(33,126))
	return randstr
	

with open(fastqfile,'w') as out:
    for i in range(numreads):
        name = (sequence.id)
        size = len(sequence)
        start = randint(0,size - readLength)
        end = start + readLength
	my_substring=genomicseq[start:end]
	randompos=randint(0,readLength-1)
	sequenceread = my_substring.replace(my_substring[randompos],random.choice(['A','T','G','C']))
        out.write("@SEQ_ID:"+str(name)+":"+str(start+1)+":"+str(end+1)+"\n")
        out.write(str(sequenceread)+"\n")
        out.write("+\n")
        out.write(str(dummyval())+"\n")
