# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 08:00:56 2019

@author: Abhishek
"""

import pandas as pd
import requests

filename = 'C:/This/Is/Random.csv'
destination_file = 'C/This/Is/Output.xls'

parameters_countries = pd.read_csv(filename)
def get_data(name,pid):
    fr_data = pd.DataFrame()
    main_url = 'https://app.abcdef.com/api/whynot'
    offset = 0
    while offset < 10000:
        querystring = {
        'dataset': 'widgetdata',
        'dashboard_id': str(parameters_countries['dashboardId'][0]),
        'widget_id' :str(parameters_countries['widgetId'][0]),
        'use_date_from' : '2019-06-01',
        'use_date_to' : '2019-06-30',
        'offset':offset,
        'id' : pid,
        'key' : '5ef806d06041c4c6b82f2254e6cd4acef11890aecbe763c0f789b2c53494df0c',
        'secret' : '13ba0c06a16df5fad7633cf7333a8372f81c022c7f94c958a4308a6600a3c9b1'}
        try:
            req = requests.request("GET",main_url,params=querystring).json()
        except:
            print('API limit exceeded...')
        if len(req['data']) > 0:
            data = pd.DataFrame(req['data'])
            data['pid'] = pid
            data['Market'] = name
            fr_data = fr_data.append(data)
            offset = offset+50
        else:
            print('All data extracted')
            break
    return fr_data

complete_data = pd.DataFrame()
for i,j in zip(parameters_countries['Countries'],parameters_countries['PID']):
    print('Started Extracting ',i,'...')
    complete_data = complete_data.append(get_data(i,j))
    print('Extraction completed for ',j,'...')

#Remove duplicates from data
complete_data = complete_data.drop_duplicates()
complete_data.to_excel(destination_file, index= False)

