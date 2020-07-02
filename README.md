# LDBC SNB SPARQL implementation

[SPARQL 1.1](https://www.w3.org/TR/sparql11-query/) implementation of the [LDBC SNB benchmark](https://github.com/ldbc/ldbc_snb_docs).

## General Remarks
Two RDF backends are currently supported: {virtuoso, stardog}

The backend is specified by defining the `SPARQL_BACKEND` variable in `env_vars.sh`.
Once the dataset to be loaded is generated, the `RDF_DATA_DIR` and `SEED_PATH` variables should be updated accordingly to contain the path where ttl files and substitution params are stored respectively, i.e. the `env_vars.sh` file should contain entries of the form:

```bash
export RDF_DATA_DIR=/path/to/the/ttl/files
export SEED_PATH=/path/to/substitution/params
```

The query benchmark parameters are contained in two env variables specifying number of substitution parameters (seeds) used per single query type and query timeout 
```
export SPARQL_SEEDS=5
export SPARQL_TIMEOUT_MINS=30
```

## Loading datasets

### Generating datasets

Datasets can be generated using the facilities at [DATAGEN](https://github.com/ldbc/ldbc_snb_datagen/). For RDF backends, use the `TTL` format:

```
ldbc.snb.datagen.serializer.personSerializer:ldbc.snb.datagen.serializer.snb.interactive.TurtlePersonSerializer
ldbc.snb.datagen.serializer.invariantSerializer:ldbc.snb.datagen.serializer.snb.interactive.TurtleInvariantSerializer
ldbc.snb.datagen.serializer.personActivitySerializer:ldbc.snb.datagen.serializer.snb.interactive.TurtlePersonActivitySerializer
```


### Loading with Stardog
When loading with Stardog, the additional env vars of `STARDOG_HOME` and `STARDOG_SERVER_JAVA_ARGS` need to be specified in `env_vars.sh`:

```bash
export STARDOG_HOME=/path/to/stardog/dir
export STARDOG_SERVER_JAVA_ARGS="-Xms16G -Xmx16G -XX:MaxDirectMemorySize=128G"
```

Once these are specified, the loading can be initiated by running the `load-to-stardog.sh` script.

### Loading with Virtuoso
When loading with Virtuoso, the additional env vars of `VIRTUOSO_HOME`, `VIRTUOSO_AVAILABLE_MEMORY_GB`, `VIRTUOSO_DB_SIZE_GB` and `VIRTUOSO_LOADERS` need to be defined in `env_vars.sh`:

```bash
export VIRTUOSO_HOME=/path/to/virtuoso/dir
export VIRTUOSO_AVAILABLE_MEMORY_GB=8
export VIRTUOSO_DB_SIZE_GB=10
export VIRTUOSO_LOADERS=4
```

The `VIRTUOSO_AVAILABLE_MEMORY` determines the number of buffers and maximum number of dirty buffers created when loading which affects loading performance. `VIRTUOSO_DB_SIZE_GB` determines maximum renapping checkpoint. `VIRTUOSO_LOADERS` specifies how many loaders will be created when loading. For best performance it should amount to `no_of_available_cores/2.5`.

**NB: Before loading:**
- run the `virtuoso-prepare.sh` script
- restart virtuoso

After doing that, the loading can be started by running the `load-to-virtuoso.sh` script.


## Running the query benchmark
The query benchmark can be started by simply running the `benchmark.sh` script located in the `query` directory. The script requires the underlying backend to be running. The script uses parameters specified in `env_vars.sh` file. The script triggers execution of all possible queries. Single queries can be executed by running the `sparql_driver.py` located in the `query/src` directory:

```
python3 -u sparql_driver.py -b $backend -db $database -qt $qtype -qn $query_number -n $seeds -p $seed_path -to $timeout
```
where the parameters have the following meaning:
- backend  - either `stardog` or `virtuoso`
- database - target database name to be queried
- qtype - benchmark query type, a value from {is, ic, bi}
- query_number - specific number of the query to be executed
- seeds - number of seeds (substitution parameters) used
- seed_path - path to directory where seeds are located
- timeout - query timeout in minutes

## Adding new backend
All driver implementations are located in `src` directory. To add a new backend:
- new query runner needs to be implemented inheriting from `SparqlQueryRunner` defined in `sparql_query_runner.py`. Example implementations are located in `stardog_query_runner.py` and `virtuoso_query_runner.py`.
- the new query runner should implement a `runQuery` method which executes an injected query in string representation against a specific backend.
- SPARQL driver in `sparql_driver.py` needs to be updated to include the newly created runner, example:
```
    queryRunner =  newbackend_query_runner.NewBackendQueryRunner(args.database, timeout, QUERY_DIR)

    seeds = seed_generator.get_seeds(args.path, args.num, args.qtype, args.qno, DATE_FORMAT)
    driver.run_queries(seeds, args.qtype, args.qno, queryRunner)
```
