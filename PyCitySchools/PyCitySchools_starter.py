#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd
import numpy as py
import random as rd

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.  
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete.head(10)


# In[2]:


#to find total schools, extract school list first
school_count = school_data_complete["school_name"].value_counts()
school_count.head(15)


# In[3]:


#total schools
number_of_school = len(school_count)
print(f" There are totally {number_of_school} schools within the district")


# In[4]:


#Total number of students
student_count = school_data_complete["student_name"].count()
student_count


# In[5]:


#Total_budget
total_budget = school_data["budget"].sum()
total_budget


# In[6]:


#find the average of Math | Reading scores
average_Maths = round(school_data_complete["math_score"].mean(),2)
print(average_Maths)
average_Readings = round(school_data_complete["reading_score"].mean(),2)
print(average_Readings)


# In[7]:


#Another way to do or just cross check the results
school_data_complete.describe()


# In[8]:


# Calculate the percentage of Pass Math 
# find the number of student passed Maths | Reading first, then find the %
passing_math_count = school_data_complete[(school_data_complete["math_score"] >= 70)].count()["student_name"]
passing_math_count


# In[9]:


# Calculate the percentage of Pass Reading
passing_Reading_count = school_data_complete[(school_data_complete["reading_score"]>=70)].count()["student_name"]
passing_Reading_count


# In[10]:


#find % of Math_Pass
Math_pass_percentage = round((passing_math_count/student_count*100),2)
Math_pass_percentage


# In[11]:


#find % of Reading_Pass
Reading_pass_percentage = round((passing_Reading_count/student_count*100),2)
Reading_pass_percentage


# In[12]:


passing_overall_count = school_data_complete[(school_data_complete["reading_score"]>=70) & 
                                              (school_data_complete["math_score"]>=70)].count()["student_name"]
passing_overall_count                                           


# In[13]:


#passing %
overall_passing_percentage = round((passing_overall_count/student_count*100),2)
overall_passing_percentage


# In[14]:


#format the data frame intoschool_name index
school_data_complete_index = school_data_complete.set_index("school_name")
school_data_complete_index.head()


# In[15]:


#check if the data set is clean
school_data_complete.count()


# In[16]:


#


# ## District Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average math score 
# 
# * Calculate the average reading score
# 
# * Calculate the percentage of students with a passing math score (70 or greater)
# 
# * Calculate the percentage of students with a passing reading score (70 or greater)
# 
# * Calculate the percentage of students who passed math **and** reading (% Overall Passing)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# In[17]:


## Creating a summary DataFrame using above values
school_summary_df = pd.DataFrame({"Total School": number_of_school,
                                  "Total Students": student_count,
                                  "Total budget ($)": total_budget,
                                  "Average Math Score(%)": average_Maths,
                                  "Average Reading score (%)": average_Readings,
                                  "% Passing Math": Math_pass_percentage,
                                  "% Passing Reading": Reading_pass_percentage,
                                 "% Overall Passing": overall_passing_percentage},index = [1])
school_summary_df.head()


# ## School Summary

# * Create an overview table that summarizes key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * % Overall Passing (The percentage of students that passed math **and** reading.)
#   
# * Create a dataframe to hold the above results

# In[18]:


#Create df summarizes key metrics ab EACH school
each_school_df = school_data_complete[["school_name","type","budget","reading_score","math_score","student_name"]]
each_school_df.head()


# In[19]:


#groupby school_name; then do mean() to get average budget | average scores
each_school_groupby_df = each_school_df.groupby(["school_name"])

school_name_groupby_df = each_school_groupby_df.mean()
school_name_groupby_df.head(16)


# In[20]:


#total student each school
Total_student =[]
Total_students = school_data_complete["school_name"].value_counts()
Total_students

sch_students = each_school_groupby_df["student_name"].count()
sch_students                               


# In[21]:


# Passing Math|Reading|Overall each school
sch_budget = each_school_groupby_df['budget'].mean()
sch_math = each_school_groupby_df['math_score'].mean()
sch_reading = each_school_groupby_df['reading_score'].mean()
budget_per_student = round((sch_budget/sch_students))
passing_Reading_count_df = each_school_df[(each_school_df["reading_score"]>=70)]
passing_Math_count_df = each_school_df[(each_school_df["math_score"]>=70)]
Overall_passing = each_school_df[(each_school_df["reading_score"]>=70) & 
                                 (each_school_df["math_score"]>=70)]


