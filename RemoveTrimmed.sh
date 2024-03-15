#!/bin/bash

for i in *001.fastq.gz
do

	newName=$(echo "$i" | cut -c8-)
	newName=${i:8}
	mv "$i" "$newName"	

done

echo "Done."
