import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

def print_classification_results(model, y, y_pred, labels=['True','False']):
	'''
	Show classification results.
	This will create a plot with the confusion matrix and another one
	showing the precision against the recall and print the classification
	report.

	Args:
		model:  The fitted model
		y:      The true y values
		y_pred: The predicted y values
	'''
	fig,ax = plt.subplots(1,2, figsize=(9,3))

	cm = confusion_matrix(y, y_pred)
	ConfusionMatrixDisplay(cm, display_labels=labels).plot(ax=ax[0])

	precisions, recalls, thresholds = precision_recall_curve(y, y_pred)
	ax[1].plot(thresholds, precisions[:-1], "b--", label="Precision")
	ax[1].plot(thresholds, recalls[:-1], "g-", label="Recall")
	ax[1].grid()
	ax[1].legend()

	plt.tight_layout()
	plt.show()
	print(classification_report(y, y_pred))
	print()
