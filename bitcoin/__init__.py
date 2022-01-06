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


import bitcoin.core

# Note that setup.py can break if __init__.py imports any external
# dependencies, as these might not be installed when setup.py runs. In this
# case __version__ could be moved to a separate version.py and imported here.
__version__ = '0.11.1dev'

class MainParams(bitcoin.core.CoreMainParams):
    MESSAGE_START = b'\x03\xd5\xb5\x03'
    DEFAULT_PORT = 65534
    RPC_PORT = 65535
    DNS_SEEDS = (('unobtanium.uno','node1.unobtanium.uno'),
                 ('unobtanium.uno','node2.unobtanium.uno'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':130,
                       'SCRIPT_ADDR':30,
                       'SECRET_KEY' :224}
    BECH32_HRP = 'un'

class TestNetParams(bitcoin.core.CoreTestNetParams):
    MESSAGE_START = b'\x01\x02\x03\x04'
    DEFAULT_PORT = 65522
    RPC_PORT = 65531
    DNS_SEEDS = (('temporary','3.144.134.250'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':68,
                       'SCRIPT_ADDR':30,
                       'SECRET_KEY' :239}
    BECH32_HRP = 'tun'

class SigNetParams(bitcoin.core.CoreSigNetParams):
    MESSAGE_START = b'\x0a\x03\xcf\x40'
    DEFAULT_PORT = 38333
    RPC_PORT = 38332
    DNS_SEEDS = (("signet.bitcoin.sprovoost.nl", "seed.signet.bitcoin.sprovoost.nl"))

class RegTestParams(bitcoin.core.CoreRegTestParams):
    MESSAGE_START = b'\xfa\xbf\xb5\xda'
    DEFAULT_PORT = 18444
    RPC_PORT = 18443
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}
    BECH32_HRP = 'bcrt'

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
