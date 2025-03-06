#Written by Timothy Lim 16/9/2022
#This is to generate metadata using random sampling method

#import relevant libraries
import os
import pandas as pd
import numpy as np

def source_variability(metadata_path, save_path, draw_number):
    '''
    

    Parameters
    ----------
    metadata_path : location of the metadata files (need to have different metadata files for each animal)
    save_path : Location to save modified metadata
    draw_number: Number of times you want to randomly sample the samples that are picked as sources

    Returns
    -------
    files in save_path

    '''
    #change directory for the modified metadata to be saved
    os.chdir(save_path)
    
    #obtain unique animal names, and sizes
    df = pd.read_csv(metadata_path, sep="\t")
    animal_names = df["Env"].unique() #obtain unique animal names
    size_animal = df.groupby(["Env"]).size() #obtain size of animal
    #print(size_animal)
    
    #get current animal name in loop
    for i in range(0,len(animal_names)):
        current_animal = animal_names[i] #current animal name in loop
        #print (current_animal)
        
        #get current number of animal which needs to be randomly selected
        for j in range(1,size_animal.loc[current_animal]):
           #print (j)           
           
           #randomly select samples to be changed as sinks in metadata
           for k in range(0,no_of_draws):
               df = pd.read_csv(metadata_path, sep="\t")
               no_of_sinks = size_animal.loc[current_animal] - j
               _index = df[df["Env"] == current_animal].index
               #print (_index)
               rand = np.random.choice(_index, size = no_of_sinks, replace = False)
               #print (rand)
               #print(df.loc(current_animal))
               df.iloc[[rand],2] = 'sink' #make reciprocal change, eg. if only test with one sample, the rest change to sink
               namefile = current_animal
               with open("%s_%sSources_DrawNo%s.txt" %(namefile,j,k+1), 'w') as f:
                   dfAsString = df.to_csv(index=False,sep="\t")
                   f.write(dfAsString)

                   
    print ('Metadata has been generated and saved')
               

if __name__=='__main__':
    metadata_path = "S:\Source_variability\metadata_SourceVariability.txt"
    save_path = "S:\Source_variability\Modified_metadata"
    no_of_draws = 10
    source_variability(metadata_path, save_path, no_of_draws)    
