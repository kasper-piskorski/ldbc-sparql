import logging
import sys
from argparse import ArgumentParser

import driver
import seed_generator
import stardog_query_runner
import virtuoso_query_runner

DEFAULT_MAX_NUM_SEEDS = 1
DEFAULT_QUERY_TYPE = "ic"
DEFAULT_QUERY_NUMBER = 1
DEFAULT_TIMEOUT = 30000
DEFAULT_DATABASE = "sf1"
MAX_IC = 14
MAX_BI = 25
DATE_FORMAT = "%Y%m%d%H%M%S000"
QUERY_DIR = "sparql"

if __name__ == "__main__":
    ap = ArgumentParser()
    ap.add_argument("-b", "--backend")
    ap.add_argument("-p", "--path", help="Full path to the seed directory.")
    ap.add_argument("-n", "--num", type=int, default=DEFAULT_MAX_NUM_SEEDS, help="Number of seeds to run queries.")
    ap.add_argument("-qt", "--qtype", default=DEFAULT_QUERY_TYPE)
    ap.add_argument("-qn", "--qno", type=int, default=DEFAULT_QUERY_NUMBER)
    ap.add_argument("-to", "--timeout", default=DEFAULT_TIMEOUT, help="Query timeout in mins")
    ap.add_argument("-db", "--database", default=DEFAULT_TIMEOUT)
    args = ap.parse_args()

    args = ap.parse_args()
    backend = args.backend
    timeout = int(args.timeout)
    if backend == "stardog":
        queryRunner = stardog_query_runner.StardogQueryRunner(args.database, timeout, QUERY_DIR)
    elif backend == "virtuoso":
        queryRunner = virtuoso_query_runner.VirtuosoQueryRunner("http://www.ldbc.eu/" + args.database, timeout, QUERY_DIR)

    logging.basicConfig(stream=sys.stdout, level='INFO', format="%(message)s")

    seeds = seed_generator.get_seeds(args.path, args.num, args.qtype, args.qno, DATE_FORMAT)
    driver.run_queries(seeds, args.qtype, args.qno, queryRunner)
