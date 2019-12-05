import unittest
from api import AlgoexplorerApi

client = AlgoexplorerApi('testnet')

class TestBlock(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()