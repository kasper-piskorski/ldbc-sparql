import unittest
import virtuoso_query_runner
import stardog_query_runner
import seed_generator
import driver
import json

PATH_TO_SEEDS = "/Users/kasper/data/sf1/substitution_parameters/"
NO_OF_SEEDS=5
SFACTOR="sf1"
DATE_FORMAT="%Y%m%d%H%M%S000"
TIMEOUT=5

class TestInteractive(unittest.TestCase):

    def testImplementation(self):
        query_type="ic"
        virtuosoRunner=virtuoso_query_runner.VirtuosoQueryRunner("http://www.ldbc.eu/" + SFACTOR, TIMEOUT, "../queries")
        stardogRunner=stardog_query_runner.StardogQueryRunner(SFACTOR, TIMEOUT, "../queries")

        for qno in range(1, 12):
            print("Virtuoso: Interactive Complex " + str(qno))
            seeds = seed_generator.get_seeds(PATH_TO_SEEDS, NO_OF_SEEDS, query_type, qno, DATE_FORMAT)
            query_ok = False
            for seed_no in range(0, len(seeds)):
                seed = seeds[seed_no]
                print(seed)
                virtuosoResults = driver.run_query(seed, query_type, qno, virtuosoRunner)
                stardogResults = driver.run_query(seed, query_type, qno, stardogRunner)
                
                if (virtuosoResults != None and stardogResults != None):
                    #for r in virtuosoResults:
                        #print("virtuoso: " + json.dumps(r))
                    #for r in stardogResults:
                        #print("stardog: " + json.dumps(r))
                    print("v: " + str(len(virtuosoResults)) + " s: " + str(len(stardogResults)))
                    self.assertEqual(len(virtuosoResults), len(stardogResults))
                    query_ok = True
            self.assertTrue(query_ok)

if __name__ == '__main__':
    unittest.main()
