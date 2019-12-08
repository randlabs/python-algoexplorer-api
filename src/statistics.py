#!/usr/bin/env python

import time
from typing import Union, Optional
from request import fetchGet

class Statistics:
	'''
    The Statistics Model
	
	Args:
		config: a dictionary containing the api configuration (url, genesis, id)
	
    '''
	def __init__(self, config: dict):
		'''
		Create a new Statistics with the provided attributes

        '''
		self.config = config
		
	def queryStats(self) -> dict:
		'''
		Returns:
			statistics about the blockchain

        '''
		response = fetchGet(self.config['url'] + '/stats')
		return response.json()
	