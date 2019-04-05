import ditk

class longae(ditk.graph_completion):
	"""longae is the implementation of the "Autoencoders for Unsupervised Link Prediction and Semi-Supervised Node Classification"
	project.
	"""
	model = None

	@classmethod
	def read_dataset(cls, fileNames, options=None):
		"""
		Reads a dataset in preparation for: train or test. Returns data in proper format for: train or test.

		Args:
			cls: class instance
			fileNames: list-like. List of files representing the dataset to read. Each element is str, representing 
				filename [possibly with filepath]
			options: object to store any extra or implementation specific data

		Returns:
			A tuple (e.g. train_X, train_Y, dev_X, dev_Y, test_X, test_Y) in proper format for train and test. Dev set may be optional for some.
			Note:
				X: represents features and data instances [i.e. the data you want to train/predict on]
				Y: represents the ground truth or labels for each of the data instances [i.e. the value/label you want to predict]

		Raises:
			None
		"""
		# open dataset files and does preprocessing
		pass


	@classmethod
	def train(cls, data_X, data_Y, options=None):
		"""
		Trains a model on the given input data

		Args:
			cls: class instance
			data_X: iterable of arbitrary format. represents the data instances and features you use to train your model.
			data_Y: iterable of arbitrary format. represents the ground truth, used in training/optimizing your model.
				Note: data_X and data_Y are in format returned by read_dataset_train() [i.e. read_dataset using 'train' mode]
			options: object to store any extra or implementation specific data

		Returns:
			ret: None. Trained model stored internally to class instance state. 

		Raises:
			None
		"""
		# updates model with proper weights
		pass


	@classmethod
	def predict(cls, data_X, options=None):
		"""
		Predicts on the given input data. Assumes model has been trained with train()

		Args:
			cls: class instance
			data_X: iterable of arbitrary format. represents the data instances and features you use to make predictions
				Note that prediction requires trained model. Precondition that class instance already stores rained model 
				information.
			options: object to store any extra or implementation specific data

		Returns:
			predictions: output model predictions for data_X.
				
		Raises:
			None
		"""
		# outputs model estimation on link prediction or entity prediction
		pass

	@classmethod
	def evaluate(cls, test_X, test_Y, options=None):
		"""
		Calculates evaluation metrics on chosen benchmark dataset

		Args:
			cls: class instance
			predictions: [tuple,...], list of tuples [same format as output from predict]
			groundTruths: [tuple,...], list of tuples representing ground truth.
				precondition: len(predictions) == len(groundTruth) i.e. like parallel-array, so
					prediction[i] and groundTruth[i] represent the prediction tuple and
					the groundTruth tuple for the same datapoint i.
			options: object to store any extra or implementation specific data

		Returns:
			metrics: tuple of each evaluation metric. Each element is float.

		Raises:
			None
		"""
		# outputs scores of model performance relative to ground truth on benchmarks
		pass
		
"""
Example pipeline:

from ditk_longae import longae

train_x, train_y, test_x, test_y = longae.read_dataset(['file1', 'file2'])
longae.train(train_x, train_y)
y_hat = longae.predict(test_x)
scores = longae.evaluate(test_y, y_hat)
print(scores)
"""