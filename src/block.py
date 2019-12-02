#!/usr/bin/env python

from request import fetchGet

class Block:
	def __init__(self, config):
		self.config = config
	
	def blockCount(self):
		'''
        Amount of available blocks

        :return: the amount of available blocks
        :rtype: int

        '''
		response = fetchGet(self.config['url'] + '/block/count')
		response_json = response.json()
		return response_json['blockCount']

	def queryBlock(self, hash_or_round):
		'''
        Block information based on the specified round or hash

        :param hash_or_round: round number or hash string to query, greater or equal than 0
        :type hash_or_round: int or str
        :return: the block information based on the specified round or hash
        :rtype: dict

        '''
		if (type(hash_or_round) != int and type(hash_or_round) != str) or (type(hash_or_round) == int and hash_or_round < 0):
			return False
		response = fetchGet(self.config['url'] + '/block/' + str(hash_or_round))
		return response.json()

	def queryBlockLatestByRound(self, count):
		'''
        Latest blocks

        :param count: amount of blocks to return, between 1 and 100
		:type count: int
        :return: the latest blocks
        :rtype: list

        '''
		if type(count) != int or count < 1 or count > 100:
			return False
		response = fetchGet(self.config['url'] + '/block/latest/' + str(count))
		return response.json()

	def queryBlockIntervalByRound(self, from_round, to_round):
		'''
        Blocks between the specified rounds

        :param int from_round: the starting round number (inclusive), greater or equal than 0
        :param int to_round: the ending round number (inclusive), greater or equal than 1
        :return: the blocks between the specified rounds
        :rtype: list

        '''
		if type(from_round) != int or type(to_round) != int or to_round - from_round < 1 or from_round < 0 or to_round < 1:
			return False
		if to_round - from_round > 99:
			return False
		response = fetchGet(self.config['url'] + '/block/from/' + str(from_round) + '/to/' + str(to_round))
		return response.json()

	def queryBlockLatestByTimestamp(self, since):
		'''
        Latest blocks since the specified timestamp

        :param int since: the earliest timestamp of the sought blocks, greater or equal than 0
        :return: the latest blocks since the specified timestamp
        :rtype: list

        '''
		if type(since) != int or since < 0:
			return False
		response = fetchGet(self.config['url'] + '/block/since/' + str(since))
		return response.json()

	def queryBlockLatestCountByTimestamp(self, since):
		'''
        Amount of blocks since the specified timestamp

        :param int since: the earliest timestamp of the sought blocks, greater or equal than 0
        :return: the amount of blocks since the specified timestamp
        :rtype: int

        '''
		if type(since) != int or since < 0:
			return False
		response = fetchGet(self.config['url'] + '/block/since/' + str(since) + '/count')
		response_json = response.json()
		return response_json['blockCount']

	def queryBlockIntervalByTimestamp(self, since, until):
		'''
        Blocks between the specified timestamps

        :param int since: the starting UTC timestamp (inclusive), greater or equal than 0
        :param int until: the ending UTC timestamp (inclusive), greater or equal than 1
        :return: the blocks between the specified timestamps
        :rtype: list

        '''
		if type(since) != int or type(until) != int or until - since < 1 or until - since > 172799 or since < 0 or until < 1:
			return False
		response = fetchGet(self.config['url'] + '/block/since/' + str(since) + '/until/' + str(until))
		return response.json()

	def queryBlockIntervalCountByTimestamp(self, since, until):
		'''
        Amount of blocks between the specified timestamps

        :param int since: the starting UTC timestamp (inclusive), greater or equal than 0
        :param int until: the ending UTC timestamp (inclusive), greater or equal than 1
        :return: the amount of blocks between the specified timestamps
        :rtype: int

        '''
		if type(since) != int or type(until) != int or until - since < 1 or until - since > 172799 or since < 0 or until < 1:
			return False
		response = fetchGet(self.config['url'] + '/block/since/' + str(since) + '/until/' + str(until) + '/count')
		response_json = response.json()
		return response_json['blockCount']

	def queryBlockTransactions(self, hash_or_round):
		'''
        Transactions of the specified block

        :param hash_or_round: round number or hash string to query, greater or equal than 0
        :type hash_or_round: int or str
        :return: the transactions of the specified block
        :rtype: list

        '''
		if (type(hash_or_round) != int and type(hash_or_round) != str) or (type(hash_or_round) == int and hash_or_round < 0):
			return False
		response = fetchGet(self.config['url'] + '/block/' + str(hash_or_round) + '/transactions')
		return response.json()
