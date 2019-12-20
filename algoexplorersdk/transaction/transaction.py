#!/usr/bin/env python

import time
from typing import Union, Optional
from algoexplorersdk.network.request import fetchGet

class Transaction:
	'''
    The Transaction Model
	
	Args:
		config: a dictionary containing the api configuration (url, genesis, id)
	
    '''
	def __init__(self, config: dict):
		'''
		Create a new Transaction with the provided attributes

        '''
		self.config = config
	
	def queryTransactionsCount(self) -> int:
		'''
		Returns:
			the amount of available transactions

        '''
		response = fetchGet(self.config['url'] + '/transaction/count')
		response_json = response.json()
		return response_json['txCount']
		
	def queryTransaction(self, value: Union[int, str]) -> dict:
		'''
		Args:
			value: index number or txid string to query
		
		Returns:
			the transaction based on the specified index or txid

        '''
		if (type(value) != str and type(value) != int) or (type(value) == int and value < 0):
			raise Exception('Invalid argument, VALUE must be a positive integer or a string hash')
		response = fetchGet(self.config['url'] + '/transaction/' + str(value))
		return response.json()

	def queryLatestTransactions(self, count: int) -> list:
		'''
		Args:
			count: amount of transactions to return (between 1 and 100)
		
		Returns:
			the latest transactions
        '''
		if type(count) != int or count < 1 or count > 100:
			raise Exception('Invalid argument, COUNT must be a positive integer between 1 and 100')
		response = fetchGet(self.config['url'] + '/transaction/latest/' + str(count))
		return response.json()

	def queryTransactionsFromInterval(self, from_index: int, to_index: int) -> list:
		'''
		Args:
			from_index: the starting index number (inclusive)
			to_index: the ending index number (inclusive)

		Returns:
			the transactions between the specified indexes

        '''
		if type(from_index) != int or type(to_index) != int or to_index - from_index < 1 or from_index < 0 or to_index < 1:
			raise Exception('Invalid arguments, FROM_INDEX and TO_INDEX must be a positive integers, and TO_INDEX must be greater than FROM_INDEX')
		if to_index - from_index > 99:
			raise Exception('Max transactions to query is 100')
		response = fetchGet(self.config['url'] + '/transaction/from/' + str(from_index) + '/to/' + str(to_index))
		return response.json()

	def queryTransactionsByDate(self, since: int, until: Optional[int] = None, count: Optional[bool] = False) -> Union[int, list]:
		'''
		Args:
			since: the starting UTC timestamp (inclusive)
			until: the ending UTC timestamp (inclusive)
			count: if its true, will return the amount of transactions, else, will return an array of transactions
		
		Returns:
			the amount of transactions or a transactions array between the specified UTC timestamps

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
		url = self.config['url'] + '/transaction/since/' + str(since)
		if count:
			if until != None:
				response = fetchGet(url + '/until/' + str(until) + '/count')
			else:
				response = fetchGet(url + '/count')
			response_json = response.json()
			return response_json['txCount']
		elif until != None:
			response = fetchGet(url + '/until/' + str(until))
		else:
			response = fetchGet(url)
		return response.json()
