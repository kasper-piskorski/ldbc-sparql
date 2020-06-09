$STARDOG_HOME/bin/stardog file split -t $SPLIT_TRIPLE_SIZE --compression gzip $RDF_DATA_DIR/social_network_activity_0_0.ttl
mv *.gz $RDF_DATA_DIR
gzip $RDF_DATA_DIR/social_network_person_0_0.ttl
gzip $RDF_DATA_DIR/social_network_static_0_0.ttl
