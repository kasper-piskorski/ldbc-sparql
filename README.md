# LDBC SNB SPARQL implementation

[SPARQL 1.1](https://www.w3.org/TR/sparql11-query/) implementation of the [LDBC SNB BI benchmark](https://github.com/ldbc/ldbc_snb_docs).

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

Once these are specified, the loading can be initiated by running the `load-to-virtuoso.sh` script.

### Loading with Virtuoso
When loading with Virtuoso, the additional env vars of `VIRTUOSO_HOME`, `VIRTUOSO_AVAILABLE_MEMORY_GB`, `VIRTUOSO_DB_SIZE_GB` and `VIRTUOSO_LOADERS` need to be defined in `env_vars.sh`:

```bash
export VIRTUOSO_HOME=/path/to/virtuoso/dir
export VIRTUOSO_AVAILABLE_MEMORY_GB=8
export VIRTUOSO_DB_SIZE_GB=10
export VIRTUOSO_LOADERS=4
```

The `VIRTUOSO_AVAILABLE_MEMORY` determines the number of buffers and maximum number of dirty buffers created when loading which affects loading performance. `VIRTUOSO_DB_SIZE_GB` determines maximum renapping checkpoint. `VIRTUOSO_LOADERS` specifies how many loaders will be created when loading. For best performance it should amount to `no_of_available_cores/2.5`.

Before initiating the loading, the `virtuoso-prepare.sh` script should be run after which the Virtuoso server should be restarted. After doing that, the loading can be started by running `load-to-virtuoso.sh` script.


### Running the query benchmark
The query benchmark can be started by running the `benchmark.sh` script
