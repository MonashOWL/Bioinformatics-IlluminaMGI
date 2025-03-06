# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 2022

@author: Timothy
"""
#import relevant libraries
import os

#change directory for the modified metadata to be saved
files = os.listdir("S:\OneWater\EPA\Site specific objectives framework 2023\Task work\Task 5\Source_variability\Modified_metadata")
namefile= [os.path.splitext(filename)[0] for filename in os.listdir("S:\OneWater\EPA\Site specific objectives framework 2023\Task work\Task 5\Source_variability\Modified_metadata")]
#print (files)
#print (namefile)

#set directory to save job file
os.chdir("S:\Source_variability\Metadata_for_compilation")
         
#use nested for loop, first run 5 times, then switch to another metadata file for the entire range of the loop
for x in range(len(files)):
    for runs in range(1,2):    
        script = '%s\n' %(namefile[x])
        with open("ST_sinkswitch_16S_Source.txt",'a') as f:
                f.write (script)
        
print ('Script has been written and you need to add lines to request session and load sourcetracker')       
# After file has been written, upload the txt file to https://www.fileformat.info/convert/text/dos2unix.tr (Dos2Unix to solve \n issue)
# Then upload to winscp. From Winscp, edit to add sbatch commands.
