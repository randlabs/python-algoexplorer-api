#!/usr/bin/env python

import time
import unittest
from api import AlgoexplorerApi

client = AlgoexplorerApi('testnet')

class BlockOperations(unittest.TestCase):

    def testBlockCount(self):
        '''
        It should query block count

        '''
        result = client.blockCount()
        self.assertTrue(type(result) == int)

    def testQueryBlockByRoundNumber(self):
        '''
        It should query a block by a round number

        '''
        result = client.queryBlock(3636)
        self.assertTrue(type(result) == dict)

    def testQueryBlockByHash(self):
        '''
        It should query a block by a hash

        '''
        result = client.queryBlock('7MGM3IVHZV4GJTB2Z2Q5DWBNPGFWNJAGQJJRUNNKQ7COUAVE6SDA')
        self.assertTrue(type(result) == dict)

    def testQueryLatestBlocks(self):
        '''
        It should query lastest blocks

        '''
        result = client.queryLatestBlocks(10)
        self.assertTrue(type(result) == list)

    def testQueryBlocksFromInterval(self):
        '''
        It should query blocks between a specific rounds

        '''
        from_round = 100
        to_round = 149
        result = client.queryBlocksFromInterval(from_round, to_round)
        self.assertTrue(type(result) == list)

    def testQueryBlocksByDate(self):
        '''
        It should query a block by a date

        '''
        since = int(time.time())
        result = client.queryBlocksByDate(since)
        self.assertTrue(type(result) == list)

    def testQueryBlocksCountByDate(self):
        '''
        It should query the block count by a date

        '''
        since = int(time.time())
        result = client.queryBlocksByDate(since, count=True)
        self.assertTrue(type(result) == int)

    def testQueryBlocksFromDateInterval(self):
        '''
        It should query a block by a date interval

        '''
        interval = 100
        until = int(time.time())
        since = until - interval
        result = client.queryBlocksByDate(since, until=until)
        self.assertTrue(type(result) == list)

    def testQueryBlocksCountFromDateInterval(self):
        '''
        It should query the block count by a date interval

        '''
        interval = 100
        until = int(time.time())
        since = until - interval
        result = client.queryBlocksByDate(since, until=until, count=True)
        self.assertTrue(type(result) == int)

    def testQueryBlockTransactionsByRoundNumber(self):
        '''
        It should query transactions of a specific block by round number

        '''
        result = client.queryBlockTransactions(3636)
        self.assertTrue(type(result) == list)

    def testQueryBlockTransactionsByHash(self):
        '''
        It should query transactions of a specific block by round hash

        '''
        result = client.queryBlockTransactions('7MGM3IVHZV4GJTB2Z2Q5DWBNPGFWNJAGQJJRUNNKQ7COUAVE6SDA')
        self.assertTrue(type(result) == list)

if __name__ == '__main__':
    unittest.main()