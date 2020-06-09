CONFIG="${VIRTUOSO_HOME}"/database/virtuoso.ini
TIMEOUT_S=$(( SPARQL_TIMEOUT_MINS * 60))

#2/3 of available mem in 8k pages
NUMBER_OF_BUFFERS=$(( VIRTUOSO_AVAILABLE_MEMORY_GB * 660000/8))
MAX_DIRTY_BUFFERS=$(( NUMBER_OF_BUFFERS * 3/4))
#0.75 x db size in 8k pages
MAX_CHECKPOINT_REMAP=$(( VIRTUOSO_DB_SIZE_GB * 750000/8))
MAX_MEM_POOLSIZE=800000000

echo $NUMBER_OF_BUFFERS
echo $MAX_DIRTY_BUFFERS
echo $MAX_CHECKPOINT_REMAP

sed -i "s|DirsAllowed.*|DirsAllowed= /|g" "${CONFIG}"
sed -i "s|MaxMemPoolSize.*|MaxMemPoolSize=${MAX_MEM_POOLSIZE}|g" "${CONFIG}"
sed -i "s|NumberOfBuffers.*|NumberOfBuffers=${NUMBER_OF_BUFFERS}|g" "${CONFIG}"
sed -i "s|MaxDirtyBuffers.*|MaxDirtyBuffers=${MAX_DIRTY_BUFFERS}|g" "${CONFIG}"
sed -i "s|MaxCheckpointRemap.*|MaxCheckpointRemap=${MAX_CHECKPOINT_REMAP}|g" "${CONFIG}"
sed -i "s|.*MaxQueryCostEstimationTime.*|;MaxQueryCostEstimationTime = 400|g" "${CONFIG}"
sed -i "s|MaxQueryExecutionTime.*|MaxQueryExecutionTime=${TIMEOUT_S}|g" "${CONFIG}"
sed -i "s|KeepAliveTimeout.*|KeepAliveTimeout=${TIMEOUT_S}|g" "${CONFIG}"

#MaxQueryCostEstimationTime      = 400   ; in seconds
#MaxQueryExecutionTime           = 300   ; in seconds
#NumberOfBuffers          = 680000
#MaxDirtyBuffers          = 500000
