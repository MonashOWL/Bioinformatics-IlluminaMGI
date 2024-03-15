#!/bin/bash

#Before using, please move this bash script to the folder which you want to initiate fastp trimming on (make sure you have backup) 
#Change directory, and then initiate this bash script using "source FAST.sh"

for f1 in *_R1_001.fastq.gz
do
        f2=${f1%%_R1_001.fastq.gz}"_R2_001.fastq.gz"
	#echo "f2 is $f2"
        fastp -i $f1 -I $f2 -o "trimmed-$f1" -O "trimmed-$f2" -A -Q -l 300 -b 300 -B 300
done

echo "Done."
