#!/usr/bin/env python

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import seaborn as sns
from datetime import datetime

import os
from os import path
if path.isfile('yimi.xls'):
    os.remove('yimi.xls')

# interesting fields
cols = ['ship_mobile', 'total_amount', 'pay_status', 'ship_status', 'erp_order_id', 'erp_status', 'createtime', 'last_modified', 'payment', 'shipping', 'member_id', 'promotion_type', 'group_id', 'groupOn_id', 'is_leader', 'group_num', 'status', 'confirm_delivery', 'ship_area', 'weight', 'itemnum', 'ship_time', 'cost_item', 'is_tax', 'tax_type', 'advance', 'score_u', 'score_g', 'discount', 'pmt_goods', 'pmt_order', 'displayonsite', 'cost_freight', 'source', 'city_link', 'verify_city_link', 'fuzzy', 'longitude', 'latitude', 'scalping', 'autoSendErp', 'autoSendErpStatus', 'lang', 'delivery_note_price']

#df = pd.read_excel('test_data.xls', usecols=cols)
df = pd.read_excel('test_data.xls')

df.createtime = df.createtime.map(datetime.fromtimestamp).map(datetime.datetime)
df.last_modified = df.last_modified.map(datetime.fromtimestamp).map(datetime.datetime)

df.to_excel('yimi.xls', index=False)
