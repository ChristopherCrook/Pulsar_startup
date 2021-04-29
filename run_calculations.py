import os, sys, string, csv
import subprocess
import pandas as pd
import glob
from csv import reader
import statistics


latency_list = []
throughput_list = []

blendedrootdir = 'Results/Blended'
messagesizerootdir = 'Results/Message_size'
actorcountrootdir = 'Results/Actor_Count'
datadir = 'Data'

def get_avg(some_list):
    return sum(some_list) / len(some_list)

def get_min(some_list):
    return min(some_list)

def get_max(some_list):
    return max(some_list)

def get_sd(some_list):
    return statistics.stdev(some_list)

def create_csv(some_latency_list, some_throughput_list, some_file):
    columns = ['Metric', 'value']
    with open (some_file, 'w') as f:
        write = csv.writer(f)
        write.writerow(columns)
        write.writerow(['Processing Latency Min', get_min(some_latency_list)])
        write.writerow(['Processing Latency Max', get_max(some_latency_list)])
        write.writerow(['Processing Latency Average', get_avg(some_latency_list)])
        write.writerow(['Processing Latency Standard Deviation', get_sd(some_latency_list)])
        if len(some_throughput_list) != 0:
            write.writerow(['Processing Throughput Min',get_min(some_throughput_list)])
            write.writerow(['Processing Throughput Max', get_max(some_throughput_list)])
            write.writerow(['Processing Throughput Average', get_avg(some_throughput_list)])
            write.writerow(['Processing Throughput Standard Deviation',  get_sd(some_throughput_list)])
        else:
            write.writerow(['Processing Throughput Min', 'NA'])
            write.writerow(['Processing Throughput Max', 'NA'])
            write.writerow(['Processing Throughput Average', 'NA'])
            write.writerow(['Processing Throughput Standard Deviation', 'NA'])


# GENERATE RESULTS FOR THE BLENDED EXPERIMENT
for subdir, dirs, files in os.walk(blendedrootdir):
    results_file = "" 
    results = subdir + "_results.csv"
    for file in files:
        if file.startswith("latencies") or file.startswith("throughput"):
            results_file = subdir + "_results.csv" 
        if file.startswith("latencies"):    
            with open(os.path.join(subdir, file), 'r') as read_obj:
                read = reader(read_obj)
                for row in read:
                    latency_list.append(float(row[0]))
                    
        if file.startswith("throughput"):              
            with open(os.path.join(subdir, file), 'r') as read_obj:
                read = reader(read_obj)
                for row in read:
                    throughput_list.append(float(row[0]))

    if results_file != "":
        create_csv(latency_list, throughput_list, results_file)
        throughput_list = []
        latency_list = []




# GENERATE RESULTS FOR THE MESSAGE SIZE EXPERIMENT
for subdir, dirs, files in os.walk(messagesizerootdir):
    results_file = "" 
    results = subdir + "_results.csv"
    for file in files:
        if file.startswith("latencies") or file.startswith("throughput"):
            results_file = subdir + "_results.csv" 
        if file.startswith("latencies"):    
            with open(os.path.join(subdir, file), 'r') as read_obj:
                read = reader(read_obj)
                for row in read:
                    latency_list.append(float(row[0]))
                    
        if file.startswith("throughput"):    
            with open(os.path.join(subdir, file), 'r') as read_obj:
                read = reader(read_obj)
                for row in read:
                    throughput_list.append(float(row[0]))

    if results_file != "":
        create_csv(latency_list, throughput_list, results_file)
        throughput_list = []
        latency_list = []


# # GENERATE RESULTS FOR THE ACTOR SIZE EXPERIMENT PT. 2
for subdir, dirs, files in os.walk(actorcountrootdir):
    results_file = "" 
    results = subdir + "_results.csv"

    for file in files:
        if file.startswith("latencies") or file.startswith("throughput"):
            results_file = subdir + "_results.csv" 
        if file.startswith("latencies"):    
            with open(os.path.join(subdir, file), 'r') as read_obj:
                read = reader(read_obj)
                for row in read:
                    latency_list.append(float(row[0]))
    
        if file.startswith("throughput"):    
            with open(os.path.join(subdir, file), 'r') as read_obj:
                read = reader(read_obj)
                for row in read:
                    throughput_list.append(float(row[0]))

    if results_file != "":
        create_csv(latency_list, throughput_list, results_file)
        throughput_list = []
        latency_list = []
    else:
        throughput_list = []
        latency_list = []

                        


