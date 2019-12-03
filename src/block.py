#!/usr/bin/env python

from request import fetchGet

class Block:
	def __init__(self, config):
		self.config = config
	
	def blockCount(self):
		'''
        :return: the amount of available blocks
        :rtype: int

        '''
		response = fetchGet(self.config['url'] + '/block/count')
		response_json = response.json()
		return response_json['blockCount']

	def queryBlock(self, value):
		'''
        :param value: a block number or block hash
        :type value: int/str
        :return: the block information based on the specified round or hash
        :rtype: dict

        '''
		if (type(value) != int and type(value) != str) or (type(value) == int and value < 0):
			raise Exception('Invalid argument, value must be a positive integer or a string hash')
		response = fetchGet(self.config['url'] + '/block/' + str(value))
		return response.json()

	def queryLatestBlocks(self, count):
		'''
        :param count: amount of blocks to return. Limited to values between 1 and 100
		:type count: int
        :return: the latest blocks
        :rtype: list

        '''
		if type(count) != int or count < 1 or count > 100:
			raise Exception('Invalid argument, count must be a positive integer between 1 and 100')
		response = fetchGet(self.config['url'] + '/block/latest/' + str(count))
		return response.json()

	def queryBlocksFromInterval(self, from_round, to_round):
		'''
        :param int from_round: the starting round number (inclusive)
        :param int to_round: the ending round number (inclusive)
        :return: the blocks between the specified rounds
        :rtype: list

        '''
		if type(from_round) != int or type(to_round) != int or to_round - from_round < 1 or from_round < 0 or to_round < 1:
			raise Exception('Invalid arguments, from_round and to_round must be a positive integers, and to_round must be greater than from_round')
		if to_round - from_round > 99:
			raise Exception('Max blocks to query is 100')
		response = fetchGet(self.config['url'] + '/block/from/' + str(from_round) + '/to/' + str(to_round))
		return response.json()

	def queryBlockLatestByTimestamp(self, since):
		'''
        :param int since: the earliest timestamp of the sought blocks
        :return: the latest blocks since the specified timestamp
        :rtype: list

        '''
		if type(since) != int or since < 0:
			return False
		response = fetchGet(self.config['url'] + '/block/since/' + str(since))
		return response.json()

	def queryBlockLatestCountByTimestamp(self, since):
		'''
        :param int since: the earliest timestamp of the sought blocks
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
        :param int since: the starting UTC timestamp (inclusive)
        :param int until: the ending UTC timestamp (inclusive)
        :return: the blocks between the specified timestamps
        :rtype: list

        '''
		if type(since) != int or type(until) != int or until - since < 1 or until - since > 172799 or since < 0 or until < 1:
			return False
		response = fetchGet(self.config['url'] + '/block/since/' + str(since) + '/until/' + str(until))
		return response.json()

	def queryBlockIntervalCountByTimestamp(self, since, until):
		'''
        :param int since: the starting UTC timestamp (inclusive)
        :param int until: the ending UTC timestamp (inclusive)
        :return: the amount of blocks between the specified timestamps
        :rtype: int

        '''
		if type(since) != int or type(until) != int or until - since < 1 or until - since > 172799 or since < 0 or until < 1:
			return False
		response = fetchGet(self.config['url'] + '/block/since/' + str(since) + '/until/' + str(until) + '/count')
		response_json = response.json()
		return response_json['blockCount']

	def queryBlockTransactions(self, value):
		'''
        :param value: round number or hash string to query
        :type value: int or str
        :return: the transactions of the specified block
        :rtype: list

        '''
		if (type(value) != int and type(value) != str) or (type(value) == int and value < 0):
			raise Exception('Invalid argument, value must be a positive integer or a string hash')
		response = fetchGet(self.config['url'] + '/block/' + str(value) + '/transactions')
		return response.json()
