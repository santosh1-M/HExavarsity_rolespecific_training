import pandas as pd

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     'Age': [25, 30, 25, 22, 28],
#     'City': ['New York', 'Los Angeles', 'New York', "London", 'Chicago'],
#     'Score': [85, 90, 95, 99, 88]
# }

# df = pd.DataFrame(data,index=['s1','s2','s3','s4','s5'])
# print(df )


sales_data = pd.read_csv('sales_data_sample.csv', encoding='latin1')

# print(sales_data)

## return top 5 rows from the csv file
# print(sales_data.head())

##returning the row based on the conditon
#print(sales_data.iloc[:3])

# #returning the colum based on two methods

# print(sales_data.PRICEEACH)
# print(sales_data['PRICEEACH'])

# # Return row and columns based on specified conditon

# print(sales_data.iloc[:,1:5])
# print(sales_data.iloc[:,6:10])

# # returning values based on COLUMN WITH ILOC

# print(sales_data.PRICEEACH.iloc[:])
# print(sales_data.PRICEEACH.iloc[5])

# # returing values with list in iloc

# print(sales_data.iloc[[1,3,4,5],1])
# print(sales_data.iloc[[1,3,4,5],[1,2,3,4,5]])

# # redaing values from tha end

# print(sales_data.iloc[-1])
# print(sales_data.iloc[:,-1])
# print(sales_data.iloc[:-2000,-8:-3])

# # Using the labels displaying the values 
# print(sales_data.loc[25,'PRICEEACH'])
# print(sales_data.loc[0:25,'PRICEEACH'])

# #creating new data using the exixting data
# new_sales_data=sales_data.loc[:,"PRICEEACH":"ORDERLINENUMBER"]
# print(new_sales_data)

# # set index
# new_sales_data=sales_data.set_index("ORDERLINENUMBER")
# print(new_sales_data)

# # CONDITION
# print(sales_data.COUNTRY=="France")
# print(sales_data.loc[sales_data.COUNTRY=="France"])
# print(sales_data.loc[(sales_data.COUNTRY=="France"),["CUSTOMERNAME","PHONE"]])

# # ISINFUNCTION
# print(sales_data.loc[sales_data.COUNTRY.isin(["France","USA"]),["CUSTOMERNAME","PHONE"]])

# #GETTING ISNULL VALUES
# print(sales_data.loc[sales_data.TERRITORY.notnull()])

# #ADDING NEW COLUMN

# sales_data["New column"]="userdef"
# print(sales_data.head())

##summary Function
# print(sales_data.describe())
# print(sales_data.COUNTRY.describe())
# print(sales_data.ORDERNUMBER.mean())
# print(sales_data.ORDERLINENUMBER.mean())
# print(sales_data.CUSTOMERNAME.unique())
# print(sales_data.COUNTRY.value_counts().get("France"))
# print((sales_data.COUNTRY=="France").sum())
