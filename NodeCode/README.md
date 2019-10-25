**Overview of the Node Code**

The entire program is run through node_main

The nodes default to a listening state and wait for an input from the aggregator in node_server.

Once the aggregator sends the information the nodes extract the necessary info and reads the training file to extract the raw data.

The node then sends the information to the SVM which, for tau iterations:
  * Shuffles the data (if applicable).
  * Converts the data to a recognizable format.
  * Performs gradient descent on the each data point.

The node then sends the information back to the aggregator with node_client and restarts.
