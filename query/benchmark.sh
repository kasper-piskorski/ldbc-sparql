. ../env_vars.sh

if [ ${SPARQL_BACKEND} = "stardog" ]; then
    echo "Preparing stardog backend..."
    ./stardog-prepare.sh
fi

mkdir output
echo "About to start benchmark with backend: ${SPARQL_BACKEND}..."

./run_is.sh ${SPARQL_BACKEND} $SEED_PATH $SFACTOR ${SPARQL_SEEDS} ${SPARQL_TIMEOUT_MINS} &> output/${SPARQL_BACKEND}.$SFACTOR.${SPARQL_TIMEOUT_MINS}m.${SPARQL_SEEDS}.is
./run_ic.sh ${SPARQL_BACKEND} $SEED_PATH $SFACTOR ${SPARQL_SEEDS} ${SPARQL_TIMEOUT_MINS} &> output/${SPARQL_BACKEND}.$SFACTOR.${SPARQL_TIMEOUT_MINS}m.${SPARQL_SEEDS}.ic
#./run_bi.sh ${SPARQL_BACKEND} $SEED_PATH $SFACTOR ${SPARQL_SEEDS} ${SPARQL_TIMEOUT_MINS} &> output/${SPARQL_BACKEND}.$SFACTOR.${SPARQL_TIMEOUT_MINS}m.${SPARQL_SEEDS}.bi

