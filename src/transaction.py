#!/usr/bin/env python

from request import fetchGet

class Transaction:
	def __init__(self, config):
		self.config = config
	
	def transactionsCount(self):
		'''
        Amount of available transactions

        :return: the amount of available transactions
        :rtype: int

        '''
		response = fetchGet(self.config['url'] + '/transaction/count')
		response_json = response.json()
		return response_json['txCount']
		
	def queryTransaction(self, txid_or_index):
		'''
        Transaction based on the specified index or txid

        :param txid_or_index: index number or txid string to query, greater or equal than 0
        :type txid_or_index: int or str
        :return: the transaction based on the specified index or txid
        :rtype: dict

        '''
		if (type(txid_or_index) != str and type(txid_or_index) != int) or txid_or_index < 0:
			return False
		response = fetchGet(self.config['url'] + '/transaction/' + str(txid_or_index))
		return response.json()

	def queryTransactionLatestByIndex(self, count):
		'''
        Latest transactions

        :param int count: amount of transactions to return, between 1 and 100
        :return: the latest transactions
        :rtype: list

        '''
		if type(count) != int or count < 1 or count > 100:
			return False
		response = fetchGet(self.config['url'] + '/transaction/latest/' + str(count))
		return response.json()

	def queryTransactionIntervalByIndex(self, from_index, to_index):
		'''
        Transactions between the specified indexes

        :param int from_index: the starting index number (inclusive), greater or equal than 0
        :param int to_index: the ending index number (inclusive), greater or equal than 1
        :return: the transactions between the specified indexes
        :rtype: list

        '''
		if type(from_index) != int or type(to_index) != int or to_index - from_index < 1 or from_index < 0 or to_index < 1 or to_index - from_index > 100:
			return False
		response = fetchGet(self.config['url'] + '/transaction/from/' + str(from_index) + '/to/' + str(to_index))
		return response.json()

	def queryTransactionLatestByTimestamp(self, since):
		'''
        Latest transactions since a specific timestamp.

        :param int since: the earliest timestamp of the sought transactions, greater or equal than 0
        :return: the latest transactions since a specific timestamp.
        :rtype: list

        '''
		if type(since) != int or since < 0:
			return False
		response = fetchGet(self.config['url'] + '/transaction/since/' + str(since))
		return response.json()

	def queryTransactionLatestCountByTimestamp(self, since):
		'''
        Amount of transactions since the specified UTC timestamp

        :param int since: the earliest timestamp of the sought transactions, greater or equal than 0
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
        Transactions in a date range

        :param int since: the starting UTC timestamp (inclusive), greater or equal than 0
        :param int until: the ending UTC timestamp (inclusive), greater or equal than 1
        :return: the transactions in a date range
        :rtype: list

        '''
		if type(since) != int or since < 0 or type(until) != int or until < 1 or until - since < 1:
			return False
		response = fetchGet(self.config['url'] + '/transaction/since/' + str(since) + '/until/' + str(until))
		return response.json()

	def queryTransactionIntervalCountByTimestamp(self, since, until):
		'''
        Amount of transactions between the specified UTC timestamps

        :param int since: the starting UTC timestamp (inclusive), greater or equal than 0
        :param int until: the ending UTC timestamp (inclusive), greater or equal than 1
        :return: the amount of transactions between the specified UTC timestamps
        :rtype: int

        '''
		if type(since) != int or since < 0 or type(until) != int or until < 1 or until - since < 1:
			return False
		response = fetchGet(self.config['url'] + '/transaction/since/' + str(since) + '/until/' + str(until) + '/count')
		response_json = response.json()
		return response_json['txCount']
