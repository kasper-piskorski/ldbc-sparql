import json
import logging
import os
import socket
import urllib.parse
import urllib.request
from string import Template
from urllib.error import HTTPError, URLError

import sparql_query_runner


class VirtuosoQueryRunner(sparql_query_runner.SparqlQueryRunner):
    name = "virtuoso"
    def __init__(self, database, timeout_mins, queryDir):
        sparql_query_runner.SparqlQueryRunner.__init__(self, queryDir)
        self.database = database
        self.timeout_secs = timeout_mins * 60

    def durationDays(self, days):
        durationDays = "xsd:duration(\"P" + days + "D\")"
        return durationDays

    def runQuery(self, query):
        results = {}
        if self.timeout == 0:
            return query, results
            
        params = {
            "default-graph-uri": self.database,
            "query": query,
            "timeout": 0,
            "format": "application/json",
        }
        baseURL = "http://localhost:8890/sparql/"
        data = urllib.parse.urlencode(params).encode("utf-8")
        req = urllib.request.Request(baseURL)
        try:
            with urllib.request.urlopen(req, data=data, timeout=self.timeout_secs) as f:
                response = f.read()
                output = json.loads(response)
                results = output.get("results").get("bindings")
                logging.info("Results: " + str(len(results)))
    
        except HTTPError as error:
            logging.error('Data not retrieved because %s', error)
        except URLError as error:
            if isinstance(error.reason, socket.timeout):
                logging.error('socket timed out - URL')
            else:
                logging.error("Error encountered during query request %s", error)
        return query, results


if __name__ == "__main__":
    graph = "http://www.ldbc.eu"

    query = "SELECT DISTINCT (count(*) as ?count) WHERE {?s ?p ?o}"

    runner = VirtuosoQueryRunner(graph, 1, "queries")
    runner.runQuery(query)
