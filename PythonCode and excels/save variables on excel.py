import pandas as pd
import numpy as np
from Sample_Entropy import Sample_Entropy
from DFA import DFA
from datetime import datetime

# set input path and import data
path = r'stride_times.xlsx'
df = pd.read_excel(path)

dictionary = {}

# iterate over columns of dataframe
for column,data in df.iteritems():

    subject_id = column
    stride_times = data.values[np.logical_not(np.isnan(data.values))]
    variables = []

    currTime = datetime.now()

    # calculate variables of interest (dfa input size was set to 74 stride times because this was the minimum
    # number of stride times found in the dataset)
    mean_stride_times = np.mean(stride_times)
    cv_stride_times = (np.mean(stride_times)/np.std(stride_times))*100
    no_strides = len(stride_times)+1
    global dfa_4_8
    global dfa_4_10
    global dfa_4_12
    global dfa_4_12
    global sampen_2_020
    global sampen_2_025
    global sampen_2_030
    global sampen_3_025
    global sampen_3_030

    if len(stride_times) >= 74:
        dfa_4_8 = DFA(stride_times[:74],4,8)[0][0]
        dfa_4_10 = DFA(stride_times[:74],4,10)[0][0]
        dfa_4_12 = DFA(stride_times[:74],4,12)[0][0]
        dfa_4_14 = DFA(stride_times[:74],4,14)[0][0]
        sampen_2_020 = Sample_Entropy(stride_times[:74], 2, 0.20 * np.std(stride_times[:74]))
        sampen_2_025 = Sample_Entropy(stride_times[:74], 2, 0.25 * np.std(stride_times[:74]))
        sampen_2_030 = Sample_Entropy(stride_times[:74], 2, 0.30 * np.std(stride_times[:74]))
        sampen_3_025 = Sample_Entropy(stride_times[:74], 3, 0.25 * np.std(stride_times[:74]))
        sampen_3_030 = Sample_Entropy(stride_times[:74], 3, 0.30 * np.std(stride_times[:74]))

    else:
        dfa_4_8 = 'NaN'
        dfa_4_10 = 'NaN'
        dfa_4_12 = 'NaN'
        dfa_4_14 = 'NaN'
        sampen_2_020 = 'NaN'
        sampen_2_025 = 'NaN'
        sampen_2_030 = 'NaN'
        sampen_3_025 = 'NaN'
        sampen_3_030 = 'NaN'

    variables.extend([mean_stride_times,cv_stride_times,no_strides,dfa_4_8,dfa_4_10,dfa_4_12,dfa_4_14,sampen_2_020,sampen_2_025,
                      sampen_2_030,sampen_3_025,sampen_3_030])

    dictionary[subject_id] = variables

    print(subject_id + ' done!')
    print('Time spent for this subj : ' + str(datetime.now() - currTime))

# save dictionary on excel
df_vars = pd.DataFrame.from_dict(dictionary,orient='index')
df_vars.to_excel('variables.xlsx',index=True,header=['mean_stride_times','cv_stride_times','no_strides','dfa_4_8','dfa_4_10','dfa_4_12','dfa_4_14',
                                                     'sampen_2_020','sampen_2_025','sampen_2_030','sampen_3_025','sampen_3_030'])