# In[22]:


sch_budget.head(16)


# In[23]:


passing_Reading_df = passing_Reading_count_df.groupby("school_name")["student_name"].count()
passing_Reading_df.head(16)


# In[24]:


passing_Math_df = passing_Math_count_df.groupby("school_name")["student_name"].count()
passing_Math_df.head()


# In[25]:


Overall_passing_df = Overall_passing.groupby("school_name")["student_name"].count()
Overall_passing_df.head()


# In[26]:


#% % Passing Math: passing_Math / total_students
#% Passing Reading: passing_Reading / total_students
#% Overall Passing: oeverall_passing / total_students 
Percent_Math = passing_Math_df/sch_students
Percent_Math.head()


# In[27]:


Percent_Reading = passing_Reading_df/sch_students
Percent_Reading.head()


# In[28]:


Percent_overall_passing = round((Overall_passing_df/sch_students*100),2)
Percent_overall_passing.head()


# In[29]:


school_types=each_school_df.groupby('school_name')["type"].unique()
school_types


# In[30]:


#create a final df
school_summary_df = pd.DataFrame({'School_type':school_types,'Budget':sch_budget, 'Budget_per_Student':budget_per_student,
                                  'Average Math score':sch_math, 'Average Reading score':sch_reading, 
                                  '% Overall_passing': Percent_overall_passing,'% Passing Maths':Percent_Math, 
                                  '% Passing Reading':Percent_Reading,
                                  'Total Students':sch_students})
school_summary_df.head(16)


# ## Top Performing Schools (By % Overall Passing)

# * Sort and display the top five performing schools by % overall passing.

# In[31]:


#freedom_df = happiness_df.sort_values("Freedom", ascending=False)
Top_five_performing = school_summary_df.sort_values("% Overall_passing", ascending=False)
Top_five_performing.head()


# ## Bottom Performing Schools (By % Overall Passing)

# * Sort and display the five worst-performing schools by % overall passing.

# In[32]:


Five_worst_performing = school_summary_df.sort_values("% Overall_passing", ascending=True)
Five_worst_performing.head()


# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[33]:


Grade_9 = school_data_complete.loc[school_data_complete["grade"] == "9th", ["school_name","grade","math_score"]]
Grade_9.head()


# In[34]:


grade_9_score = Grade_9.groupby("school_name")["math_score"].mean()
grade_9_score.head(16)


# In[35]:


Grade_10 = school_data_complete.loc[school_data_complete["grade"] == "10th", ["school_name","grade","math_score"]]
Grade_10.head()


# In[36]:


grade_10_score = Grade_10.groupby("school_name")["math_score"].mean()
grade_10_score.head()


# In[37]:


Grade_11 = school_data_complete.loc[school_data_complete["grade"] == "11th", ["school_name","grade","math_score"]]
Grade_11.head()


# In[38]:


grade_11_score = Grade_11.groupby("school_name")["math_score"].mean()
grade_11_score.head()


# In[39]:


Grade_12 = school_data_complete.loc[school_data_complete["grade"] == "12th", ["school_name","grade","math_score"]]
grade_12_score = Grade_12.groupby("school_name")["math_score"].mean()
grade_12_score.head()


# In[40]:


#combine all above series of grade-score into a df
Math_score_by_grade = pd.DataFrame({'Grade 9th':grade_9_score,'Grade 10th':grade_10_score, 'Grade 11th':grade_11_score,
                                  'Grade 12th':grade_12_score})
Math_score_by_grade.head(16)


# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[41]:


#Reading score by grade with same Math operations
Grade_9R = school_data_complete.loc[school_data_complete["grade"] == "9th", ["school_name","grade","reading_score"]]
grade_9R_score = Grade_9R.groupby("school_name")["reading_score"].mean()
grade_9R_score.head()


# In[42]:


Grade_10R = school_data_complete.loc[school_data_complete["grade"] == "10th", ["school_name","grade","reading_score"]]
grade_10R_score = Grade_9R.groupby("school_name")["reading_score"].mean()
grade_10R_score.head()


# In[43]:


