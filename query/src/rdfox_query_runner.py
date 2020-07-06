import json
import logging
import os
import socket
import urllib.parse
import urllib.request
from string import Template
from urllib.error import HTTPError, URLError

import sparql_query_runner
import requests


class RDFoxQueryRunner(sparql_query_runner.SparqlQueryRunner):
    name = "rdfox"
    def __init__(self, database, timeout_mins, queryDir):
        sparql_query_runner.SparqlQueryRunner.__init__(self, queryDir)
        self.database = database
        self.timeout_secs = timeout_mins * 60

    def durationDays(self, days):
        durationDays = "xsd:duration(\"P" + days + "D\")"
        return durationDays

    def runQuery(self, query):
        results = {}
        if self.timeout_secs == 0:
            return query, results

        rdfox_server = "http://localhost:8080"
        baseURL = rdfox_server + "/datastores/" + self.database + "/sparql"

        params = {
            "query": query,
            "format": "application/json",
        }
        response = requests.get(baseURL, 
            params, 
            headers={"Accept": "application/sparql-results+json"},
            timeout = self.timeout_secs)
        print(response.text)
        output = json.loads(response.text)
        results = output.get("results").get("bindings")
        logging.info("Results: " + str(len(results))) 

        return query, results
