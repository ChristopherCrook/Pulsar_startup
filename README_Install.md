Run the Installer script using the following command:
> sudo sh ./install.sh

Once the Apache Pulsar file exists in the home directory, run
the following command from the Apache Pulsar directory:
> bin/pulsar standalone

The script for installation would have copied over the run_producer 
and run_consumer scripts.

Run each of these scripts in a separate shell from the Apache Pulsar 
directory.


To run the calculations:
> sudo sh ./mq-data-processor/generate_latencies_throughputs.sh
> python3 prep_actor_count.py
> python3 run_calculations.py
