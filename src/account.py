#!/usr/bin/env python

import time
from algosdk import encoding
from typing import Union, Optional
from request import fetchGet

class Account:
	'''
    The Account Model
	
	Args:
		config: a dictionary containing the api configuration (url, genesis, id)
	
    '''
	def __init__(self, config: dict):
		'''
		Create a new Account with the provided attributes

        '''
		self.config = config
		
	def queryAddress(self, address: str) -> dict:
		'''
		Args:
			address: address of the account to query

		Returns:
			information about the specified address

        '''
		if (not encoding.is_valid_address(address)):
			raise Exception('Invalid address')
		response = fetchGet(self.config['url'] + '/account/' + address)
		return response.json()
		
	def queryAddressLatestTransactions(self, address: str, count: int) -> list:
		'''
		Args:
			address: address of the account to query
			count: amount of transactions to return (between 1 and 100)
		
		Returns:
			the latest transactions of the specified account
			
        '''
		if not encoding.is_valid_address(address):
			raise Exception('Invalid address')
		if type(count) != int or count < 1:
			raise Exception('Invalid argument, COUNT must be a positive integer')
		response = fetchGet(self.config['url'] + '/account/' + address + '/transactions/latest/' + str(count))
		return response.json()

	def queryAddressTransactionsFromInterval(self, address: str, from_round: int, to_round: int):
		'''
		Args:
			address: address of the account to query
			from_round: the starting index number (inclusive)
			to_round: the ending index number (inclusive)

		Returns:
			the transactions between the specified indexes of the specified account

        '''
		if not encoding.is_valid_address(address):
			raise Exception('Invalid address')
		if type(from_round) != int or type(to_round) != int or (to_round - from_round < 1) or from_round < 0 or to_round < 1:
			raise Exception('Invalid arguments, FROM_ROUND and TO_ROUND must be a positive integers, and TO_ROUND must be greater than FROM_ROUND')
		if to_round - from_round > 99:
			raise Exception('Max blocks to query is 100')
		response = fetchGet(self.config['url'] + '/account/' + address + '/transactions/from/' + str(from_round) + '/to/' + str(to_round))
		return response.json()

	def queryAddressTransactionsByDate(self, address: str, since: int, until: Optional[int] = None, count: Optional[bool] = False) -> Union[int, list]:
		'''
		Args:
			address: address of the account to query
			since: the starting UTC timestamp (inclusive)
			until: the ending UTC timestamp (inclusive)

		Returns:
			if its true, will return the amount of transactions, else, will return an array of transactions

        '''
		if not encoding.is_valid_address(address):
			raise Exception('Invalid address')
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
		url = self.config['url'] + '/account/' + address + '/transactions/since/' + str(since)
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
