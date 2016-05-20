import numpy as np

class Neuron():

	def __init__(self, node_type=None, number_of_neurons=[5,5] ):
		self.node_type = node_type
		self.number_of_neurons = number_of_neurons # Defines the size of a 2D array
		self.node_activity = np.zeros(self.number_of_neurons)  ## Initial neurons value

		self.input_activity = [] ## Set lists to append activity and weights from the synapses
		self.input_weights  = [] 


	def update(self):

		self.input_activity = np.asarray(self.input_activity)
		self.input_weights  = np.asarray(self.input_weights)

		print self.input_weights.shape, self.input_activity.shape, self.node_activity.shape

		if self.node_type == "random":
			self.node_activity = np.random.uniform( 0,1,self.number_of_neurons )

		if self.node_type == "IaF":
			# self.node_activity += np.dot( self.input_activity , self.input_weights )
			pass

		self.input_activity = [] ## Set lists empty for next iteration
		self.input_weights  = [] 