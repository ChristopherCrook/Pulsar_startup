python3 main.py -d ../Data/tiny/1-and-1
mv latencies.csv ../Results/Blended/1p_1c_tiny
mv throughput.csv ../Results/Blended/1p_1c_tiny
python3 main.py -d ../Data/small/1prod-5cons
mv latencies.csv ../Results/Blended/1p_5c_small
mv throughput.csv ../Results/Blended/1p_5c_small
python3 main.py -d ../Data/medium/1con-5prods
mv latencies.csv ../Results/Blended/5p_1c_medium
mv throughput.csv ../Results/Blended/5p_1c_medium
python3 main.py -d ../Data/large/producers
mv latencies.csv ../Results/Blended/24p_24c_large
mv throughput.csv ../Results/Blended/24p_24c_large

python3 main.py -d ../Data/tiny/1-and-1
mv latencies.csv ../Results/Message_size/1p_1c_tiny
mv throughput.csv ../Results/Message_size/1p_1c_tiny
python3 main.py -d ../Data/small/1-and-1
mv latencies.csv ../Results/Message_size/1p_1c_small
mv throughput.csv ../Results/Message_size/1p_1c_small
python3 main.py -d ../Data/medium/1-and-1
mv latencies.csv ../Results/Message_size/1p_1c_medium
mv throughput.csv ../Results/Message_size/1p_1c_medium
python3 main.py -d ../Data/large/1-and-1
mv latencies.csv ../Results/Message_size/1p_1c_large
mv throughput.csv ../Results/Message_size/1p_1c_large
python3 main.py -d ../Data/xlarge/1-and-1
mv latencies.csv ../Results/Message_size/1p_1c_xlarge
mv throughput.csv ../Results/Message_size/1p_1c_xlarge

python3 ../prep_actor_count.py
python3 main.py -d ../Data/actor_count/1-and-1
mv latencies.csv ../Results/Actor_Count/1p_1c
mv throughput.csv ../Results/Actor_Count/1p_1c
python3 main.py -d ../Data/actor_count/1prod-5cons
mv latencies.csv ../Results/Actor_Count/1p_5c
mv throughput.csv ../Results/Actor_Count/1p_5c

## For some reason generating their throughput freezes
#python3 main.py -d ../Data/actor_count/5prod-1con
#mv latencies.csv ../Results/Actor_Count/5p_1c
#mv throughput.csv ../Results/Actor_Count/5p_1c