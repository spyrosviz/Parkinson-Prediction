import pandas as pd
import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

def find_stride_times(forces_r,forces_l,fs,plot=False):

    strides_r, _ = find_peaks(forces_r, distance=0.5 * fs,prominence=100)
    strides_l, _ = find_peaks(forces_l, distance=0.5 * fs, prominence=100)

    stride_times_r = []
    stride_times_l = []

    for s in range(0,len(strides_r)-1):
        time_diff = (strides_r[s + 1] - strides_r[s]) / fs
        stride_times_r.append(time_diff)

    for s in range(0,len(strides_l)-1):
        time_diff = (strides_l[s + 1] - strides_l[s]) / fs
        stride_times_l.append(time_diff)

    steps = sorted((strides_r/fs).tolist() + (strides_l/fs).tolist())
    step_times = []

    for s in range(1,len(steps)):

        step_interval = steps[s] - steps[s-1]
        step_times.append(step_interval)

    right_steps = []
    left_steps = []

    if strides_r[0] < strides_l[0]:
        right_steps = step_times[::2]
        left_steps = step_times[1:2]

    else:
        left_steps = step_times[::2]
        right_steps = step_times[1:2]

    mean_right = np.mean(np.array(right_steps))
    mean_left = np.mean(np.array(left_steps))

    leg_imbalance = (abs(mean_right - mean_left))/(mean_right + mean_left)

    if plot == True:
        plt.figure(figsize=[10, 10])
        plt.plot(forces_r)
        plt.plot(strides_r, forces_r[strides_r], "x")
        plt.title("Strides find")
        plt.xlabel("Number of frames")
        plt.ylabel("Force (N)")
        plt.show()

    return stride_times_r, len(strides_r), len(steps), step_times, leg_imbalance

if __name__ == '__main__':

    path = r"C:\Users\spyro\OneDrive\Documents\ΣΠΥΡΟΣ\Pycharm Projects\Github\Parkinson stage prediction\Walks\GaCo01_01.txt"
    df = pd.read_csv(path,usecols = [17,18],delimiter = '\t', header = None,names = ['Left', 'Right'])
    steps = find_stride_times(df['Right'].values,df['Left'].values,100,plot=True)
    print(steps)




