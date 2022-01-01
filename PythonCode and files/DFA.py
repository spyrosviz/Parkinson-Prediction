import numpy as np
from sklearn.linear_model import LinearRegression
from scipy import signal

'''Detrended Fluctuation Analysis'''

def DFA (lista,min_box_size,max_box_size,show=False):
    lista = np.array(lista)
    cumsum = np.cumsum(lista-np.mean(lista))
    RMS = []


    '''# mean centered cumulation sum
    for i,num in enumerate(lista):
        
        if i == 0: 
            a = num - np.mean(lista)            
            cumsum.append(a)
            continue

        a = a + num - np.mean(lista)           
        cumsum.append(a)'''

    
     
    for box_size in range (min_box_size,max_box_size + 1):
        k = 0
        rms_windows = []
        while k <= len(cumsum)- box_size:
            window = cumsum[k:k+box_size]
            window = np.array(window)
            rms = np.sqrt(np.mean(signal.detrend(window)**2))
            rms_windows.append(rms)
            k = k + box_size
                
 
        else:
            rms_windows = np.array(rms_windows)
            mean_rms = np.sqrt(np.mean(rms_windows**2))
            RMS.append(mean_rms)

    RMS = np.array(RMS)
    RMS_log = np.log2(RMS).reshape(-1,1)
    scale_log = [np.log2(x) for x in range (min_box_size,max_box_size+1)]
    scale_log = np.array(scale_log)
    x = scale_log.reshape(-1,1)

    LinReg = LinearRegression()

    try:
        LinReg.fit(x,RMS_log)
    except:
        return "something went wrong in DFA algorithm"

    alpha = LinReg.coef_

    return alpha




