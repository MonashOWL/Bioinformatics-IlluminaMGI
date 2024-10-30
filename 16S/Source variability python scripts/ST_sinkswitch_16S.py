# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 19:09:27 2022

@author: Timothy
"""
#import relevant libraries
import os

#change directory for the modified metadata to be saved
files = os.listdir("S:\Source_variability\Modified_metadata")
namefile= [os.path.splitext(filename)[0] for filename in os.listdir("S:\Source_variability\Modified_metadata")]
#print (files)
#print (namefile)


#use nested for loop, first run 5 times, then switch to another metadata file for the entire range of the loop
for x in range(len(files)):
    for runs in range(1,6):    
        script = 'sourcetracker2 gibbs -i /fs03/hj18/Tim_duplicate/EPA/Phylo/core-metrics-results/feature-table.tsv -m /fs03/hj18/Tim_duplicate/EPA/Source_variability/Diversity/Modified_metadata/%s -o /fs03/hj18/Tim_duplicate/EPA/Source_variability/SourceTracker/Exports/%s_r%s --burnin 100 --source_rarefaction_depth 10000 --sink_rarefaction_depth 10000 \n' %(files[x],namefile[x],runs)
        with open("ST_sinkswitch_16S.txt",'a') as f:
                f.write (script)
        
print ('Script has been written and you need to add lines to request session and load sourcetracker')       
# After file has been written, upload the txt file to https://www.fileformat.info/convert/text/dos2unix.tr (Dos2Unix to solve \n issue)
# Then upload to winscp. From Winscp, edit to add sbatch commands.