#!/usr/bin/env python

import time
import unittest
from algoexplorersdk import AlgoexplorerApi

client = AlgoexplorerApi('testnet')

class Operations(unittest.TestCase):
    # Account Operations

    def testQueryAddress(self):
        '''
        It should query address information

        '''
        result = client.queryAddress('FFJZOPQCYSRZISSJF33MBQJGGTIB2JFUEGBJIY6GXRWEU23ONC65GUZXHM')
        self.assertTrue(type(result) == dict)
    
    def testQueryAddressLatestTransactions(self):
        '''
        It should query latest transactions of specified address

        '''
        result = client.queryAddressLatestTransactions('FFJZOPQCYSRZISSJF33MBQJGGTIB2JFUEGBJIY6GXRWEU23ONC65GUZXHM', 10)
        self.assertTrue(type(result) == list)

    def testQueryAddressTransactionsFromInterval(self):
        '''
        It should query address transactions between specified indexes

        '''
        result = client.queryAddressTransactionsFromInterval('FFJZOPQCYSRZISSJF33MBQJGGTIB2JFUEGBJIY6GXRWEU23ONC65GUZXHM', 50, 55)
        self.assertTrue(type(result) == list)

    def testQueryAddressTransactionsByDate(self):
        '''
        It should query address transacctions by a date

        '''
        since = int(time.time())
        result = client.queryAddressTransactionsByDate('FFJZOPQCYSRZISSJF33MBQJGGTIB2JFUEGBJIY6GXRWEU23ONC65GUZXHM', since)
        self.assertTrue(type(result) == list)

    def testQueryAddressTransactionsCountByDate(self):
        '''
        It should query address transacctions count by a date

        '''
        since = int(time.time())
        result = client.queryAddressTransactionsByDate('FFJZOPQCYSRZISSJF33MBQJGGTIB2JFUEGBJIY6GXRWEU23ONC65GUZXHM', since, count=True)
        self.assertTrue(type(result) == int)

    def testQueryAddressTransactionsByDateInterval(self):
        '''
        It should query address transactions by a date interval

        '''
        interval = 100
        until = int(time.time())
        since = until - interval
        result = client.queryAddressTransactionsByDate('FFJZOPQCYSRZISSJF33MBQJGGTIB2JFUEGBJIY6GXRWEU23ONC65GUZXHM', since, until)
        self.assertTrue(type(result) == list)

    def testQueryAddressTransactionsCountByDateInterval(self):
        '''
        It should query address transacctions count by a date interval

        '''
        interval = 100
        until = int(time.time())
        since = until - interval
        result = client.queryAddressTransactionsByDate('FFJZOPQCYSRZISSJF33MBQJGGTIB2JFUEGBJIY6GXRWEU23ONC65GUZXHM', since, until, True)
        self.assertTrue(type(result) == int)

    # Asset Operations

    def testQueryRelevantAssets(self):
        '''
        It should query the relevant assets of a specific account

        '''
        result = client.queryRelevantAssets('46QNIYQEMLKNOBTQC56UEBBHFNH37EWLHGT2KGL3ZGB4SW77W6V7GBKPDY')
        self.assertTrue(type(result) == list)

    # Block Operations

    def testQueryBlockCount(self):
        '''
        It should query block count

        '''
        result = client.queryBlockCount()
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

    def testQueryBlocksByDateInterval(self):
        '''
        It should query a block by a date interval

        '''
        interval = 100
        until = int(time.time())
        since = until - interval
        result = client.queryBlocksByDate(since, until)
        self.assertTrue(type(result) == list)

    def testQueryBlocksCountByDateInterval(self):
        '''
        It should query the block count by a date interval

        '''
        interval = 100
        until = int(time.time())
        since = until - interval
        result = client.queryBlocksByDate(since, until, True)
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

    # Node Operations

    def testQueryStatus(self):
        '''
        It should get the detailed statistics about the blockchain

        '''
        result = client.queryStatus()
        self.assertTrue(type(result) == dict)

    # Statistics Operations

    def testQueryStats(self):
        '''
        It should get the statistics about the blockchain

        '''
        result = client.queryStats()
        self.assertTrue(type(result) == dict)

    # Transaction Operations

    def testQueryTransactionsCount(self):
        '''
        It should query the total amount of available transactions

        '''
        result = client.queryTransactionsCount()
        self.assertTrue(type(result) == int)

    def testQueryTransactionByIndex(self):
        '''
        It should query transaction by a specified index

        '''
        result = client.queryTransaction(6363)
        self.assertTrue(type(result) == dict)

    def testQueryTransactionByHash(self):
        '''
        It should query transaction by a hash

        '''
        result = client.queryTransaction('QT577XN4UFS755QN7WHYG6WDIQM4ZN7JRT3TTYHH4N2F4S2IJRBQ')
        self.assertTrue(type(result) == dict)

    def testQueryLatestTransactions(self):
        '''
        It should query the latest transactions

        '''
        result = client.queryLatestTransactions(10)
        self.assertTrue(type(result) == list)

    def testQueryTransactionsFromInterval(self):
        '''
        It should query transactions between the specified indexes

        '''
        result = client.queryTransactionsFromInterval(999, 1009)
        self.assertTrue(type(result) == list)

    def testQueryTransactionsByDate(self):
        '''
        It should query transactions by a date

        '''
        since = int(time.time())
        result = client.queryTransactionsByDate(since)
        self.assertTrue(type(result) == list)

    def testQueryTransactionsCountByDate(self):
        '''
        It should query transactions count by a date

        '''
        since = int(time.time())
        result = client.queryTransactionsByDate(since, count=True)
        self.assertTrue(type(result) == int)

    def testQueryTransactionsByDateInterval(self):
        '''
        It should query transactions by a range of date

        '''
        interval = 100
        until = int(time.time())
        since = until - interval
        result = client.queryTransactionsByDate(since, until)
        self.assertTrue(type(result) == list)

    def testQueryTransactionsCountByDateInterval(self):
        '''
        It should query transactions count by a range of date

        '''
        interval = 100
        until = int(time.time())
        since = until - interval
        result = client.queryTransactionsByDate(since, until, True)
        self.assertTrue(type(result) == int)

if __name__ == '__main__':
    unittest.main()