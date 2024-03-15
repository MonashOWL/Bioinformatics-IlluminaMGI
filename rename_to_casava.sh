#!/bin/bash

# Before 20171019-64_S63_     R1_001.fastq.gz
# After  20171019-64_S63_L001_R1_001.fastq.gz

shopt -s nullglob

mkdir CASAVA_Renamed

echo "Moving completed R1 files..."

for InFileNameR1 in *L001_R1_001.fastq.gz
do
	mv $InFileNameR1 CASAVA_Renamed
done

echo "Moving completed R2 files..."

for InFileNameR2 in *L001_R2_001.fastq.gz
do
	mv $InFileNameR2 CASAVA_Renamed
done

echo "Processing R1 files..."
for InFileNameR1 in *R1_001.fastq.gz
do
	CasavaFileNameR1=$(echo "$InFileNameR1" | sed 's/R1_001.fastq.gz/L001_R1_001.fastq.gz/g')
	echo "$InFileNameR1 to $CasavaFileNameR1"
	mv $InFileNameR1 ./CASAVA_Renamed/$CasavaFileNameR1
done

echo "Processing R2 files..."
for InFileNameR2 in *R2_001.fastq.gz
do
	CasavaFileNameR2=$(echo "$InFileNameR2" | sed 's/R2_001.fastq.gz/L001_R2_001.fastq.gz/g')
	echo "$InFileNameR2 to $CasavaFileNameR2"
	mv $InFileNameR2 ./CASAVA_Renamed/$CasavaFileNameR2
done


echo "Done."
