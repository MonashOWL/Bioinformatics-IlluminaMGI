#!/bin/bash

# Enable nullglob to avoid issues with empty globs
shopt -s nullglob

# Create the directory for renamed files
mkdir -p CASAVA_Renamed

echo "Moving completed R1 files..."

for InFileNameR1 in *L001_R1_001.fastq.gz
do
    mv "$InFileNameR1" CASAVA_Renamed
done

echo "Moving completed R2 files..."

for InFileNameR2 in *L001_R2_001.fastq.gz
do
    mv "$InFileNameR2" CASAVA_Renamed
done

echo "Processing R1 files..."
for InFileNameR1 in *_L1_1.fq.gz
do
    # Rename file from _L1_1.fq.gz to L001_R1_001.fastq.gz
    CasavaFileNameR1=$(echo "$InFileNameR1" | sed 's/_L1_1\.fq\.gz$/_L001_R1_001.fastq.gz/')
    echo "$InFileNameR1 to $CasavaFileNameR1"
    mv "$InFileNameR1" "./CASAVA_Renamed/$CasavaFileNameR1"
done

echo "Processing R2 files..."
for InFileNameR2 in *_L1_2.fq.gz
do
    # Rename file from _L1_2.fq.gz to L001_R2_001.fastq.gz
    CasavaFileNameR2=$(echo "$InFileNameR2" | sed 's/_L1_2\.fq\.gz$/_L001_R2_001.fastq.gz/')
    echo "$InFileNameR2 to $CasavaFileNameR2"
    mv "$InFileNameR2" "./CASAVA_Renamed/$CasavaFileNameR2"
done

echo "Done."