Grade_11R = school_data_complete.loc[school_data_complete["grade"] == "11th", ["school_name","grade","reading_score"]]
grade_11R_score = Grade_11R.groupby("school_name")["reading_score"].mean()
grade_11R_score.head()


# In[44]:


Grade_12R = school_data_complete.loc[school_data_complete["grade"] == "12th", ["school_name","grade","reading_score"]]
grade_12R_score = Grade_12R.groupby("school_name")["reading_score"].mean()
grade_12R_score.head()


# In[45]:


# Create combination df of Reading score by grade
Reading_score_by_grade = pd.DataFrame({'Grade 9th':grade_9R_score,'Grade 10th':grade_10R_score, 'Grade 11th':grade_11R_score,
                                  'Grade 12th':grade_12R_score})
Reading_score_by_grade.head(16)


# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[46]:


# create df score_df from school_data_complete: 
# define Average Math|Reading|%Passing
#do max|min|bins|labels


# In[47]:


#find the range within by min-max
max_budget = school_summary_df["Budget_per_Student"].max()
min_budget = school_summary_df["Budget_per_Student"].min()
print(max_budget)
print(min_budget)


# In[48]:


#extract the neccessary vaiables | column : score | 
#create new df = above + sch_budget above
#find average score by mean()
#do the bins | labels
#final df re-order 
#score_by_spending = school_data_complete[""]


# In[49]:


#create bins and labels
bins = [0, 585.0, 630.0, 645.0, 680]

group_labels = ["<$585", "$585 - $630", "$631 -  $645", "$646 - $680"]

# Slice the data and place it into bins
pd.cut(school_summary_df["Budget_per_Student"], bins, labels=group_labels).head()


# In[50]:


# Place the binned data series into a new column inside of the df
school_summary_df["Spending range (per student)"] = pd.cut(school_summary_df["Budget_per_Student"], bins, labels=group_labels)
school_summary_df.head()


# In[51]:


#reset index to Spending range
summary_per_spending = school_summary_df.reset_index()
summary_per_spending.head()
summary_per_spending.groupby("Spending range (per student)")


# In[52]:


summary_per_spending1 = summary_per_spending[["Spending range (per student)","Average Math score","Average Reading score","% Overall_passing",
                                              "% Passing Maths","% Passing Reading"]]
summary_per_spending1.head()


# In[53]:


summary_per_spending1.groupby("Spending range (per student)").mean()
summary_per_spending1.head()


# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[54]:


# add size colum from data_complete to school_summary_df

score_size = school_summary_df.reset_index()
score_size.head()


# In[55]:


score_size_df = score_size[["Total Students","Average Math score","Average Reading score","% Overall_passing",
                           "% Passing Maths","% Passing Reading"]]
score_size_df = score_size_df.rename(columns={"Total Students": "School size"})
score_size_df.head()


# In[56]:


#find the range within by min-max of school_size & double if this column is numberic
max_size = score_size_df["School size"].max()
min_size = score_size_df["School size"].min()
print(max_size)
print(min_size)


# In[57]:


# do bins and labels
bins = [0, 1000, 2000, 5000]

group_labels = ["Small (<1000)", "Medium (1000 - 2000)", "Large (2000 -  5000)"]

# Slice the data and place it into bins
pd.cut(score_size_df["School size"], bins, labels=group_labels).head()


# In[58]:


#place new column of size range to score_size df
score_size_df["School size"] = pd.cut(score_size_df["School size"], bins, labels=group_labels)
score_size_df.head()


# In[59]:


# groupby for final result
score_size_group_df = score_size_df.groupby("School size").mean()
score_size_group_df.head()


# ## Scores by School Type

# * Perform the same operations as above, based on school type

# In[60]:


score_size.head()


# In[61]:


Type_df = score_size.loc[:,["School_type", "Average Math score", "Average Reading score","% Overall_passing",
                            "% Passing Maths","% Passing Reading"]]
Type_df.head()


# In[62]:


#Type_df["School_type"].value_counts()


# In[71]:


Type_df = Type_df.replace({"[Charter]": "Charter", "[District]": "District"})
Type_df.head()


# In[72]:


#groupby to get final result:
Type_score_df = Type_df.groupby("School_type").mean()
Type_score_df.head()


# In[ ]:




