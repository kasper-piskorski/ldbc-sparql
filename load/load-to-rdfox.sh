
#!/bin/bash
set -x
. ../env_vars.sh
rm load.rdfox
echo "dstore delete ${SFACTOR}" >> load.rdfox
echo "dstore create ${SFACTOR} par-complex-nn" >> load.rdfox
echo "active ${SFACTOR}" >> load.rdfox

files=( $( ls ${RDF_DATA_DIR}/*.ttl ) )

for file in "${files[@]}"
do
    echo "$file"
    echo "import $file" >> load.rdfox
done

echo "set endpoint.port 8080" >> load.rdfox
echo "endpoint start" >> load.rdfox
SCRIPT_HOME=" $(pwd)""/load.rdfox"
${RDFOX_HOME}RDFox sandbox exec "${SCRIPT_HOME}"
#curl -i -X POST localhost:8080/datastores/family/sparql -d "query=PREFIX : <https://oxfordsemantic.tech/RDFox/getting-started/>  SELECT ?p ?n WHERE { ?p a :Person . ?p :forename ?n }"