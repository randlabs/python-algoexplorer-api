#!/usr/bin/env python

import time
import unittest
from api import AlgoexplorerApi

client = AlgoexplorerApi('testnet')

class AccountOperations(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()