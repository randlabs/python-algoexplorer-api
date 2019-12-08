#!/usr/bin/env python

import time
import unittest
from api import AlgoexplorerApi

client = AlgoexplorerApi('testnet')

class StatisticsOperations(unittest.TestCase):

    def testQueryStats(self):
        '''
        It should get the statistics about the blockchain

        '''
        result = client.queryStats()
        self.assertTrue(type(result) == dict)

if __name__ == '__main__':
    unittest.main()