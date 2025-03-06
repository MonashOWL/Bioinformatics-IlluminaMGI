#Written by Timothy Lim 30/8/2022

#import relevant libraries
import os
import pandas as pd
#change directory for the modified metadata to be saved
os.chdir("G:\My Drive\Monash postgraduate\SourceTracker and Qiime2\QIIME ST runs\\29072022\Combined data with septics and third campaign sources and first campaign sinks and WWTP_Rarefied-2k\One at a time\Modified_metadata")
#read original metadata file
original_metadata = pd.read_csv("G:\My Drive\Monash postgraduate\SourceTracker and Qiime2\QIIME ST runs\\29072022\Combined data with septics and third campaign sources and first campaign sinks and WWTP_Rarefied-2k\One at a time\Metadata_default_MergedWithWWTP.txt",sep="\t") 

#replace each row's source to sink and save it as new file
for x in range(len(original_metadata)):
    metadata = pd.read_csv("G:\My Drive\Monash postgraduate\SourceTracker and Qiime2\QIIME ST runs\\29072022\Combined data with septics and third campaign sources and first campaign sinks and WWTP_Rarefied-2k\One at a time\Metadata_default_MergedWithWWTP.txt",sep="\t") 
    metadata.iloc[x,2] = 'sink' #change every subsequent row to sink at each iteration (which is column 3)
    namefile = metadata.iloc[x,0]  #set name of file (saved at column 0)
    with open("%s.txt" %namefile, 'w') as f:
        dfAsString = metadata.to_csv(index=False,sep="\t")
        f.write(dfAsString)

print ('Metadata has been modified and saved')



