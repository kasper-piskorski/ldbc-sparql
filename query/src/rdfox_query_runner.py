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

    short_queries = [
        "",
        "interactive-short-1.sparql",
        "interactive-short-2-noPP.sparql",
        "interactive-short-3.sparql",
        "interactive-short-4.sparql",
        "interactive-short-5.sparql",
        "interactive-short-6-noPP.sparql",
        "interactive-short-7-noPP.sparql",
        "interactive-short-8.sparql",
        "interactive-short-9.sparql"
    ]

    interactive_queries = [
        "",
        "interactive-complex-1-noPP.sparql",
        "interactive-complex-2-noPP.sparql",
        "interactive-complex-3-noPP.sparql",
        "interactive-complex-4-noPP.sparql",
        "interactive-complex-5-noPP.sparql",
        "interactive-complex-6-noPP.sparql",
        "interactive-complex-7-noPP.sparql",
        "interactive-complex-8.sparql",
        "interactive-complex-9-noPP.sparql",
        "interactive-complex-10-noPP.sparql",
        "interactive-complex-11-noPP.sparql",
        "interactive-complex-12-noPP.sparql",
        "interactive-complex-13.sparql",
        "interactive-complex-14.sparql"
    ]

    def backendName(self):
        return "RDFox"

    def __init__(self, database, timeout_mins, queryDir):
        sparql_query_runner.SparqlQueryRunner.__init__(self, queryDir)
        self.database = database
        self.timeout_secs = timeout_mins * 60

    def shortyQueryImplementation(self):
        return self.short_queries

    def interactiveQueryImplementation(self):
        return self.interactive_queries

    def durationDays(self, days):
        durationDays = "xsd:duration(\"P" + days + "D\")"
        return durationDays

    def runQuery(self, query):
        #print(query)
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
        #print(response)
        output = json.loads(response.text)
        results = output.get("results").get("bindings")
        logging.info("Results: " + str(len(results))) 

        return query, results
