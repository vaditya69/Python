import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

store = pd.read_csv('C:/Users/Adity/Desktop/Aditya/CSV/Orders csv.csv', encoding="ISO-8859-1")
store2 = pd.read_csv("C:/Users/Adity/Desktop/Aditya/CSV/Return csv.csv")
store3 = pd.read_csv("C:/Users/Adity/Desktop/Aditya/CSV/User csv.csv")
print(store)
print(store.info())

'''
#CHECKING THE NUMBER OF FREQUENCY OF SUB_CATEGORY PRODUCT
# store['number'] = store.groupby('Product Sub-Category').cumcount() + 1
store['number'] = 1
store = store[["Product Category", 'Product Sub-Category', 'Sales', 'Profit', 'Quantity ordered new', 'number']]

#USING GROUP BY
store2 = store.groupby('Product Sub-Category')[['Sales', 'Quantity ordered new', 'number']].sum().sort_values('Sales' ,ascending = False)
print(store2)
#FOR CHECKING THE MOST RECURING PRODUCT SUB_CATEGORY
print(store2['number'].max())


#FINDING A SPECIFIC SUB CATEGORY BY USING str.contians()
store = store[store['Product Sub-Category'].str.contains('Computer Peripherals')]
print(store)
print(store.count())


#CREATING A TABLE FOR EACH SUB CATEGORY AND ANALYZING SALES
category = store['Product Category'].unique()

for letter in category:
    print('This is the table for ' + letter.upper())
    category_sales = store[store['Product Category'] == letter].reset_index()
    print(category_sales.Sales)


#FINDING OUT THE DUPLICATE VALUES IN ROW_ID
#This gives us the comparison between the total no. of entries and non-duplicate entries
store_dupli = set(store['Row ID'])
print(store['Row ID'].count())
print(len(store_dupli))
#FINDING THE DUPLICATE ONE
b = store[store['Row ID'].duplicated(keep = False)]
print(b['Row ID'].unique())
print(store[store['Row ID'] == 22015])

#ANALYZING UNIT PRICE MORE THAN 50
ups50 = store.loc[store['Unit Price'] >50, ['Product Category', 'Sales', 'Unit Price']].reset_index()
print(ups50)
'''

# WORKING WITH MULTIPAL SHEETS AND ANALYZING
# ALSO VISUALIZING THE OUTPUT

