import  re
from Bio import (SeqIO) #Import statement for Biopython

total=-1 # total number of reads
unaligned=-1 #unaligned number of reads
sam =raw_input("Enter the sam filename :") #asking user to input the sam filename present in the same directory
i = open(sam,'r') #opening the file in read mode

for line in i : #reading each line
	arr = re.findall(r'\w+',line)  #to find out  
	if(len(arr) > 6):
		if arr[2] != arr[6] :
		        unaligned =unaligned+1 
		total=total+ 1
rate=(unaligned/total)*100
print("Total unaligned reads: "+str(unaligned)+"\n")
print("Total reads: "+str(total)+"\n")
print(" Error-rate: "+str(rate)+"\n")

