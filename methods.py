import numpy as np
import json
from time import sleep
from node import Neuron

### GLOBALS ###
nodes_dict = {} ## A list containing all the nodes from the interface
synapses_dict = {} ## A dictionary containing synapses

simulation_ON_flag = True


def run(diagram_structure):
	"""
	 function 'run' makes the bridge between our javascript diagram and the python simulation.
	 Receive the argument 'diagram_structure' in a stringified json format containing the diagram structure properties.
	"""

	global nodes_dict, synapses_dict

	structure_data = json.loads(diagram_structure)

	for ii in range(len(structure_data["nodeDataArray"])):  ### Set up the nodes ###
				
		try: node_type = structure_data["nodeDataArray"][ii]['neuron_type'] ## Im doing a try/catch to set the neuron type to something in case it was not defined from
		except: node_type = "IaF"											## the interface... in future, such property should be set to a default mode...
		
		node_name = structure_data["nodeDataArray"][ii]["text"] ## Get an id for the neuron and set it to the dictionary
		nodes_dict[node_name] = Neuron(node_type)


	for ii in range(len(structure_data["linkDataArray"])): ### Set up synapses ###
		synapses_dict[ii] = {}
		synapses_dict[ii]['from']         = structure_data["linkDataArray"][ii]["from"]
		synapses_dict[ii]['to']           = structure_data["linkDataArray"][ii]["to"]
		
		try:    synapses_dict[ii]['synapse_type'] = structure_data["linkDataArray"][ii]["synapse_type"] ## Again the try/except .... make synapse type a default value from the interface
		except: synapses_dict[ii]['synapse_type'] = 'excitatory'

		synapses_dict[ii]['weight'] = np.random.uniform(0,1, nodes_dict[node_name].number_of_neurons   ) ## Set a random weight

		if synapses_dict[ii]['synapse_type'] == 'inhibitory' :  synapses_dict[ii]['weight'] *= -1

	loop()
	# print nodes_dict

def loop():
	global nodes_dict, synapses_dict, simulation_ON_flag

	while simulation_ON_flag:

		for ii in synapses_dict:
			nodes_dict[ synapses_dict[ii]['to']  ].input_weights.append( synapses_dict[ii]['weight'] )
			nodes_dict[ synapses_dict[ii]['to']  ].input_activity.append( nodes_dict[synapses_dict[ii]['from']].node_activity  )

		for ii in nodes_dict:
			nodes_dict[ii].update()

		# print nodes_dict['Cell2'].node_activity.shape, nodes_dict['Cell2'].input_activity.shape , nodes_dict['Cell2'].input_weights.shape


def stop_simulation():
	simulation_ON_flag = False