# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 19:09:27 2022

@author: Timothy
"""
#import relevant libraries
import os

#change directory for the modified metadata to be saved
files = os.listdir("G:\My Drive\Monash postgraduate\SourceTracker and Qiime2\QIIME ST runs\\29072022\Combined data with septics and third campaign sources and first campaign sinks and WWTP_Rarefied-2k\One at a time\Modified_metadata")
namefile= [os.path.splitext(filename)[0] for filename in os.listdir("G:\My Drive\Monash postgraduate\SourceTracker and Qiime2\QIIME ST runs\\29072022\Combined data with septics and third campaign sources and first campaign sinks and WWTP_Rarefied-2k\One at a time\Modified_metadata")]
#print (files)
#print (namefile)


#use nested for loop, first run 5 times, then switch to another metadata file for the entire range of the loop
for x in range(len(files)):
    for runs in range(1,6):    
        script = 'sourcetracker2 gibbs -i /fs04/hj18/Timothy/Tarago_24022022_Wastewater/Merged_with_24022022_Combined/Phylo/Without_excluding_septics/core-metrics-results/feature-table.tsv -m /fs04/hj18/Timothy/Tarago_24022022_Wastewater/Merged_with_24022022_Combined/OneAtATime/Diversity/%s -o /fs04/hj18/Timothy/Tarago_24022022_Wastewater/Merged_with_24022022_Combined/OneAtATime/SourceTracker/Exports/%s_r%s --burnin 100 --source_rarefaction_depth 2000 --sink_rarefaction_depth 2000 \n' %(files[x],namefile[x],runs)
        with open("ST_sinkswitch_16S.txt",'a') as f:
                f.write (script)
        
print ('Script has been written and you need to add lines to request session and load sourcetracker')       
# After file has been written, upload the txt file to https://www.fileformat.info/convert/text/dos2unix.tr (Dos2Unix to solve \n issue)
# Then upload to winscp. From Winscp, edit to add sbatch commands.
