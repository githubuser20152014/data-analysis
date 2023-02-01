# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 00:29:35 2023

@author: akhil
"""


# import pandas librar
import pandas as pd

# read the data file into a dataframe
sales = pd.read_csv('salesdata.csv', sep=';')
sales.info()


## now we inspect data
sales.head()

## we calculate profit per item
sales['ProfitPerItem'] = sales['SellingPricePerItem'] - sales['CostPerItem']
print(sales.head())

# calculate profit margin
sales['ProfitMargin'] =  (sales['ProfitPerItem']/sales['SellingPricePerItem'])*100
print(sales.head())

# now we calculate sales per transaction, cost per transaction & profit per transaction
sales['SalesPerTransaction'] = sales['SellingPricePerItem'] * sales['NumberOfItemsPurchased']
sales['CostPerTransaction'] = sales['CostPerItem'] * sales['NumberOfItemsPurchased']
sales['ProfitPerTransaction'] = sales['ProfitPerItem'] * sales['NumberOfItemsPurchased']

# item description is all uppercase, we want it in mixed case (ie. first letter capitalized)
sales['ItemDescription'] = sales['ItemDescription'].str.title()

# we combine Day, Month, Year as one field: Date format: Day-Mon-Year
sales['Date'] = sales['Day'].astype(str) + '-' + sales['Month'] + '-' + sales['Year'].astype(str)

# now we drop Day, Month and Year columns
sales = sales.drop(['Day', 'Month', 'Year'], axis=1)

# we split ClientKeywords into separate columns
sales['ClientAge'] = sales['ClientKeywords'].str.split(',', expand=True)[0].str.replace('[', '')
sales['ClientType'] = sales['ClientKeywords'].str.split(',', expand=True)[1]
sales['ClientDuration'] = sales['ClientKeywords'].str.split(',', expand=True)[2].str.replace(']', '')



# now we drop ClientKeywods column
sales = sales.drop('ClientKeywords', axis=1)

print(sales.head())


# now we have the dataframe ready to export to csv so we can do analysis in Tableau
sales.to_csv('salesdata.csv', index=False)



