#!/usr/bin/env python

from .node.node import Node
from .block.block import Block
from .account.account import Account
from .statistics.statistics import Statistics
from .transaction.transaction import Transaction
from .config import MAINNET, TESTNET, BETANET

class AlgoexplorerApi(Block, Transaction, Account, Statistics, Node):
    def __init__(self, network_name: str = 'mainnet'):
        if network_name:
            if network_name == 'mainnet':
                self._config = MAINNET
            elif network_name == 'testnet':
                self._config = TESTNET
            elif network_name == 'betanet':
                self._config = BETANET
        
        Block.__init__(self, self._config)
        Transaction.__init__(self, self._config)
        Account.__init__(self, self._config)
        Statistics.__init__(self, self._config)
        Node.__init__(self, self._config)

    def getGenesisId(self):
        '''
		Returns:
			the genesis ID

        '''
        return self._config['id']
        
    def getGenesisHash(self):
        '''
		Returns:
			the genesis Hash

        '''
        return self._config['genesis']
