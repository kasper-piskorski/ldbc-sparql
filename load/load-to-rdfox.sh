
#!/bin/bash
set -x
. ../env_vars.sh
rm load.rdfox
echo "dstore delete ${SFACTOR}" >> load.rdfox
echo "dstore create ${SFACTOR} par-complex-nn" >> load.rdfox
echo "active ${SFACTOR}" >> load.rdfox

files=( $( ls ${RDF_DATA_DIR}/*.ttl ) )

#add data
for file in "${files[@]}"
do
    echo "$file"
    echo "import $file" >> load.rdfox
done

#add rules
echo "import ! [?x, snvoc:replyOf, ?z] :- [?x, snvoc:replyOf, ?y], [?y, snvoc:replyOf, ?z] ." >> load.rdfox
echo "import ! [?x, rdfs:subClassOf, ?z] :- [?x, rdfs:subClassOf, ?y], [?y, rdfs:subClassOf, ?z] ." >> load.rdfox

echo "set endpoint.port 8080" >> load.rdfox
echo "endpoint start" >> load.rdfox
SCRIPT_HOME=" $(pwd)""/load.rdfox"
${RDFOX_HOME}RDFox sandbox exec "${SCRIPT_HOME}"
