#!/usr/bin/env python

import time
import unittest
from api import AlgoexplorerApi

client = AlgoexplorerApi('testnet')

class TransactionOperations(unittest.TestCase):

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