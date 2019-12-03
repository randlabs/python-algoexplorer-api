#!/usr/bin/env python

from request import fetchGet

class Transaction:
	def __init__(self, config):
		self.config = config
	
	def transactionsCount(self):
		'''
        :return: the amount of available transactions
        :rtype: int

        '''
		response = fetchGet(self.config['url'] + '/transaction/count')
		response_json = response.json()
		return response_json['txCount']
		
	def queryTransaction(self, value):
		'''
        :param value: index number or txid string to query
        :type value: int/str
        :return: the transaction based on the specified index or txid
        :rtype: dict

        '''
		if (type(value) != str and type(value) != int) or (type(value) == int and value < 0):
			raise Exception('Invalid argument, transaction id must be a positive integer or a string hash')
		response = fetchGet(self.config['url'] + '/transaction/' + str(value))
		return response.json()

	def queryLatestTransactions(self, count):
		'''
        :param int count: amount of transactions to return. Limited to values between 1 and 100
        :return: the latest transactions
        :rtype: list

        '''
		if type(count) != int or count < 1 or count > 100:
			raise Exception('Invalid argument, COUNT must be a positive integer between 1 and 100')
		response = fetchGet(self.config['url'] + '/transaction/latest/' + str(count))
		return response.json()

	def queryTransactionsFromInterval(self, from_index, to_index):
		'''
        :param int from_index: the starting index number (inclusive)
        :param int to_index: the ending index number (inclusive)
        :return: the transactions between the specified indexes
        :rtype: list

        '''
		if type(from_index) != int or type(to_index) != int or to_index - from_index < 1 or from_index < 0 or to_index < 1:
			raise Exception('Invalid arguments, from_index and to_index must be a positive integers, and to_index must be greater than from_index')
		if to_index - from_index > 99:
			raise Exception('Max transactions to query is 100')
		response = fetchGet(self.config['url'] + '/transaction/from/' + str(from_index) + '/to/' + str(to_index))
		return response.json()

	def queryTransactionLatestByTimestamp(self, since):
		'''
        :param int since: the earliest timestamp of the sought transactions
        :return: the latest transactions since a specific timestamp.
        :rtype: list

        '''
		if type(since) != int or since < 0:
			return False
		response = fetchGet(self.config['url'] + '/transaction/since/' + str(since))
		return response.json()

	def queryTransactionLatestCountByTimestamp(self, since):
		'''
        :param int since: the earliest timestamp of the sought transactions
        :return: the amount of transactions since the specified UTC timestamp
        :rtype: int

        '''
		if type(since) != int or since < 0:
			return False
		response = fetchGet(self.config['url'] + '/transaction/since/' + str(since) + '/count')
		response_json = response.json()
		return response_json['txCount']

	def queryTransactionIntervalByTimestamp(self, since, until):
		'''
        :param int since: the starting UTC timestamp (inclusive)
        :param int until: the ending UTC timestamp (inclusive)
        :return: the transactions in a date range
        :rtype: list

        '''
		if type(since) != int or since < 0 or type(until) != int or until < 1 or until - since < 1:
			return False
		response = fetchGet(self.config['url'] + '/transaction/since/' + str(since) + '/until/' + str(until))
		return response.json()

	def queryTransactionIntervalCountByTimestamp(self, since, until):
		'''
        :param int since: the starting UTC timestamp (inclusive)
        :param int until: the ending UTC timestamp (inclusive)
        :return: the amount of transactions between the specified UTC timestamps
        :rtype: int

        '''
		if type(since) != int or since < 0 or type(until) != int or until < 1 or until - since < 1:
			return False
		response = fetchGet(self.config['url'] + '/transaction/since/' + str(since) + '/until/' + str(until) + '/count')
		response_json = response.json()
		return response_json['txCount']
