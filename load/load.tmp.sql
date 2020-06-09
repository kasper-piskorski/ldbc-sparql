delete from DB.DBA.load_list;
SPARQL CLEAR GRAPH <http://www.ldbc.eu/SFACTOR>;
ld_dir('SRC', '*.ttl.gz', 'http://www.ldbc.eu/SFACTOR');
exit;