#!/usr/bin/env python
# coding: utf-8

# Author: Zachary Wu
# Edit time: 05-03-2021
# status: partial complete

###
# realize currency_formatter which takes in series of string data and corresponding denotation type (euro, USD, etc.)
# and convert into integer, float or other denotation type 
###

import pandas as pd


class Currency:
    def __init__(self, data, ctype):
        self.data = data
        self.ctype = ctype
    
    def to_int(self):
        if self.ctype == 'euro':
            return self.euro_to_int(self.data)
        
        elif self.nation == 'usd':
            return self.usd_to_int(self.data)
        
    def euro_to_int(self, data):
        data = data.str.replace('.', '')
        data = data.str.replace(',', '.')
        data = pd.to_numeric(data)
        
        return data
        
    def usd_to_int(self, data):
        return 






