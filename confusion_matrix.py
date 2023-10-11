import h5py
import scipy.io as sio
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report
from sklearn import metrics
import matplotlib.pyplot as plt
import pickle
# label=sio.loadmat('result_of_the_model&manully_labeled/CSPC2020label_02_0_1_by_manurally.mat')
# actual_y = label['sqi'].reshape(8218, 1)
with open('testing_dataset.pkl', 'rb') as f:
    actual = pickle.load(f)
with open('2011_label_predict_by_model_trainied_on_patient_02.pkl', 'rb') as f:
    predicted = pickle.load(f)

actual_y = actual[:, -1].reshape(198, 1)
predicted = np.array(predicted).reshape(198, 1)
# actual_y = actual_y[0:500]
# actual_y = label['sqi'].reshape(500)
# print(label['sqi'].shape)

# predicted = sio.loadmat('2020label_02_result_trained_on_computer.mat')['predict']
# predicted = predicted.reshape(8218, 1)
print(predicted.shape)

target_names = ['acceptable 0', 'unacceptable 1']
print(classification_report(actual_y, predicted, target_names=target_names))

# accuracy
results = metrics.accuracy_score(actual_y, predicted)
print("Test Accuracy: ", results)

confusion_matrix = confusion_matrix(actual_y, predicted)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix)
cm_display.plot()
plt.show()
