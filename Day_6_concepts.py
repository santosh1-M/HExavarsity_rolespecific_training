import pandas as pd
sales_data = pd.read_csv('sales_data_sample.csv', encoding='latin1')
print(sales_data)

# # print information of table
print(sales_data.info())

# # printing information of column datatypes
print(sales_data.dtypes)

# # converting datatype using astype:
sales_data["STATUS"]=sales_data["STATUS"].astype("string")
print(sales_data.dtypes)

# # # to_numeric in table(sales_data[,error='coerce'])
sales_data['PRICEEACH'] = pd.to_numeric(sales_data['PRICEEACH'], errors='coerce')
print(sales_data.head())

# # automatic-typr_conversion
print(sales_data.dtypes)
print(sales_data.convert_dtypes())
print(sales_data.dtypes)

# # isnull()
print(sales_data.isnull())
print(sales_data.isnull().sum())
print(sales_data.isnull().any(axis=1).sum())
print(sales_data[sales_data.isnull()])

# # isna() is same as isnull
print(sales_data.isna().sum())

# # notnull() or df.notna()
print(sales_data.notnull().sum())
print(sales_data.notnull().any(axis=1).sum())
print(sales_data[sales_data.notnull()])
print(sales_data[sales_data["ORDERLINENUMBER"].isnull()])

# # USING FILLNA

sales_data["PRICEEACH"]=sales_data["PRICEEACH"].fillna(sales_data["PRICEEACH"].median())
print(sales_data.head())

# # usinf fastfilling:

sales_data["TERRITORY"]=sales_data["TERRITORY"].ffill()
print(sales_data)

# # dropping columns

print(len(sales_data))
print(sales_data.isnull())
sales_data=sales_data.dropna()
print(sales_data)
print(len(sales_data))
sales_data.to_csv("new_sales.csv")

clean_data=pd.read_csv("sales_data_cleaned.csv")
print(clean_data)    

# Renaming the file with rename
clean_data.rename(columns={'PRICEEACH':"PRICE"},inplace=True)
print(clean_data)

# clean_data.rename(columns)

clean_data["COMBINED_DATA"]=clean_data["CONTACTLASTNAME"]+"|"+clean_data["CONTACTFIRSTNAME"]
print(clean_data)

clean_data['PRICECATEGORY']=pd.cut(clean_data['PRICE'],bins=[80,90,100,120],labels=['Good','Premium','Luxury'])
print(clean_data)