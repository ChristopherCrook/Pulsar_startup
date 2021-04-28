echo "Fetching Apache Pulsar"
sudo apt install default-jre
wget https://archive.apache.org/dist/pulsar/pulsar-2.7.1/apache-pulsar-2.7.1-bin.tar.gz
tar xvfz apache-pulsar-2.7.1-bin.tar.gz
pip3 install pulsar-client
pip3 install pandas
