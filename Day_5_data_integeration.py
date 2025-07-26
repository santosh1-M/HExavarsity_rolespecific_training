
import pandas as pd
#column name as index for table daata
sales_data = pd.read_csv('sales_data_sample.csv', encoding='latin1')
# print(sales_data)

# #i need to get head of 5 columnd
# print(sales_data[["COUNTRY","ORDERLINENUMBER","SALES"]].head(5))

# usa_df=sales_data[sales_data["COUNTRY"]=="USA"]
# print(usa_df.count())

# print(sales_data.COUNTRY)

# # USING MAP FUNCTION
# map_country={"USA":"US"}
# sales_data["COUNTRY_CHANGED"]=sales_data["COUNTRY"].map(map_country).fillna(sales_data["COUNTRY"])
# print(sales_data.COUNTRY_CHANGED)

# apply function change create new column based on existing column

# print(sales_data.head(2))

# #using apply with normal function:

# def fun_priceeach(priceeach):
#     if pd.isna(priceeach):
#         return "Unknown"
#     elif(priceeach>80):
#         return "average price"
#     elif(priceeach>90):
#         return "medium price"
#     else:
#         return "no segragation"
# sales_data["new_apply_function"]=sales_data["PRICEEACH"].apply(fun_priceeach)
# print(sales_data.head(3))

# # apply for multiple columns in single row
# sales_data["new_apply_lambda"]=sales_data.apply(lambda x: "G00D QUANTITY PRICE" if x["PRICEEACH"] > 90 and x["QUANTITYORDERED"] > 40 else "low QUANTITY PRICE",axis=1)
# print(sales_data.head(3))

# # apply for multiple columns in single row using map

# sales_data["new_apply_map"]=sales_data["PRICEEACH"].map(lambda x: "G00D QUANTITY PRICE" if x > 90 and x > 40 else "low QUANTITY PRICE")
# print(sales_data.new_apply_map)

# # sales_data.to_csv("new_sales_data.csv",index=False)
# new_sales=pd.read_csv("new_sales_data.csv",encoding='latin1')
# print(new_sales)

# # using the fucntion

# # using isin function to get columns ith the same value
# print(sales_data[sales_data["COUNTRY"].isin(["USA","France"])])

# # string.contains:

# print(sales_data[sales_data["TERRITORY"].str.contains("em",case=False,na=False)]["CONTACTFIRSTNAME"])

# # Between function:

# print(sales_data[sales_data["PRICEEACH"].between(80,90)]["PRICEEACH"])

# # using isnull and is notnull

# print(sales_data[sales_data["TERRITORY"].isnull()])

# # NOT NULL FUNCTION

# print(sales_data[sales_data["TERRITORY"].notnull()]["CONTACTFIRSTNAME"])

# # fILTERING DUPLICTES

# print(sales_data[sales_data.duplicated("COUNTRY",keep=False)])
# print(sales_data.duplicated())
# print(sales_data[sales_data.duplicated()])
# print(sales_data[sales_data.duplicated(["COUNTRY"],keep=False)]["COUNTRY"])
# # drop the entire duplicates
# sales_data.drop_duplicates(inplace=True)
# print(sales_data)

# # kkeping the first occurence using the subset
# sales_data.drop_duplicates(subset="COUNTRY",keep='first',inplace=True)
# print(sales_data)
# print(sales_data.drop_duplicates(subset="COUNTRY",keep='last',inplace=True))
# print(sales_data)

# # also using unique
# unique_country=sales_data[sales_data.duplicated("COUNTRY",keep=False)]['COUNTRY'].unique()
# print(unique_country)

# # Values of each count values in the column
# print(sales_data["PRICEEACH"].value_counts())
# print(sales_data["COUNTRY"].value_counts())

# # Duplicates for multicolumn

# multi_col=sales_data[sales_data.duplicated(subset=["COUNTRY","PRICEEACH","CONTACTFIRSTNAME"],keep=False)]
# print(multi_col)

# # Aggregating function

# print(sales_data.groupby("COUNTRY")["PRICEEACH"].mean())
# print(sales_data.groupby("COUNTRY")["PRICEEACH"].mean().sort_values())
# print(sales_data.groupby("COUNTRY")["PRICEEACH"].mean().sort_values(ascending=False))

# # Group by for multiple values

# print(sales_data.groupby(["COUNTRY","ORDERLINENUMBER"])["PRICEEACH"].mean())

# # Groupig with multiple Aggreagetion

# print(sales_data.groupby(["COUNTRY"])["PRICEEACH"].agg(['mean','min','max','sum']))
print(sales_data.groupby("COUNTRY").agg(avg=('PRICEEACH','mean'),max=('PRICEEACH','max')))

# # filter along with group by

# # print(sales_data.groupby("COUNTRY").filter(lambda x: x["PRICEEACH"].mean() > 85))

# print(sales_data.groupby('COUNTRY').apply(lambda x:x[x["PRICEEACH"]>95])[["COUNTRY","PRICEEACH"]])

# # Sort by column
# print(sales_data.sort_values(by='PRICEEACH',ascending=False)['PRICEEACH'])

# SORTING MULTIPLE COLUMNS

# print(sales_data.sort_values(by=['PRICEEACH',"ORDERLINENUMBER"],ascending=[False,True])[['PRICEEACH',"ORDERLINENUMBER"]])
