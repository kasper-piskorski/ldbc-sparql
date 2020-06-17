#!/bin/bash
backend=$1
seed_path=$2
database=$3
seeds=$4
timeout=$5
qtype="is"

total_timeout=$((seeds * timeout))
echo "Running IC queries..."
for query_number in {1..9}
do
	#-u option for disabling buffering for stdout
	timeout ${total_timeout}m python3 -u src/sparql_driver.py -b $backend -db $database -qt $qtype -qn $query_number -n $seeds -p $seed_path -to $timeout
done