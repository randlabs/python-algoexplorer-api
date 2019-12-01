#!/usr/bin/env python

from request import fetchGet

class Block:
	def __init__(self, config):
		self.config = config
	
	def blockCount(self):
		response = fetchGet(self.config['url'] + '/block/count')
		response_json = response.json()
		return response_json['blockCount']

	def queryBlock(self, hash_or_round):
		if (type(hash_or_round) != int and type(hash_or_round) != str) or (type(hash_or_round) == int and hash_or_round < 0):
			return False
		response = fetchGet(self.config['url'] + '/block/' + str(hash_or_round))
		return response.json()

	def queryLatestByRound(self, count):
		if type(count) != int or count < 1 or count > 100:
			return False
		response = fetchGet(self.config['url'] + '/block/latest/' + str(count))
		return response.json()

	def queryIntervalByRound(self, from_round, to_round):
		if type(from_round) != int or type(to_round) != int or to_round - from_round < 1 or to_round < 1 or from_round < 0:
			return False
		if to_round - from_round > 99:
			return False
		response = fetchGet(self.config['url'] + '/block/from/' + str(from_round) + '/to/' + str(to_round))
		return response.json()

	def queryLatestByTimestamp(self, since):
		if type(since) != int or since < 0:
			return False
		response = fetchGet(self.config['url'] + '/block/since/' + str(since))
		return response.json()

	def queryLatestCountByTimestamp(self, since):
		if type(since) != int or since < 0:
			return False
		response = fetchGet(self.config['url'] + '/block/since/' + str(since) + '/count')
		response_json = response.json()
		return response_json['blockCount']

	def queryIntervalByTimestamp(self, since, until):
		if type(since) != int or type(until) != int or until - since < 1 or until - since > 172799 or since < 0 or until < 1:
			return False
		response = fetchGet(self.config['url'] + '/block/since/' + str(since) + '/until/' + str(until))
		return response.json()

	def queryIntervalCountByTimestamp(self, since, until):
		if type(since) != int or type(until) != int or until - since < 1 or until - since > 172799 or since < 0 or until < 1:
			return False
		response = fetchGet(self.config['url'] + '/block/since/' + str(since) + '/until/' + str(until) + '/count')
		response_json = response.json()
		return response_json['blockCount']

	def queryBlockTransactions(self, hash_or_round):
		if (type(hash_or_round) != int and type(hash_or_round) != str) or (type(hash_or_round) == int and hash_or_round < 0):
			return False
		response = fetchGet(self.config['url'] + '/block/' + str(hash_or_round) + '/transactions')
		return response.json()
