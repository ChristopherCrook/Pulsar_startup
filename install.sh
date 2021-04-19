echo "Fetching Apache Pulsar"
wget https://archive.apache.org/dist/pulsar/pulsar-2.7.1/apache-pulsar-2.7.1-bin.tar.gz
cp apache-pulsar-2.7.1-bin.tar.gz ~
cd ~
tar xvfz apache-pulsar-2.7.1-bin.tar.gz
cp run_consumer.sh ~/apache-pulsar-2.7.1
cp run_producer.sh ~/apache-pulsar-2.7.1
pip3 install pulsar-client
