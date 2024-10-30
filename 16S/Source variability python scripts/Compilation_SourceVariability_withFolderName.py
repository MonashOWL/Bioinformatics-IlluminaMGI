'''
Data intergration
author: Timothy Lim (credits to Zhuomin(Min) Zhou)
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
    for i, _ in enumerate(env):
        if _ == '\n':
            env.pop(i)
    env.pop(0)
    #####Get the date and ENV#######
    dateWenv_list = []
    for i in env:
        _data, _env,_ = i.split('\t')
        dateWenv_list.append(
            {
                'Sample_ID':_data,
                'env':_env
            }
        )
    #####get the files#####
    for i in dateWenv_list:
        _list = []
        for j in files:
            if i['Sample_ID'] == j[:-3]:
                _list.append(j)
        _list.sort(key= lambda a:int(a.split('_r')[-1])) 
        i['files_name'] = _list

    data_list = []
    k = 0
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
            df_std = pd.read_csv(
                os.path.join(
                    fp,
                    'mixing_proportions_stds.txt'
                ),
                delimiter = '\t'
            )
            k = k + 1
            print (k)
            df.insert(
                0,
                'Env',
                env
            )
            df.insert(
                0,
                'FolderName',
                j
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

    all1one = pd.concat(data_list)
    all1one.to_csv(
        os.path.join(
            save_path,
            'Source_variability_Compilation.csv'
        )
    )

if __name__=='__main__':
    files_path = "S:\Source_variability\SourceTracker\Exports"
    env_file_path = "S:\Source_variability\Metadata_for_compilation\ST_sinkswitch_16S_Source_modified.txt"
    save_path = "S:\Source_variability\Results"
    tread_data(files_path, env_file_path, save_path)  