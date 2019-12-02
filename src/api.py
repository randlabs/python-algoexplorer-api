#!/usr/bin/env python

from config import MAINNET, TESTNET, BETANET
from block import Block
from transaction import Transaction

class AlgoexplorerApi(Block, Transaction):
    def __init__(self, network_name = MAINNET):
        if network_name:
            if network_name == 'mainnet':
                self._config = MAINNET
            elif network_name == 'testnet':
                self._config = TESTNET
            elif network_name == 'betanet':
                self._config = BETANET
        
        Block.__init__(self, self._config)
        Transaction.__init__(self, self._config)
