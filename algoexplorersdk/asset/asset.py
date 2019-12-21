#!/usr/bin/env python

from algosdk import encoding
from algoexplorersdk.network.request import fetchGet

class Asset:
	'''
    The Asset Model
	
	Args:
		config: a dictionary containing the api configuration (url, genesis, id)
	
    '''
	def __init__(self, config: dict):
		'''
		Create a new Asset with the provided attributes

        '''
		self.config = config
		
	def queryRelevantAssets(self, address: str) -> list:
		'''
		Args:
			address: address of the account to query

		Returns:
			assets that had movements in this account

        '''
		if (not encoding.is_valid_address(address)):
			raise Exception('Invalid address')
		response = fetchGet(self.config['url'] + '/account/' + address + '/assets/relevant')
		return response.json()
