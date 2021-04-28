import os, sys, string, csv, pandas
from csv import reader
import statistics


latency_tiny = 'Results/Message_Size/1p_1c_tiny/latencies.csv'
latency_tiny_list = []

throughput_tiny = 'Results/Message_Size/1p_1c_tiny/throughput.csv'
throughput_tiny_list = []

latency_small = 'Results/Message_Size/1p_1c_small/latencies.csv'
latency_small_list = []

throughput_small = 'Results/Message_Size/1p_1c_small/throughput.csv'
throughput_small_list = []

latency_medium = 'Results/Message_Size/1p_1c_medium/latencies.csv'
latency_medium_list = []

throughput_medium = 'Results/Message_Size/1p_1c_medium/throughput.csv'
throughput_medium_list = []

latency_large = 'Results/Message_Size/1p_1c_large/latencies.csv'
latency_large_list = []

throughput_large = 'Results/Message_Size/1p_1c_large/throughput.csv'
throughput_large_list = []


def populate_list(latency_file, latency_list, throughput_file, throughput_list):
    with open(latency_file, 'r') as read_obj:
        read = reader(read_obj)
        for row in read:
            latency_list.append(float(row[0]))

    with open(throughput_file, 'r') as read_obj:
        read = reader(read_obj)
        for row in read:
            throughput_list.append(float(row[0]))

def get_avg(some_list):
    return sum(some_list) / len(some_list)

def get_min(some_list):
    return min(some_list)

def get_max(some_list):
    return max(some_list)

def get_sd(some_list):
    return statistics.stdev(some_list)

def create_csv(latency_list, throughput_list, some_file):
    columns = ['Metric', 'value']
    with open (some_file, 'w') as f:
        write = csv.writer(f)
        write.writerow(columns)
        write.writerow(['Processing Latency Min', get_min(latency_list)])
        write.writerow(['Processing Latency Max', get_max(latency_list)])
        write.writerow(['Processing Latency Average', get_avg(latency_list)])
        write.writerow(['Processing Latency Standard Deviation', get_sd(latency_list)])
        write.writerow(['Processing Throughput Min', get_min(throughput_list)])
        write.writerow(['Processing Throughput Max', get_max(throughput_list)])
        write.writerow(['Processing Throughput Average', get_avg(throughput_list)])
        write.writerow(['Processing Throughput Standard Deviation', get_sd(throughput_list)])


populate_list(latency_tiny, latency_tiny_list, throughput_tiny, throughput_tiny_list)
create_csv(latency_tiny_list, throughput_tiny_list, 'Results/Message_Size/1p_1c_tiny/results.csv')
populate_list(latency_small,  latency_small_list, throughput_small, throughput_small_list)
create_csv(latency_small_list, throughput_small_list, 'Results/Message_Size/1p_1c_small/results.csv')
populate_list(latency_medium, latency_medium_list, throughput_medium, throughput_medium_list)
create_csv(latency_medium_list, throughput_medium_list, 'Results/Message_Size/1p_1c_medium/results.csv')
populate_list(latency_large,  latency_large_list, throughput_large, throughput_large_list)
create_csv(latency_large_list, throughput_large_list, 'Results/Message_Size/1p_1c_large/results.csv')



