import pandas as pd
import numpy as np
from stride_counter_insole_force_sensor import find_stride_times
import glob
import matplotlib.pyplot as plt

# set input path
path = r"C:\Users\spyro\OneDrive\Documents\ΣΠΥΡΟΣ\Pycharm Projects\Github\Parkinson stage prediction\Walks"

# get all txts from folder named Walks
filenames = glob.glob(path + "/*01.txt")

# dictionary to append timeseries data of each individual
dictionary = {}

# iterate over all txts to add subject's id as key and the corresponding stride times as value in the dictionary
for file in filenames:
    forc_data = pd.read_csv(file,delimiter='\t',usecols=[17,18],names=['Sum of right foot forces','Sum of left foot forces'])
    sum_force_r = forc_data['Sum of right foot forces'].values.flatten()
    sum_force_l = forc_data['Sum of left foot forces'].values.flatten()
    stride_tim = find_stride_times(sum_force_r,sum_force_l,100,plot=False)[0]
    subject_id = file.split('\\')[-1].split('.')[0]
    dictionary[subject_id] = stride_tim

# save timeseries on excel
df = pd.DataFrame.from_dict(dictionary,orient="index")
df = df.transpose()
df.to_excel(r'stride_times.xlsx',sheet_name='stride_times',index=False,header=dictionary.keys())

dict = {}

# iterate over all txts to add subject's id as key and variables in another dictionary, named dict
for file in filenames:
    data = pd.read_csv(file, delimiter='\t', usecols=[17, 18], names=['Right Forces', 'Left Forces'])
    sum_forces_r = data['Right Forces'].values.flatten()
    sum_forces_l = data['Left Forces'].values.flatten()
    leg_imbal = find_stride_times(sum_forces_r, sum_forces_l, 100, plot=False)[4]
    subj_id = file.split('\\')[-1].split('.')[0]
    dict[subj_id] = leg_imbal

# save var on excel
df_new = pd.DataFrame.from_dict(dict,orient='index')
df_new.to_excel(r'Leg_imbalances.xlsx', sheet_name='leg_imbalances', index=dict.keys(), header='Leg_Imbalance')
