#!/usr/bin/env python

from algoexplorersdk.network.request import fetchGet, fetchPost
from algoexplorersdk.utils.validates import validateHex

class Node:
	'''
    The Node Model
	
	Args:
		config: a dictionary containing the api configuration (url, genesis, id)
	
    '''
	def __init__(self, config: dict):
		'''
		Create a new Node with the provided attributes

        '''
		self.config = config
		
	def sendTransaction(self, hexa: str) -> str:
		'''
		Args:
		    hexa: address of the account to query

		Returns:
			information about the specified address

        '''
		if not validateHex(hexa):
			raise Exception('Invalid argument, must be a hex string')
		body = { 'hexa': hexa }
		response = fetchPost(self.config['url'] + '/sendraw', body)
		response_json = response.json()
		return response_json['hash']
	
	def queryStatus(self) -> dict:
		'''
		Returns:
			information about the specified address

        '''
		response = fetchGet(self.config['url'] + '/status')
		return response.json()