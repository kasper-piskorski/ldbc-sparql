${STARDOG_HOME}bin/stardog-admin server stop
cp ../load/stardog.properties ${STARDOG_HOME}stardog.properties
sed -i '.original' "s|# query.timeout.*|query.timeout=${SPARQL_TIMEOUT_MINS}m|g" ${STARDOG_HOME}stardog.properties
sed -i '.original' "s|strict.parsing.*|strict.parsing=false|g" ${STARDOG_HOME}stardog.properties
sed -i '.original' "s|memory.mode.*|memory.mode=read_optimized|g" ${STARDOG_HOME}stardog.properties
sed -i '.original' "s|.*database.connection.timeout.ms.*|database.connection.timeout=${SPARQL_TIMEOUT_MINS}m|g" ${STARDOG_HOME}stardog.properties
${STARDOG_HOME}bin/stardog-admin server start
