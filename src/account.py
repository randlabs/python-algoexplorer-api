#!/usr/bin/env python

from request import fetchGet
from algosdk import encoding

class Account:
	def __init__(self, config):
		self.config = config
		
	def queryAddress(self, address):
		if (not encoding.is_valid_address(address)):
			raise Exception('Invalid address')
		response = fetchGet(self.config['url'] + '/account/' + address)
		return response.json()
		
	def queryAddressTransactions(self, address, count):
		if (not encoding.is_valid_address(address)) or type(count) != int or count < 1:
			raise Exception('Invalid type')
		response = fetchGet(self.config['url'] + '/account/' + address + '/transactions/latest/' + str(count))
		return response.json()

	def queryAddressTransactionsFromInterval(self, address, from_round, to_round):
		if (not encoding.is_valid_address(address)) or type(from_round) != int or type(to_round) != int or (to_round - from_round < 1) or from_round < 0 or to_round < 1 or (to_round - from_round > 99):
			raise Exception('Invalid type')
		response = fetchGet(self.config['url'] + '/account/' + address + '/transactions/from/' + str(from_round) + '/to/' + str(to_round))
		return response.json()

	def queryAddressTransactionsSince(self, address, since, until=None):
		if (not encoding.is_valid_address(address)) or type(since) != int or since < 0 or (until and type(until) != int) or (until and until < 1) or (until and (until - since) < 1):
			raise Exception('Invalid type')
		url = self.config['url'] + '/account/' + address + '/transactions/since/' + str(since)
		if until:
			response = fetchGet(url + '/until/' + str(until))
		else:
			response = fetchGet(url)
		return response.json()

	def queryAddressTransactionsSinceCount(self, address, since, until):
		if (not encoding.is_valid_address(address)) or type(since) != int or since < 0 or (until and type(until) != int) or (until and until < 1) or (until and (until - since) < 1):
			raise Exception('Invalid type')
		url = self.config['url'] + '/account/' + address + '/transactions/since/' + str(since)
		if until:
			response = fetchGet(url + '/until/' + str(until) + '/count')
		else:
			response = fetchGet(url + '/count')
		return response.json()
