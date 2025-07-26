import pandas as pd
student_data=pd.read_csv("updated_college_student_placement_dataset.csv")
# print(student_data)

# # code 1:
# #Getting the number of students
# print(student_data.shape[0])

# #code 2:
# # College getting placed or not
print(student_data.Gender.value_counts().get("Male"))
print(student_data.Gender.value_counts().get("Female"))

# # code 3:
# # getting average percentage in mba

# print("Average MBA percentage",student_data.MBA_Percentage.mean())

# # code 4:
# # getting value based on ssc and hsc percentage

# print("Students scored 80% above in both conditon",student_data[(student_data["SSC_Percentage"]>80) &(student_data["HSC_Percentage"]>80) ])
# print("Students scored 80% above in both conditon\n",student_data[(student_data["SSC_Percentage"]>80) &(student_data["HSC_Percentage"]>80) ]["College_ID"])

# # code 5:
# # person with prior work experience

# print(student_data[student_data["Internship_Experience"]=="Yes"])

# code 6:
# 

# # code 7:
# # count of placed and non placend student

# print(student_data.Placement.value_counts().get("Yes"))
# print(student_data.Placement.value_counts().get("No"))

# code 8:
# 

# code 9:
# placement succes column

student_data["Placement_Succes_new"]=student_data.apply(lambda row:'High' if row["Placement"]=="Yes" and row["Salary"]>95000 else( 'average' if row["Placement"]=="Yes" and row["Salary"]>40000 else 'Unplace'),axis=1 )
print(student_data)