#!/usr/bin/env python

import time
from typing import Union, Optional
from request import fetchGet

class Block:
	def __init__(self, config):
		self.config = config
	
	def blockCount(self) -> int:
		'''
        :return: the amount of available blocks
        :rtype: int

        '''
		response = fetchGet(self.config['url'] + '/block/count')
		response_json = response.json()
		return response_json['blockCount']

	def queryBlock(self, value: Union[int, str]) -> dict:
		'''
        :param value: a block number or block hash
        :return: the block information based on the specified round or hash
        :rtype: dict

        '''
		if (type(value) != int and type(value) != str) or (type(value) == int and value < 0):
			raise Exception('Invalid argument, value must be a positive integer or a string hash')
		response = fetchGet(self.config['url'] + '/block/' + str(value))
		return response.json()

	def queryLatestBlocks(self, count: int) -> list:
		'''
        :param count: amount of blocks to return. Limited to values between 1 and 100
        :return: the latest blocks
        :rtype: list

        '''
		if type(count) != int or count < 1 or count > 100:
			raise Exception('Invalid argument, count must be a positive integer between 1 and 100')
		response = fetchGet(self.config['url'] + '/block/latest/' + str(count))
		return response.json()

	def queryBlocksFromInterval(self, from_round: int, to_round: int) -> list:
		'''
        :param from_round: the starting round number (inclusive)
        :param to_round: the ending round number (inclusive)
        :return: the blocks between the specified rounds
        :rtype: list

        '''
		if type(from_round) != int or type(to_round) != int or to_round - from_round < 1 or from_round < 0 or to_round < 1:
			raise Exception('Invalid arguments, from_round and to_round must be a positive integers, and to_round must be greater than from_round')
		if to_round - from_round > 99:
			raise Exception('Max blocks to query is 100')
		response = fetchGet(self.config['url'] + '/block/from/' + str(from_round) + '/to/' + str(to_round))
		return response.json()

	def queryBlocksByDate(self, since: int, until: Optional[int] = None, count: Optional[bool] = False) -> Union[int, list]:
		'''
        :param since: the starting UTC timestamp (inclusive)
		:param until: the ending UTC timestamp (inclusive)
		:param count: if its true, will return the amount of blocks, else, will return an array of blocks
        :return: the amount of blocks or a blocks list since the specified interval of time
        :rtype: Union[int, list]

        '''
		date = time.time() + 60
		if type(since) != int or (until != None and type(until) != int):
			raise Exception('Invalid arguments, the date must be a positive integer')
		if since < 1546300800 or since > date or (until != None and (until - since < 1 or until - since > 172799)):
			raise Exception('Invalid date')
		if until != None and (until < since or until > date):
			raise Exception('Invalid arguments, until must be greater than since')
		if type(count) != bool:
			raise Exception('Invalid arguments, COUNT must be a boolean')
		url = self.config['url'] + '/block/since/' + str(since)
		if count:
			if until != None:
				response = fetchGet(url + '/until/' + str(until) + '/count')
			else:
				response = fetchGet(url + '/count')
			response_json = response.json()
			return response_json['blockCount']
		elif until != None:
			response = fetchGet(url + '/until/' + str(until))
		else:
			response = fetchGet(url)
		return response.json()

	def queryBlockTransactions(self, value: Union[int, str]) -> list:
		'''
        :param value: round number or hash string to query
        :return: the transactions of the specified block
        :rtype: list

        '''
		if (type(value) != int and type(value) != str) or (type(value) == int and value < 0):
			raise Exception('Invalid argument, value must be a positive integer or a string hash')
		response = fetchGet(self.config['url'] + '/block/' + str(value) + '/transactions')
		return response.json()
