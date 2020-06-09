#!/bin/bash
. ../env_vars.sh
cp stardog.properties ${STARDOG_HOME}stardog.properties
$STARDOG_HOME/bin/stardog-admin server start
$STARDOG_HOME/bin/stardog-admin db drop $SFACTOR

#bulk load
#./prepare-data.sh
$STARDOG_HOME/bin/stardog-admin db create -n $SFACTOR $RDF_DATA_DIR/*.ttl.gz

#gzip $RDF_DATA_DIR/*_0_0.ttl.*
#$STARDOG_HOME/bin/stardog-admin db create -n $SFACTOR $RDF_DATA_DIR/*.ttl.gz

#transactional load - slow
#$STARDOG_HOME/bin/stardog-admin db create -n $RDF_DB
#$STARDOG_HOME/bin/stardog data add $RDF_DB $RDF_DATA_DIR/*.ttl
