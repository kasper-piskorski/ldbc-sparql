import unittest

import driver
import seed_generator
import stardog_query_runner
import virtuoso_query_runner
import sys, logging

SFACTOR = "sf1"
PATH_TO_SEEDS = "/Users/kasper/data/" + SFACTOR + "-ttl/substitution_parameters/"
DATE_FORMAT = "%Y%m%d%H%M%S000"
TIMEOUT = 5
QUERY_DIR = "../sparql"

class TestInteractive(unittest.TestCase):

    def testInteractiveShortStardog(self):
        query_type = "is"
        no_of_seeds = 1
        stardogRunner = stardog_query_runner.StardogQueryRunner(SFACTOR, TIMEOUT, QUERY_DIR)

        logging.basicConfig(stream=sys.stdout, level='INFO', format="%(message)s")

        for qno in range(1, 7):
            print("Interactive Short " + str(qno))
            seeds = seed_generator.get_seeds(PATH_TO_SEEDS, no_of_seeds, query_type, qno, DATE_FORMAT)
            query_ok = True
            for seed_no in range(0, len(seeds)):
                seed = seeds[seed_no]
                print(seed)
                stardogResults = driver.run_query(seed, query_type, qno, stardogRunner)
                if stardogResults == None or len(stardogResults) == 0:
                    query_ok = False
            self.assertTrue(query_ok)

    def testInteractiveShortVirtuoso(self):
        query_type = "is"
        no_of_seeds = 1
        virtuosoRunner = virtuoso_query_runner.VirtuosoQueryRunner("http://www.ldbc.eu/" + SFACTOR, TIMEOUT, QUERY_DIR)

        logging.basicConfig(stream=sys.stdout, level='INFO', format="%(message)s")

        for qno in range(1, 7):
            print("Interactive Short " + str(qno))
            seeds = seed_generator.get_seeds(PATH_TO_SEEDS, no_of_seeds, query_type, qno, DATE_FORMAT)
            query_ok = True
            for seed_no in range(0, len(seeds)):
                seed = seeds[seed_no]
                print(seed)
                virtuosoResults = driver.run_query(seed, query_type, qno, virtuosoRunner)
                if virtuosoResults == None or len(virtuosoResults) == 0:
                    query_ok = False
            self.assertTrue(query_ok)

    @unittest.skip
    def testInteractiveCrossImplementation(self):
        query_type = "ic"
        no_of_seeds = 5
        virtuosoRunner = virtuoso_query_runner.VirtuosoQueryRunner("http://www.ldbc.eu/" + SFACTOR, TIMEOUT, QUERY_DIR)
        stardogRunner = stardog_query_runner.StardogQueryRunner(SFACTOR, TIMEOUT, QUERY_DIR)

        for qno in range(1, 13):
            print("Interactive Complex " + str(qno))
            seeds = seed_generator.get_seeds(PATH_TO_SEEDS, no_of_seeds, query_type, qno, DATE_FORMAT)
            query_ok = False
            for seed_no in range(0, len(seeds)):
                seed = seeds[seed_no]
                print(seed)
                virtuosoResults = driver.run_query(seed, query_type, qno, virtuosoRunner)
                stardogResults = driver.run_query(seed, query_type, qno, stardogRunner)

                if virtuosoResults != None and stardogResults != None:
                    # for r in virtuosoResults:
                    # print("virtuoso: " + json.dumps(r))
                    # for r in stardogResults:
                    # print("stardog: " + json.dumps(r))
                    print("v: " + str(len(virtuosoResults)) + " s: " + str(len(stardogResults)))
                    self.assertEqual(len(virtuosoResults), len(stardogResults))
                    query_ok = True
            self.assertTrue(query_ok)


if __name__ == '__main__':
    unittest.main()
