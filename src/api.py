#!/usr/bin/env python

from config import MAINNET, TESTNET, BETANET
from block import Block

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

    def blockCount(self):
        '''
        The amount of available blocks.

        :return: the amount of available blocks.
        :rtype: int

        '''
        return self.block.blockCount()

    def queryBlock(self, hash_or_round):
        '''
        Block information based on the specified round or hash.

        :param hash_or_round: Round number or hash string to query, greater or equal than 0
        :type hash_or_round: int or str
        :return: the block information based on the specified round or hash.
        :rtype: dict

        '''
        return self.block.queryBlock(hash_or_round)

    def queryLatestByRound(self, count):
        '''
        The latest blocks.

        :param int count: Amount of blocks to return, between 1 and 100.
        :return: the latest blocks.
        :rtype: list

        '''
        return self.block.queryLatestByRound(count)

    def queryIntervalByRound(self, from_round, to_round):
        '''
        The blocks between the specified rounds.

        :param int from_round: the starting round number (inclusive), greater or equal than 0
        :param int to_round: the ending round number (inclusive), greater or equal than 1
        :return: the blocks between the specified rounds.
        :rtype: list

        '''
        return self.block.queryIntervalByRound(from_round, to_round)

    def queryLatestByTimestamp(self, since):
        '''
        The latest blocks since the specified timestamp.

        :param int since: the earliest timestamp of the sought blocks, greater or equal than 0
        :return: the latest blocks since the specified timestamp.
        :rtype: list

        '''
        return self.block.queryLatestByTimestamp(since)

    def queryLatestCountByTimestamp(self, since):
        '''
        The amount of blocks since the specified timestamp.

        :param int since: the earliest timestamp of the sought blocks, greater or equal than 0
        :return: the amount of blocks since the specified timestamp.
        :rtype: int

        '''
        return self.block.queryLatestByTimestamp(since)

    def queryIntervalByTimestamp(self, since, until):
        '''
        The blocks between the specified timestamps.

        :param int since: the starting UTC timestamp (inclusive), greater or equal than 0
        :param int until: the ending UTC timestamp (inclusive), greater or equal than 1
        :return: the blocks between the specified timestamps.
        :rtype: list

        '''
        return self.block.queryIntervalByTimestamp(since, until)

    def queryIntervalCountByTimestamp(self, since, until):
        '''
        The amount of blocks between the specified timestamps.

        :param int since: the starting UTC timestamp (inclusive), greater or equal than 0
        :param int until: the ending UTC timestamp (inclusive), greater or equal than 1
        :return: the amount of blocks between the specified timestamps.
        :rtype: int

        '''
        return self.block.queryIntervalCountByTimestamp(since, until)

    def queryBlockTransactions(self, hash_or_round):
        '''
        The transactions of the specified block.

        :param hash_or_round: Round number or hash string to query, greater or equal than 0
        :type hash_or_round: int or str
        :return: the transactions of the specified block.
        :rtype: list

        '''
        return self.block.queryBlockTransactions(hash_or_round)