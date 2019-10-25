**Instructions on how the code on the aggregator works**

The main file to run for the aggregator is either the GUI.py or agg_main_v*.py. The GUI allows for some variable changes whereas the agg_main simply runs for given parameters.

Agg_main starts by detecting all the devices connected to the router and assigns the IPs identifying numbers.

It then initializes some necessary values (w, d, fnfn, accs)

For K global updates
* Data is sent to the nodes using agg_client and the aggregator waits for the nodes to perform calculations.
* Once the nodes have finished, the aggregator receives the new ws and fns from the nodes with agg_server.
* The ws are processed by med_avg to create a new global w. 
* sending data is updated and a quick AccTest runs a quick accuracy test.

ParsFile then processes the loss functions to display a graph of the process. 
