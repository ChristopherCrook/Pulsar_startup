## Performance-MQ-Message Size Experiments


For data collection, the program should output (to standard output) a CSV of message send timestamps, and a timestamp of when the acknowledge (ACK) response was received (if your MQ does not support delivery gaurantees, you will need to take some extra measures. See "Notes for MQ's Without ACK" below).

Ex output:

```
1617516000,1617516005
1617516010,1617516015
...
```

# Experiment Configurations

These are the configurations your program should be ran in. Although it is not shown, there should be a separate machine instance for the broker.

| Producer Machines | Producer Instances | Consumer Machines | Consumer Instances | Message Size | Status |
| ----------------- | ------------------ | ----------------- | ------------------ | ------------ | ------ |
| 1                 | 1                  | 1                 | 1                  | tiny         |        |
| 1                 | 1                  | 1                 | 1                  | small        |        |
| 1                 | 1                  | 1                 | 1                  | medium       |        |
| 1                 | 1                  | 1                 | 1                  | large        |        |
| 1                 | 1                  | 1                 | 1                  | x-large      |        |


### 1 Producer 1 Consumer - Tiny Message
Generate `latencies.csv` and `throughput.csv` using the program provided by the experiment designers team.

Fill this table with the appropriate links:

| File Name | Link |
| --- | --- |
| producer.csv | |
| latencies.csv | |
| throughput.csv| |

Calculate the following data using Excel or a custom program by analyzing the data in latencies.csv and throughput.csv

| Metric | Value |
| --- | --- |
| Processing Latency Min | |
| Processing Latency Max | |
| Processing Latency Average | |
| Processing Latency Standard Deviation | |
| Processing Throughput Min | |
| Processing Throughput Max | |
| Processing Throughput Average | |
| Processing Throughput Standard Deviation | |

### 1 Producer 1 Consumer - Small Message 
| File Name | Link |
| --- | --- |
| producer.csv | |
| latencies.csv | |
| throughput.csv| |

Calculate the following data using Excel or a custom program by analyzing the data in latencies.csv and throughput.csv

| Metric | Value |
| --- | --- |
| Processing Latency Min | |
| Processing Latency Max | |
| Processing Latency Average | |
| Processing Latency Standard Deviation | |
| Processing Throughput Min | |
| Processing Throughput Max | |
| Processing Throughput Average | |
| Processing Throughput Standard Deviation | |


### 1 Producer 1 Consumer - Medium Message 
| File Name | Link |
| --- | --- |
| producer.csv | |
| latencies.csv | |
| throughput.csv| |

Calculate the following data using Excel or a custom program by analyzing the data in latencies.csv and throughput.csv

| Metric | Value |
| --- | --- |
| Processing Latency Min | |
| Processing Latency Max | |
| Processing Latency Average | |
| Processing Latency Standard Deviation | |
| Processing Throughput Min | |
| Processing Throughput Max | |
| Processing Throughput Average | |
| Processing Throughput Standard Deviation | |

### 1 Producer 1 Consumer1 - Large Message 
| File Name | Link |
| --- | --- |
| producer.csv | |
| latencies.csv | |
| throughput.csv| |

Calculate the following data using Excel or a custom program by analyzing the data in latencies.csv and throughput.csv

| Metric | Value |
| --- | --- |
| Processing Latency Min | |
| Processing Latency Max | |
| Processing Latency Average | |
| Processing Latency Standard Deviation | |
| Processing Throughput Min | |
| Processing Throughput Max | |
| Processing Throughput Average | |
| Processing Throughput Standard Deviation | |


### 1 Producer 1 Consumer - X-Large Message 
| File Name | Link |
| --- | --- |
| producer.csv | |
| latencies.csv | |
| throughput.csv| |

Calculate the following data using Excel or a custom program by analyzing the data in latencies.csv and throughput.csv

| Metric | Value |
| --- | --- |
| Processing Latency Min | |
| Processing Latency Max | |
| Processing Latency Average | |
| Processing Latency Standard Deviation | |
| Processing Throughput Min | |
| Processing Throughput Max | |
| Processing Throughput Average | |
| Processing Throughput Standard Deviation | |


