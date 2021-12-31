# Parkinson Prediction

## Aim of project
This project aims to make and compare machine learning algorithms in classifying parkinson from healthy individuals based on different features.

## Source of data
Data were found on physionet.org in Gait in Parkinson's Disease database. 

## Citation
Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. C., Mark, R., ... & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. Circulation [Online]. 101 (23), pp. e215–e220.

## Project description
The project contains data from 93 parkisnon subjects and 73 healthy controls. The files that were downloaded are an excel file with demographic data and a file for each subject containing force sensor data during 2 minutes of self paced, level ground walking. During walking each subject was wearing 8 force sensors on each foot (Ultraflex Computer Dyno Graphy, Infotronic Inc.), recording data. On this project, a step counter algorithm was made from force sensors data and several gait features were extracted in order to combine them with the other variables in the excel. Some of these were alpha exponent from detrended fluctuation analysis  of stride intervals and sample entropy from stride intervals.  The parameters selected for dfa and sample entropy were:

**DFA**
* (min_window_size=4,max_window_size=8)
* (min_window_size=4,max_window_size=10)
* (min_window_size=4,max_window_size=12)
* (min_window_size=4,max_window_size=14)

**Sample Entropy**
* (m=2,r=0.2*sd)
* (m=2,r=0.25*sd)
* (m=3,r=0.3*sd)
* (m=3,r=0.25*sd)
* (m=3,r=0.3*sd)

## Project Limitations
* Data from this project are aggregated from 3 different studies so there might be some variability regarding different experimenters and different location of 2 minutes walking.
* Detrended fluctuation analysis and sample entropy, normally require a larger number of data points than the ones used in this project. This is because each subject had 2 minutes of walking which means every subject had different number of strides, thus different data points for analysis. To overcome this issue, the number of strides selected was the minimum one found in walking trials which results in few stride times for analysis. Sample entropy is less sensitive in data points length however it has been found that it's best to be used when data points >= 200 (Yentes et al. 2013). In detrended fluctuation analysis for gait analysis a larger minimum number of samples is required, around 500-600 (Damouras et al. 2010). However there are indications that  even shorter data points from 3 and 6 minutes of treadmill walking trials, result in reliable alpha exponent values (Pierrynowski et al. 2005).
* The proposed parameters for detrended fluctuation analysis in gait are minimum window size of 16 and maximum window size of N/16, where N is the number of stride intervals (Damouras et al. 2010). However because number of stride intervals is very low in this project we used much smaller parameteres. The project's aim is not to interpret the meaning of DFA and Sample Entropy in parkinson's compared to healthy individuals. Instead the aim is to find good predictors in order to make a more robust machine learning model to classify parkinson and healthy subjects.
