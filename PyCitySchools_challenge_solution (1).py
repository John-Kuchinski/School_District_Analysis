#!/usr/bin/env python
# coding: utf-8

# In[409]:


# Dependencies and setup
import pandas as pd
import os


# In[410]:


# DELIVERABLE 1
   #File to load/ Read the school data and store into a pandas
new_full_student_data = os.path.join('..', 'School_District_Analysis', 'Resources', 'new_full_student_data.csv')
student_df = pd.read_csv(new_full_student_data)

# Use .head() funtion to view the top rows of data
student_df.head()


# In[411]:


# DELIVERABLE 2: PREPARE THE DATA
student_df.count()


# In[412]:


#CHECK FOR ROWS THAT HAVE "NaN" OR MISSING VALUES
student_df.isna().sum()


# In[413]:


# Drop Na values
student_df = student_df.dropna()
student_df.isna().sum()


# In[414]:


# Check for duplicates
student_df.duplicated().sum()


# In[415]:


#Drop the duplicates
student_df = student_df.drop_duplicates()
student_df.duplicated().sum()


# In[416]:


#Check the type of the grade column with dtypes
student_df.dtypes


# In[417]:


# remove"th" from values by locating grade column then replacing strings in each iteration
student_df['grade']


# In[418]:


#Remove "th"

student_df['grade'] = student_df['grade'].str.replace('th','')
student_df['grade']                                                    
                                                      


# In[419]:


# CHANGE THE "grade" COLUMN TO THE "int" type using astype function
student_df['grade'] = student_df['grade'].astype(int)
student_df.dtypes


# In[420]:


# Use the head or tail funtion to display the data
student_df.head()


# In[421]:


# DELIVERABLE 3: SUMMARIZE THE DATA
student_df.describe()


# In[422]:


# display the mean math score
student_df['math_score'].mean()


# In[423]:


# store the minimum math score in data as min_reading_score
student_df['reading_score'].min()


# In[424]:


min_reading_score = student_df['reading_score'].min()
min_reading_score


# In[425]:


# DELIVERABLE 4: DRILL DOWN INTO THE DATA
# 1. DISPLAY THE GRADE COLUMN BY USING "loc" FUNCTION
student_df['grade'].loc()
student_df['grade']


# In[426]:


#display the first three rows of columns 3, 4, 5 by using iloc
student_df.keys()


# In[427]:


student_df[['school_name','reading_score','math_score']].iloc[0:3]


# In[428]:


# select the rows for grade 9, and display their summary statisitics by using loc and decribe
student_df.loc[student_df["grade"]==9]
student_df_grade_9 = student_df.loc[student_df["grade"]==9]


# In[429]:


student_df_grade_9.describe()


# In[430]:


student_df_grade_9['reading_score'].min()


# In[431]:


min_reading_score = student_df_grade_9['reading_score'].min()
min_reading_score


# In[432]:


# store the row with minimum overall reading score in min_reading_row by using "loc" and "min_reading_score" variable 
    #from above
student_df.loc[student_df["grade"]==10]
student_df_grade_10 = student_df.loc[student_df["grade"]==10]
student_df_grade_10.head()


# In[433]:


student_df_grade_10.describe()


# In[434]:


student_df['reading_score'].min()


# In[435]:


student_df.loc[student_df["reading_score"]==10.5]
min_reading_row = student_df.loc[student_df["reading_score"]==10.5]


# In[436]:


# select all reading scores from 10th graders at Dixon High SChool by using "loc" with conditionals
#student_df.loc[student_df["grade"]==10]
reading_scores = student_df.loc[
    (student_df['grade'] == 10) & 
    (student_df['school_name'] == 'Dixon High School'), 
        ['school_name', 
        'reading_score']]
reading_scores


# In[437]:


mean_reading_grades_11_12 = student_df.loc[(student_df['grade']==11) 
                                           | (student_df['grade']==12), 'reading_score'].mean()
mean_reading_grades_11_12


# In[452]:


# Use groupby and mean to find the average reading and math scores for each school type.
avg_scores_by_school_type = student_df.loc[:,['school_budget',
                                               'school_type']].groupby(by='school_type').mean().round()
avg_scores_by_school_type


# In[441]:


# setting a new variable in df in order to pull from the frame to group students by school
var1 = student_df[['school_name', 'student_id']]

var1.groupby('school_name').count().sort_values(by="student_id", ascending=False)





# In[451]:


#created additional variable in order to pull school type, grade, and math score for students and then group
# groups to reflect school type and grade and the get the avg math score for grade at eash school
var2 = student_df[['school_type', 'grade', 'math_score']]
var2.groupby(['school_type','grade']).mean().round()


# In[ ]:


# In this module we looked to assist Maria in analyzing data for a school district and to see if there were any large trends
# that could be determined between public and charter schools and to see how their budget may have effected
# test scores. Based off of the findings through out this module public schools on average had a slightly larger budget
# with their test scores remaining roughly the same throughout all 4 years.
# Charter schools had a lower average budget, with their test scores starting higher and then decreasing over
# 4 years. This will lead to ask questions about why this is and we can use different data parameters to rerun this 
# analysis to dive deeper into why the budget may have had different effects on supplies, teachers, etc.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




