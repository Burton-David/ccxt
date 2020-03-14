# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.async_support.okex3 import okex3


class okcoinusd(okex3):

    def describe(self):
        return self.deep_extend(super(okcoinusd, self).describe(), {
            'id': 'okcoinusd',
            'name': 'OKCoin USD',
            'countries': ['CN', 'US'],
            'hostname': 'www.okcoin.com',
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/27766791-89ffb502-5ee5-11e7-8a5b-c5950b68ac65.jpg',
                'www': 'https://www.okcoin.com',
                'doc': 'https://www.okcoin.com/docs/en/',
                'fees': 'https://www.okcoin.com/coin-fees',
                'referral': 'https://www.okcoin.com/account/register?flag=activity&channelId=600001513',
            },
            'fees': {
                'trading': {
                    'taker': 0.002,
                    'maker': 0.001,
                },
            },
            'options': {
                'fetchMarkets': ['spot'],
            },
        })
