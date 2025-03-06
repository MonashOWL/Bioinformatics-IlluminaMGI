'''
One At A Time Compilation
Created by: Zhuomin Zhou
Modified by: Timothy Lim
date: 05/09/2022

'''

import os
import pandas as pd

def tread_data(files_path, env_file_path, save_path):
    '''
    This function is used to intergate the txt files into one csv file.
    The data structure need to follow **SourceTracker**
    '''
    files = os.listdir(files_path)
    #####Get ########
    with open(env_file_path,'r') as f:
        env = f.readlines()
    for i, _ in enumerate(env): #since env_file.txt has one row with data, the following row without anything. Point of this is to remove those rows. Enumerate will go through entire list in the file
        if _ == '\n':
            env.pop(i)
    env.pop(0) #env contains data from metadata file
    
    #####Get the sampleID and ENV#######
    dateWenv_list = []
    for i in env:
        _data, _env,_ = i.split('\t') #_data is SampleID, _env is animal type, _ is sourceSinks
        dateWenv_list.append(
            {
                'Sample_ID':_data,
                'env':_env
            }
        )
        
    #####get the files#####
    for i in dateWenv_list: #loop through each row in metadata list
        _list = []
        for j in files: #loop through each file in the exports folder
            if i['Sample_ID'] == j[:-3]: #if the sample id is equivalent to the file names in export folder without '_r1' or '_r2' etc.
                _list.append(j) #then append; _list only contain one sample with different run numbers, e.g. Bat-poo-3_r1, Bat-poo-3_r2
        _list.sort(key= lambda a:int(a.split('_r')[-1])) #to sort according to the final digit. split('_r') of "Bat-poo-3_r1" outputs two things ['Bat-poo-3','1']. split('_r')[-1] will result in '1'
        i['files_name'] = _list
        

    data_list = []
    k=1
    for i in dateWenv_list:
        env = i['env']
        for j in i['files_name']:
            fp = os.path.join(
                files_path,
                j
            )
            df = pd.read_csv(
                os.path.join(
                    fp,
                    'mixing_proportions.txt'
                ),
                delimiter = '\t'
            )
            k = k+1
            print (k)
            
            df_std = pd.read_csv(
                os.path.join(
                    fp,
                    'mixing_proportions_stds.txt'
                ),
                delimiter = '\t'
            )
            df.insert(
                0,
                'Env',
                env
            )
            df.insert(
                0,
                'run',
                j.split('_r')[-1]
            )
            

            df_std = df_std.drop(columns=['SampleID'])
            #get colums index
            
            for i in df_std.columns.values:
                df_std = df_std.rename(columns={i:i+'_std'})

            data_list.append(
                pd.concat([df,df_std], axis=1)
            )
    
    oneAtATime = pd.concat(data_list)
    oneAtATime.to_csv(
        os.path.join(
            
            save_path,
            'oneAtATime_compilation.csv'
        )
    )

if __name__=='__main__':
    files_path = "C:\\Users\Timothy\Desktop\Exports"
    env_file_path = "G:\My Drive\Monash postgraduate\SourceTracker and Qiime2\QIIME ST runs\\29072022\Combined data with septics and third campaign sources and first campaign sinks and WWTP_Rarefied-2k\One at a time\Metadata_default_MergedWithWWTP.txt"
    save_path = "G:\My Drive\Monash postgraduate\SourceTracker and Qiime2\QIIME ST runs\\29072022\Combined data with septics and third campaign sources and first campaign sinks and WWTP_Rarefied-2k\One at a time\Results"
    tread_data(files_path, env_file_path, save_path)    
