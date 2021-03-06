import sparql_query_runner
import stardog
import logging

conn_details = {
    'endpoint': 'http://localhost:5820',
    'username': 'admin',
    'password': 'admin'
}


class StardogQueryRunner(sparql_query_runner.SparqlQueryRunner):
    name = "stardog"
    def __init__(self, database, timeout, queryDir):
        sparql_query_runner.SparqlQueryRunner.__init__(self, queryDir)
        self.database = database
        self.timeout = timeout

    def durationDays(self, days):
        durationDays = "\"P" + days + "D\"^^xsd:duration"
        return durationDays

    def runQuery(self, query):
        results = {}
        if self.timeout == 0:
            return query, results
        try:
            with stardog.Connection(self.database, **conn_details) as conn:
                output = conn.select(query)          
                results = output.get("results").get("bindings")
                logging.info("Results: " + str(len(results)))
        except Exception as inst:
            logging.error(inst)
        return query, results
