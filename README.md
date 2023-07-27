# signal-quality-assessment-by-residual-recurrent-based-deep-learning-method
This model was designed for classifaction the signal quality of the dynamic ECGs collected by wearable devices. In order to avoid the misjudgment of manually designed features on ECG data and improve the classification accuracy, we designed one deep learning model combined the residual module and recurrent module. The signal qulaity was classcified to three categories: good (label:0) \ medium (label:1) \ bad (label:2).
The model was trained on the wearable ECG segments with ten-fold cross validation method. The collected dynamic ECG segments randomly divided into 10 parts, nine of which was used as training data and the rest part was utilized as validation data in each fold.


The ECG data was collected by wearable ECG monitoring devices, which collect standard lead-I and lead-II ECG signal with a sampling frequency of 400 Hz and 16-bit resolution over a range of ±10 mV. The ECG data was collected from twenty patients who has or had cardiovascular disease and these collected records contain a variety of abnormal heart rhythms, such as premature ventricular beats (PVC),premature atrial beats (PAC) and atrial fibrillation (AF). A fixed time window of 10 s was used for segmenting the ECG episodes.

The collected ECG segments were classified into three categories according to the complexity of the noise in the segments and its influence on signal feature points.The signal of good quality indicates that the ECG segment is subject to a small amount of noise interference, and contains clear QRS waveform. Feature points such as T and P wave were clearly visible, and can be easily recognized.

The signal of medium quality indicates that the ECG segment under the interference of various noises but without the large-scale pulse signal. And the feature points such as P and T wave cannot be easily located. However, the QRS wave in the segment can still be accurate discrimination which means the noise in the ECG segment does not affect the judgment of heart rate information.

The signal of bad quality indicate that the ECG segment contains little information such as the signal of Lead detachment and white noise, or the segment was interfered by large noises. some signal may contain large pulse interference which can affect the detection of the QRS. Some segments may contain large baseline drift, resulting in an extremely change overall amplitude and the inability to locate its QRS position.

# codes
The model was trained by pytorch, the python code was available and the trained model was named as "trained_model_RRM.pkl". The test code was also available.
There also provide the signal quality result of patient number 02&04 in the cspc 2020database, the manurally label was also provide for assessment the accuracy of the proposed model.

The model was developed by Xiangyu Zhang （230179249@seu.edu.cn, Southeast University, China）. 

Further details will be seen in our paper--"Deep-learning based signal quality assessment for wearable ECGs".


# Training Dataset
https://physionet.org/content/challenge-2011/1.0.0/