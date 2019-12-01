#!/usr/bin/env python

from request import fetchGet

class Transaction:
	def __init__(self, config):
		self.config = config
	
	def transactionsCount(self):
		response = fetchGet(self.config['url'] + '/transaction/count')
		response_json = response.json()
		return response_json['txCount']
		
	def queryTransaction(self, txid_or_index):
		if (type(txid_or_index) != str and type(txid_or_index) != int) or txid_or_index < 0:
			return False
		response = fetchGet(self.config['url'] + '/transaction/' + str(txid_or_index))
		return response.json()

	def queryLatestByIndex(self, count):
		if type(count) != int or count < 1 or count > 100:
			return False
		response = fetchGet(self.config['url'] + '/transaction/latest/' + str(count))
		return response.json()

	def queryIntervalByIndex(self, from_index, to_index):
		if type(from_index) != int or type(to_index) != int or to_index - from_index < 1 or from_index < 0 or to_index < 1 or to_index - from_index > 100:
			return False
		response = fetchGet(self.config['url'] + '/transaction/from/' + str(from_index) + '/to/' + str(to_index))
		return response.json()

	def queryLatestByTimestamp(self, since):
		if type(since) != int or since < 0:
			return False
		response = fetchGet(self.config['url'] + '/transaction/since/' + str(since))
		return response.json()

	def queryLatestCountByTimestamp(self, since):
		if type(since) != int or since < 0:
			return False
		response = fetchGet(self.config['url'] + '/transaction/since/' + str(since) + '/count')
		response_json = response.json()
		return response_json['txCount']

	def queryIntervalByTimestamp(self, since, until):
		if type(since) != int or since < 0 or type(until) != int or until < 1 or until - since < 1:
			return False
		response = fetchGet(self.config['url'] + '/transaction/since/' + str(since) + '/until/' + str(until))
		return response.json()

	def queryIntervalCountByTimestamp(self, since, until):
		if type(since) != int or since < 0 or type(until) != int or until < 1 or until - since < 1:
			return False
		response = fetchGet(self.config['url'] + '/transaction/since/' + str(since) + '/until/' + str(until) + '/count')
		response_json = response.json()
		return response_json['txCount']
