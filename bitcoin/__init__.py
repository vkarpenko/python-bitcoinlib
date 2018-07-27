# Copyright (C) 2012-2018 The python-bitcoinlib developers
#
# This file is part of python-bitcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

from __future__ import absolute_import, division, print_function, unicode_literals

import bitcoin.core

# Note that setup.py can break if __init__.py imports any external
# dependencies, as these might not be installed when setup.py runs. In this
# case __version__ could be moved to a separate version.py and imported here.
__version__ = '0.10.2dev'

class MainParams(bitcoin.core.CoreMainParams):
    MESSAGE_START = b'\x4b\x4a\x4c\x5d'
    DEFAULT_PORT = 8335
    RPC_PORT = 8332
    DNS_SEEDS = (('138.197.73.48', '138.197.73.48'),
                 ('138.197.73.123', '138.197.73.123'),
                 ('159.203.70.193', '159.203.70.193'),
                 ('88.198.33.35', '88.198.33.35'),
                 ('95.85.35.152', '95.85.35.152'),
                 ('78.46.93.126', '78.46.93.126'),
                 ('91.233.111.28', '91.233.111.28'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':75,
                       'SCRIPT_ADDR':5,
                       'SECRET_KEY' :128}

class TestNetParams(bitcoin.core.CoreTestNetParams):
    MESSAGE_START = b'\x54\x4a\x4c\x54'
    DEFAULT_PORT = 8336
    RPC_PORT = 18332
    DNS_SEEDS = (('138.197.90.246', '138.197.90.246'),
                 ('139.59.154.41', '139.59.154.41'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}

class RegTestParams(bitcoin.core.CoreRegTestParams):
    MESSAGE_START = b'\x4b\x4a\x4c\x5d'
    DEFAULT_PORT = 18444
    RPC_PORT = 18443
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}

"""Master global setting for what chain params we're using.

However, don't set this directly, use SelectParams() instead so as to set the
bitcoin.core.params correctly too.
"""
#params = bitcoin.core.coreparams = MainParams()
params = MainParams()

def SelectParams(name):
    """Select the chain parameters to use

    name is one of 'mainnet', 'testnet', or 'regtest'

    Default chain is 'mainnet'
    """
    global params
    bitcoin.core._SelectCoreParams(name)
    if name == 'mainnet':
        params = bitcoin.core.coreparams = MainParams()
    elif name == 'testnet':
        params = bitcoin.core.coreparams = TestNetParams()
    elif name == 'regtest':
        params = bitcoin.core.coreparams = RegTestParams()
    else:
        raise ValueError('Unknown chain %r' % name)