'''
#CHECKING REGION WISE
store = store.groupby('Region')
print(store.Discount.sum())
print(store['Row ID'].count())
#CHECKING OUT THE SALES AND PROFIT (REGION WISE) AND VISUALZING DATA USING STACKED BAR CHART
store_new = store.groupby('Region').sum()
print(store_new[['Sales', 'Profit']])


labels = list(store_new.index)
sales= list(store_new.Sales)
profit = list(store_new.Profit)


plt.bar(labels, profit, label = 'Sales')
plt.bar(labels, sales, bottom = profit, label = 'Profit')
plt.xlabel('Region')
plt.ylabel('SALES AND PROFIT')
plt.title('Sales and Profit Analysis(Region Wise)')
plt.legend()
plt.show()
'''
'''
# USING DATE AND TIME
# CONVERTING THE ORDER/SHIP DATE TYPE TO DATE
store['Order_Date'] = pd.to_datetime(store['Order Date'])
store['Ship_Date'] = pd.to_datetime(store['Ship Date'])
print(store)
print(store.info())

store['month'] = store['Order_Date'].dt.month
#CHECKING
'''
'''
print(store)
counter = 1
while counter <= max(store.month):
    condition = store[store['month'] == counter]
    horizontal = list(range(1, len(condition) + 1))
    print(horizontal)
    counter += 1
'''
'''
#MONTH WISE SALES REPORT
store = store.groupby('month')['Sales'].sum().reset_index()
print(store)

#FOR CROSS CHECKING
print(store.sum())
print(store.Sales.sum())
'''
'''
#ANALYSIS1 : REGION WISE MONTHLY SALES/PROFIT REPORT
store = store.groupby(['month', 'Region'])[['Sales', 'Profit']].sum().reset_index()
print(store)
#ADDING PROFIT COULMN IN ANALYSIS1
store = store.groupby(['month', 'Region'])[['Sales', 'Profit']].sum().reset_index()
store['percentage'] = (store.Profit/store.Sales) * 100
print(store)
'''
'''
#USING OF CUMULATIVE SUM FOR BETTER REGION ANALYSIS
store['cumu sales'] = 0
for regions in store.Region.unique():
    collection = store['Sales'].where(store["Region"] == regions).cumsum()
    store.loc[store['Region'] == regions, 'cumu sales'] = collection

# print(store)
for month, rows in store.groupby('month'):
    print(f"Month: {month}")
    print(rows)
    print('\n\n')

#DATA PLOTING AND VISUALIZING ALL THE DATA AT ONCE
for region in store['Region'].unique():
    region_data = store[store['Region'] == region]
    plt.plot(region_data['month'], region_data['Sales'], label=region)
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Month wise Sales Data for each Region')
plt.legend()
plt.show()
'''
'''
#DATA PLOTING AND VISUALIZING ALL THE DATA(Month Wise) USING SUBPLOT

for regions in store.Region.unique():
    collection = store['Sales'].where(store["Region"] == regions).cumsum()
    store.loc[store['Region'] == regions, 'cumu sales'] = collection

for month, rows in store.groupby('month'):
    print(f"Month: {month}")
    print(rows)
    print('\n\n')

#DATA PLOTING AND VISUALIZING ALL THE DATA AT ONCE
counter = 1
for region in store['Region'].unique():
    region_data = store[store['Region'] == region]
    plt.subplot(2,2,counter)
    plt.plot(region_data['month'], region_data['Sales'], label=region)
    plt.plot(region_data['month'], region_data['Profit'], label=region, linestyle = '--')


    counter += 1

    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.title('Month wise Sales Data for ' + region + ' Region')

plt.show()
'''
'''
# CREATING A FUNCTION TO SEE THE MATCHING ORDER RETURN VALUES.
def returns(store, store2):
    # List to store rows with matching Order IDs
    matching_rows = []
    storage = set(matching_rows)

    # Loop through each Order ID in store and check if it exists in store2
    for row in store['Order ID'].values:
        if row in store2['Order ID'].values:
            # Append matching rows to the list
            matching_rows.append(store[store['Order ID'] == row])
            # store= store.drop(store[store['Order ID'] == 13959].index)

    # Concatenate all matching rows into a single DataFrame
    if matching_rows:
        merged_output = pd.concat(matching_rows).drop_duplicates().reset_index(drop=True)
        store = store[~store['Order ID'].isin(merged_output['Order ID'])]
        # print(merged_output)   #FOR CHECKING THE COMMON ORDER RETURNS VALUES
        return store.reset_index()  # FOR VIEWING THE REMOVED RETURN VALUES
    else:
        print("No matching rows found.")
        return store


store_new = returns(store, store2)
print(store_new)

#USING THE FUNCTION CREATED ABOVE FOR CHECKING THE REGIONS WHERE THE MOST ORDERS ARE BEING RETURNED
def returns(store, store2):
    # List to store rows with matching Order IDs
    matching_rows = []
    storage = set(matching_rows)

    # Loop through each Order ID in store and check if it exists in store2
    for row in store['Order ID'].values:
        if row in store2['Order ID'].values:
            # Append matching rows to the list
            matching_rows.append(store[store['Order ID'] == row])
            # store= store.drop(store[store['Order ID'] == 13959].index)

    # Concatenate all matching rows into a single DataFrame
    if matching_rows:
        merged_output = pd.concat(matching_rows).drop_duplicates().reset_index(drop=True)
        store = store[store['Order ID'].isin(merged_output['Order ID'])]
        column_ids = ['Region', 'Sales', 'Profit', 'Quantity ordered new', 'Row ID']
        print(merged_output[column_ids])   #FOR CHECKING THE COMMON ORDER RETURNS VALUES
        merged = merged_output.groupby('Region').sum()
        print(merged[['Sales', 'Profit', 'Quantity ordered new', 'Row ID']])
        # return store.reset_index()  # FOR VIEWING THE REMOVED RETURN VALUES
    else:
        print("No matching rows found.")
        return store

returns(store, store2)
'''
