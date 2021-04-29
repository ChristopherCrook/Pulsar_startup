import os, sys, string, csv
import subprocess
import glob
from csv import reader
import statistics



datadir = 'Data'


# GENERATE RESULTS FOR THE ACTOR SIZE EXPERIMENT PT. 1
def write_actor_count(some_file_path, row):
    with open (some_file_path, 'a') as f:
        write = csv.writer(f)
        write.writerow(row)

for subdir, dirs, files in os.walk(datadir):
    #print(subdir)
    curr_path = os.path.basename(os.path.normpath(subdir))
    if (curr_path.startswith('1-and-1')):
        for file in files:
            with open(os.path.join(subdir, file), 'r') as read_obj:
                read = reader(read_obj)
                for row in read:
                    write_actor_count('Data/actor_count/1-and-1.csv', row)
    if (curr_path.startswith('1prod-5cons')):
        for file in files:
            with open(os.path.join(subdir, file), 'r') as read_obj:
                read = reader(read_obj)
                for row in read:
                    write_actor_count('Data/actor_count/1prod-5cons.csv', row)
    if (curr_path.startswith('1con-5prods')):
        for file in files:
            with open(os.path.join(subdir, file), 'r') as read_obj:
                read = reader(read_obj)
                for row in read:
                    write_actor_count('Data/actor_count/5prod-1con.csv', row)

