import pandas as pd
student_data=pd.read_csv("final_college_student_placement_dataset.csv")
print(student_data)

# 1. Categorize placed students into salary bands:
#     Low: < 300,000
#     Medium: 300,000 – 600,000
#     High: > 600,000

student_data["salary_bands"]=student_data["Salary"].map(lambda x:"Low " if x < 300000 else ("Medium" if x > 300000 and x<600000 else "High"))
print(student_data.head(5))

# 2. For each gender and specialization, calculate:
#     Placement rate
#     Average salary (only placed)
#     Avg MBA score

print(student_data.groupby(["Gender","Specialization"]).agg(Placement_rate=('Placement',lambda x: (x=='Yes').mean()),salary_rate=('Placement',lambda x: x[x.notnull()].mean()),Average_MBA_score=('MBA_Percentage','mean')))

# 3.Find how many students have missing values in any column.
print(student_data.isnull().any(axis=1).sum())

# 4. Display all rows where salary is missing.
print(student_data[student_data["Salary"].isnull()])

# 5. Filter only students with complete records (no missing values).
print(student_data[student_data.notnull()])

# 6. Identify if there are any duplicate student entries
print(student_data[student_data.duplicated()])

# 7. Drop the duplicate records and keep only the first occurrence.
print(student_data.drop_duplicates(keep='first'))

# 8. Check for duplicates based only on student_id.
print(student_data[student_data.duplicated('College_ID')])

# 9.Find all unique specializations offered to students.
print(student_data["Specialization"].unique())

# 10. How many unique MBA scores are there?
print(len(student_data["MBA_Percentage"].unique()))

# 11. Count of unique combinations of gender, specialization, and status.
print(student_data.groupby(["Gender","Specialization","Placement"]).size())

# 12. What is the average salary of all placed students?
print(student_data[student_data["Placement"]=='Yes']["Salary"].mean())

# 13. What is the maximum and minimum degree percentage in the dataset?
print(student_data["MBA_Percentage"].min(),student_data["MBA_Percentage"].max())

# 14. Get total number of placed and unplaced students.
print(student_data["Placement"].value_counts().get('Yes'),student_data["Placement"].value_counts().get("No"))

# 15.For each specialization, calculate:
#     Average SSC
#     Average MBA
#     Placement count

print(student_data.groupby("Specialization").agg(Average_SSC=("SSC_Percentage",'mean'),Average_MBA=('MBA_Percentage','mean'),plcaement_count=('Placement',lambda x: (x=='Yes').sum())))

# 16. Create a summary table with:
#     Column name
#     Count of nulls
#     Count of unique values
#     Duplicated value count (if applicable)

summary_table=pd.DataFrame({
    "columns":student_data.columns,
    "count_of_nulls":student_data.isnull().sum().values,
    "count_of_unique":student_data.nunique().values,

})
print(summary_table)