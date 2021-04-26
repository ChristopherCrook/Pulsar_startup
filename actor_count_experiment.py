import os, sys, string, csv, pandas
from csv import reader
import statistics


latency = 'Results/Actor_Count/1p_1c/latencies.csv'
latency_list = []

throughput = 'Results/Actor_Count/1p_1c/throughput.csv'
throughput_list = []


with open(latency, 'r') as read_obj:
    read = reader(read_obj)
    for row in read:
        latency_list.append(float(row[0]))

with open(throughput, 'r') as read_obj:
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

def create_csv():
    columns = ['Metric', 'value']
    with open ('Results/Actor_Count/1p_1c/results.csv', 'w') as f:
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


create_csv()

