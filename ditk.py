import abc

class graph_completion(abc.ABC):	
	# The output of each of the following methods should be defined clearly and shared between all methods implemented by members of the group. 
	
	@classmethod
	@abc.abstractmethod
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
		pass


	@classmethod
	@abc.abstractmethod
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
		pass


	@classmethod
	@abc.abstractmethod
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
			predictions: [tuple,...], i.e. list of tuples. 
				Each tuple is (start index, span, mention text, mention type)
				Where:
				 - start index: int, the index of the first character of the mention span. None if not applicable.
				 - span: int, the length of the mention. None if not applicable.
				 - mention text: str, the actual text that was identified as a named entity. Required.
				 - mention type: str, the entity/mention type. None if not applicable.

				 NOTE: len(predictions) should equal len(data_X) AND the ordering should not change [important for 
				 	evalutation. See note in evaluate() about parallel arrays.]
				
		Raises:
			None
		"""
		pass

	@classmethod
	@abc.abstractmethod
	def evaluate(cls, test_X, test_Y, options=None):
		"""
		Calculates evaluation metrics on chosen benchmark dataset [Precision,Recall,F1, or others...]

		Args:
			cls: class instance
			predictions: [tuple,...], list of tuples [same format as output from predict]
			groundTruths: [tuple,...], list of tuples representing ground truth.
				precondition: len(predictions) == len(groundTruth) i.e. like parallel-array, so
					prediction[i] and groundTruth[i] represent the prediction tuple and
					the groundTruth tuple for the same datapoint i.
			options: object to store any extra or implementation specific data

		Returns:
			metrics: tuple with (p,r,f1). Each element is float.

		Raises:
			None
		"""
		pass
