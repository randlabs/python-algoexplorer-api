#!/usr/bin/env python

import time
from typing import Union, Optional
from algoexplorersdk.network.request import fetchGet

class Block:
	'''
    The Block Model
	
	Args:
		config: a dictionary containing the api configuration (url, genesis, id)
	
    '''
	def __init__(self, config: dict):
		'''
		Create a new Block with the provided attributes

        '''
		self.config = config
	
	def queryBlockCount(self) -> int:
		'''
		Returns:
			the amount of available blocks

        '''
		response = fetchGet(self.config['url'] + '/block/count')
		response_json = response.json()
		return response_json['blockCount']

	def queryBlock(self, value: Union[int, str]) -> dict:
		'''
		Args:
			value: a block number or block hash
		
		Returns:
			the block information based on the specified round or hash

        '''
		if (type(value) != int and type(value) != str) or (type(value) == int and value < 0):
			raise Exception('Invalid argument, VALUE must be a positive integer or a string hash')
		response = fetchGet(self.config['url'] + '/block/' + str(value))
		return response.json()

	def queryLatestBlocks(self, count: int) -> list:
		'''
		Args:
			count: amount of blocks to return (between 1 and 100)

		Returns:
			the latest blocks

        '''
		if type(count) != int or count < 1 or count > 100:
			raise Exception('Invalid argument, COUNT must be a positive integer between 1 and 100')
		response = fetchGet(self.config['url'] + '/block/latest/' + str(count))
		return response.json()

	def queryBlocksFromInterval(self, from_round: int, to_round: int) -> list:
		'''
		Args:
			from_round: the starting round number (inclusive)
			to_round: the ending round number (inclusive)
		
		Returns:
			the blocks between the specified rounds

        '''
		if type(from_round) != int or type(to_round) != int or to_round - from_round < 1 or from_round < 0 or to_round < 1:
			raise Exception('Invalid arguments, FROM_ROUND and TO_ROUND must be a positive integers, and TO_ROUND must be greater than FROM_ROUND')
		if to_round - from_round > 99:
			raise Exception('Max blocks to query is 100')
		response = fetchGet(self.config['url'] + '/block/from/' + str(from_round) + '/to/' + str(to_round))
		return response.json()

	def queryBlocksByDate(self, since: int, until: Optional[int] = None, count: Optional[bool] = False) -> Union[int, list]:
		'''
		Args:
			since: the starting UTC timestamp (inclusive)
			until: the ending UTC timestamp (inclusive)
			count: if its true, will return the amount of blocks, else, will return an array of blocks
		
		Returns:
			the amount of blocks or a blocks list since the specified interval of time

        '''
		date = time.time() + 60
		if type(since) != int or (until != None and type(until) != int):
			raise Exception('Invalid arguments, the date must be a positive integer')
		if since < 1546300800 or since > date or (until != None and until - since < 1):
			raise Exception('Invalid date')
		if until != None and (until < since or until > date):
			raise Exception('Invalid arguments, UNTIL must be greater than SINCE')
		if type(count) != bool:
			raise Exception('Invalid arguments, COUNT must be a boolean')
		if until != None and until - since > 172800:
			raise Exception('Invalid arguments. Timestamp distance cannot exceed 172800 seconds')
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
		Args:
			value: round number or hash string to query
		
		Returns:
			the transactions of the specified block

        '''
		if (type(value) != int and type(value) != str) or (type(value) == int and value < 0):
			raise Exception('Invalid argument, VALUE must be a positive integer or a string hash')
		response = fetchGet(self.config['url'] + '/block/' + str(value) + '/transactions')
		return response.json()
