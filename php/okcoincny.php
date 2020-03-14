<?php

namespace ccxt;

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

use Exception; // a common import

class okcoincny extends okcoinusd {

    public function describe () {
        return array_replace_recursive(parent::describe (), array(
            'id' => 'okcoincny',
            'name' => 'OKCoin CNY',
            'countries' => array( 'CN' ),
            'hostname' => 'www.okcoin.cn',
            'urls' => array(
                'logo' => 'https://user-images.githubusercontent.com/1294454/27766792-8be9157a-5ee5-11e7-926c-6d69b8d3378d.jpg',
                'www' => 'https://www.okcoin.cn',
                'doc' => 'https://www.okcoin.cn/docs/en/',
                'fees' => 'https://www.okcoin.cn/coin-fees',
                'referral' => 'https://www.okcoin.cn',
            ),
        ));
    }
}
