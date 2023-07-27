import h5py
import scipy.io as sio
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn import metrics
import matplotlib.pyplot as plt

label=h5py.File('result_of_the_model&manully_labeled/CSPC2020label_04_by_manurally.mat')
actual_y = label['sqi'][0:500]
actual_y = actual_y.reshape(500)
print(actual_y.shape)

predicted = sio.loadmat('2020label_04_result.mat')['predict']
predicted = predicted.reshape(500)
print(predicted.shape)

# accuracy
results = metrics.accuracy_score(actual_y, predicted)
print("Test Accuracy: ", results)

confusion_matrix = confusion_matrix(actual_y, predicted)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix)
cm_display.plot()
plt.show()
