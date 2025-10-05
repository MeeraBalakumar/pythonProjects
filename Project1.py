import numpy as np
#sales details
daily_sales=np.array([255,275,385,210,390])

print('average sales;',np.mean(daily_sales))
print('maximum sales:',np.max(daily_sales))
print('minimum sales:',np.min(daily_sales))

import pandas as pd

days=('Mon','Tue','Wed','Thu','Fri')

sales_df=pd.DataFrame({'day':days,'sales':daily_sales})
print(sales_df)

sales_df['sales_With_ Tax']=sales_df['sales']*1.10
print(sales_df)

high_sales = sales_df[sales_df['sales'] > 300]
print(high_sales)
 
"""
Spyder Editor

This is a temporary script file.
"""
