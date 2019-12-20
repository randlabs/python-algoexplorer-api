#!/usr/bin/env python

import base64
import binascii

def validateBase64String(base64: str) -> bool:
	try:
		base64.decodestring(base64)
		return True
	except binascii.Error:
		return False

def validateHex(hex: str) -> bool:
	try:
		int(hex, 16)
		return True
	except ValueError:
		return False