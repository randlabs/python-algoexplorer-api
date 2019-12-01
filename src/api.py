#!/usr/bin/env python

from config import MAINNET, TESTNET, BETANET
from block import Block
from transaction import Transaction

class AlgoexplorerApi:
    def __init__(self, network_name = MAINNET):
        if network_name:
            if network_name == 'mainnet':
                self._config = MAINNET
            elif network_name == 'testnet':
                self._config = TESTNET
            elif network_name == 'betanet':
                self._config = BETANET
        
        self.block = Block(self._config)
        self.transaction = Transaction(self._config)

    def blockCount(self):
        '''
        Amount of available blocks

        :return: the amount of available blocks
        :rtype: int

        '''
        return self.block.blockCount()

    def queryBlock(self, hash_or_round):
        '''
        Block information based on the specified round or hash

        :param hash_or_round: round number or hash string to query, greater or equal than 0
        :type hash_or_round: int or str
        :return: the block information based on the specified round or hash
        :rtype: dict

        '''
        return self.block.queryBlock(hash_or_round)

    def queryBlockLatestByRound(self, count):
        '''
        Latest blocks

        :param int count: amount of blocks to return, between 1 and 100
        :return: the latest blocks
        :rtype: list

        '''
        return self.block.queryLatestByRound(count)

    def queryBlockIntervalByRound(self, from_round, to_round):
        '''
        Blocks between the specified rounds

        :param int from_round: the starting round number (inclusive), greater or equal than 0
        :param int to_round: the ending round number (inclusive), greater or equal than 1
        :return: the blocks between the specified rounds
        :rtype: list

        '''
        return self.block.queryIntervalByRound(from_round, to_round)

    def queryBlockLatestByTimestamp(self, since):
        '''
        Latest blocks since the specified timestamp

        :param int since: the earliest timestamp of the sought blocks, greater or equal than 0
        :return: the latest blocks since the specified timestamp
        :rtype: list

        '''
        return self.block.queryLatestByTimestamp(since)

    def queryBlockLatestCountByTimestamp(self, since):
        '''
        Amount of blocks since the specified timestamp

        :param int since: the earliest timestamp of the sought blocks, greater or equal than 0
        :return: the amount of blocks since the specified timestamp
        :rtype: int

        '''
        return self.block.queryLatestByTimestamp(since)

    def queryBlockIntervalByTimestamp(self, since, until):
        '''
        Blocks between the specified timestamps

        :param int since: the starting UTC timestamp (inclusive), greater or equal than 0
        :param int until: the ending UTC timestamp (inclusive), greater or equal than 1
        :return: the blocks between the specified timestamps
        :rtype: list

        '''
        return self.block.queryIntervalByTimestamp(since, until)

    def queryBlockIntervalCountByTimestamp(self, since, until):
        '''
        Amount of blocks between the specified timestamps

        :param int since: the starting UTC timestamp (inclusive), greater or equal than 0
        :param int until: the ending UTC timestamp (inclusive), greater or equal than 1
        :return: the amount of blocks between the specified timestamps
        :rtype: int

        '''
        return self.block.queryIntervalCountByTimestamp(since, until)

    def queryBlockTransactions(self, hash_or_round):
        '''
        Transactions of the specified block

        :param hash_or_round: round number or hash string to query, greater or equal than 0
        :type hash_or_round: int or str
        :return: the transactions of the specified block
        :rtype: list

        '''
        return self.block.queryBlockTransactions(hash_or_round)


    def transactionsCount(self):
        '''
        Amount of available transactions

        :return: the amount of available transactions
        :rtype: int

        '''
        return self.transaction.transactionsCount()

    def queryTransaction(self, txid_or_index):
        '''
        Transaction based on the specified index or txid

        :param txid_or_index: index number or txid string to query, greater or equal than 0
        :type txid_or_index: int or str
        :return: the transaction based on the specified index or txid
        :rtype: dict

        '''
        return self.transaction.queryTransaction(txid_or_index)

    def queryTransactionLatestByIndex(self, count):
        '''
        Latest transactions

        :param int count: amount of transactions to return, between 1 and 100
        :return: the latest transactions
        :rtype: list

        '''
        return self.transaction.queryLatestByIndex(count)

    def queryTransactionIntervalByIndex(self, from_index, to_index):
        '''
        Transactions between the specified indexes

        :param int from_index: the starting index number (inclusive), greater or equal than 0
        :param int to_index: the ending index number (inclusive), greater or equal than 1
        :return: the transactions between the specified indexes
        :rtype: list

        '''
        return self.transaction.queryIntervalByIndex(from_index, to_index)

    def queryTransactionLatestByTimestamp(self, since):
        '''
        Latest transactions since a specific timestamp.

        :param int since: the earliest timestamp of the sought transactions, greater or equal than 0
        :return: the latest transactions since a specific timestamp.
        :rtype: list

        '''
        return self.transaction.queryLatestByTimestamp(since)

    def queryTransactionLatestCountByTimestamp(self, since):
        '''
        Amount of transactions since the specified UTC timestamp

        :param int since: the earliest timestamp of the sought transactions, greater or equal than 0
        :return: the amount of transactions since the specified UTC timestamp
        :rtype: int

        '''
        return self.transaction.queryLatestByTimestamp(since)

    def queryTransactionIntervalByTimestamp(self, since, until):
        '''
        Transactions in a date range

        :param int since: the starting UTC timestamp (inclusive), greater or equal than 0
        :param int until: the ending UTC timestamp (inclusive), greater or equal than 1
        :return: the transactions in a date range
        :rtype: list

        '''
        return self.transaction.queryIntervalByTimestamp(since, until)
    
    def queryTransactionIntervalCountByTimestamp(self, since, until):
        '''
        Amount of transactions between the specified UTC timestamps

        :param int since: the starting UTC timestamp (inclusive), greater or equal than 0
        :param int until: the ending UTC timestamp (inclusive), greater or equal than 1
        :return: the amount of transactions between the specified UTC timestamps
        :rtype: int

        '''
        return self.transaction.queryIntervalCountByTimestamp(since, until)